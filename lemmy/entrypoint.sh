#!/bin/sh
set -eu

required="LEMMY_HOSTNAME LEMMY_DATABASE_URL PICTRS_URL PICTRS_API_KEY LEMMY_ADMIN_USERNAME LEMMY_ADMIN_PASSWORD LEMMY_SITE_NAME"
for name in $required; do
  eval "value=\${$name:-}"
  if [ -z "$value" ]; then
    echo "Missing required environment variable: $name" >&2
    exit 1
  fi
done

escape_json() {
  printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g'
}

hostname=$(escape_json "$LEMMY_HOSTNAME")
database_url=$(escape_json "$LEMMY_DATABASE_URL")
pictrs_url=$(escape_json "$PICTRS_URL")
pictrs_api_key=$(escape_json "$PICTRS_API_KEY")
admin_username=$(escape_json "$LEMMY_ADMIN_USERNAME")
admin_password=$(escape_json "$LEMMY_ADMIN_PASSWORD")
site_name=$(escape_json "$LEMMY_SITE_NAME")

cat > /config/config.hjson <<EOF
{
  hostname: "$hostname"
  bind: "0.0.0.0"
  port: 8536
  tls_enabled: true
  cors_origin: "https://$hostname"
  database: {
    uri: "$database_url"
    pool_size: 10
  }
  pictrs: {
    url: "$pictrs_url"
    api_key: "$pictrs_api_key"
    image_mode: "StoreLinkPreviews"
  }
  setup: {
    admin_username: "$admin_username"
    admin_password: "$admin_password"
    site_name: "$site_name"
  }
  federation: {
    concurrent_sends_per_instance: 1
  }
  json_logging: true
}
EOF

export LEMMY_CONFIG_LOCATION=/config/config.hjson
exec /usr/local/bin/lemmy_server
