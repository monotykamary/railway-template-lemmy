# Lemmy on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/lemmy?referralCode=ZqgrJ0)

Production-oriented Railway template source for [Lemmy](https://join-lemmy.org/), a federated link aggregator and discussion platform.

## Architecture

- **Lemmy** — API, federation, and background jobs, pinned to 0.19.21
- **Lemmy UI** — server-rendered web interface, pinned to 0.19.21
- **Pict-rs** — persistent image storage, pinned to 0.5.25
- **Postgres** — Railway-managed persistent database
- **Proxy** — Caddy 2.11.4 edge service routing UI, API, ActivityPub, and image traffic through one public origin

Only Proxy receives a public domain. Internal service traffic uses Railway private networking.

## First login

Open the generated Railway domain and sign in with the values configured as `LEMMY_ADMIN_USERNAME` and `LEMMY_ADMIN_PASSWORD` on the Lemmy service. Change the generated password after the first login.

## Updating

Keep Lemmy and Lemmy UI on matching versions. Review Pict-rs and Caddy security releases independently, update the relevant source or image pins, test federation and image uploads, then publish the GitHub and Railway revisions together.

## Upgrade precautions and validation scope

Back up PostgreSQL and the Pict-rs media volume and retain the generated secrets before upgrading. Keep Lemmy and Lemmy UI on matching versions. The 0.19.20-to-0.19.21 checks preserved the original administrator, community, post, and the originally retrieved image bytes across upgrade and redeployment. Restore matching backups if rolling back a schema change.

The English UI, authentication failures, media retrieval, and local ActivityPub/WebFinger endpoints were checked. End-to-end delivery to another federated instance was not tested. Two inherited Chinese (`zh`) locale startup diagnostics remain; Chinese-language behavior was not validated, and the warnings are not represented as fixed by this release.

## Upstream

- [Lemmy](https://github.com/LemmyNet/lemmy)
- [Lemmy UI](https://github.com/LemmyNet/lemmy-ui)
- [Pict-rs](https://git.asonix.dog/asonix/pict-rs)
