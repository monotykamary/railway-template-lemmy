# Lemmy

Deploy a production-ready **Lemmy** instance on Railway. Lemmy is an open-source, federated link aggregator and forum—a self-hosted alternative to Reddit that participates in the Fediverse through ActivityPub.

## Included services

- **Lemmy** — API, federation, moderation, and background jobs
- **Lemmy UI** — responsive server-rendered web interface
- **Pict-rs** — persistent image uploads and thumbnails
- **Postgres** — persistent application database
- **Proxy** — one public HTTPS origin for the UI, API, images, and federation

All application traffic between services uses Railway private networking. Only the Proxy service is publicly exposed.

## After deployment

1. Open the generated Proxy domain.
2. Sign in using `LEMMY_ADMIN_USERNAME` and `LEMMY_ADMIN_PASSWORD` from the Lemmy service variables.
3. Change the generated administrator password.
4. Configure the site name, description, registration policy, and federation settings from the administration panel.
5. Optionally attach a custom domain to Proxy. **Choose the final domain before building a public community**: ActivityPub identities are tied to the instance hostname and cannot be migrated by simply changing domains.

## Persistence

Postgres stores communities, users, posts, and configuration. Pict-rs stores uploaded media on its attached Railway volume. Both survive application redeployments.

## Versioning

The template pins Lemmy and Lemmy UI to matching stable releases and pins Pict-rs. Review upstream release notes before upgrading.

## Source and documentation

- [Template source](https://github.com/monotykamary/railway-template-lemmy)
- [Lemmy documentation](https://join-lemmy.org/docs/)
- [Lemmy source](https://github.com/LemmyNet/lemmy)
