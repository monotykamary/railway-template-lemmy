# Lemmy on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/lemmy?referralCode=ZqgrJ0)

Production-oriented Railway template source for [Lemmy](https://join-lemmy.org/), a federated link aggregator and discussion platform.

## Architecture

- **Lemmy** — API, federation, and background jobs, pinned to 0.19.20
- **Lemmy UI** — server-rendered web interface, pinned to 0.19.20
- **Pict-rs** — persistent image storage, pinned to 0.5.19
- **Postgres** — Railway-managed persistent database
- **Proxy** — Caddy edge service routing UI, API, ActivityPub, and image traffic through one public origin

Only Proxy receives a public domain. Internal service traffic uses Railway private networking.

## First login

Open the generated Railway domain and sign in with the values configured as `LEMMY_ADMIN_USERNAME` and `LEMMY_ADMIN_PASSWORD` on the Lemmy service. Change the generated password after the first login.

## Updating

Keep Lemmy and Lemmy UI on matching versions. Update the image tags in the Railway project and the base image in `lemmy/Dockerfile`, test federation and image uploads, then publish a new template revision.

## Upstream

- [Lemmy](https://github.com/LemmyNet/lemmy)
- [Lemmy UI](https://github.com/LemmyNet/lemmy-ui)
- [Pict-rs](https://git.asonix.dog/asonix/pict-rs)
