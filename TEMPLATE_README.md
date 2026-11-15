# Deploy and Host Lemmy on Railway

Deploy a production-ready **Lemmy** instance on Railway. Lemmy is an open-source, federated link aggregator and forum—a self-hosted alternative to Reddit that participates in the Fediverse through ActivityPub.

## About Hosting Lemmy

A Lemmy deployment needs an API and federation server, server-rendered web UI, PostgreSQL database, persistent image service, and a shared public origin. This template provisions those components as five Railway services connected through private networking. Only the Proxy service is publicly exposed.

The template pins Lemmy and Lemmy UI 0.19.21, Pict-rs 0.5.25, and Caddy 2.11.4. It generates independent administrator, media, and database secrets and persists both application data and uploaded media across redeployments.

## Why Deploy Lemmy on Railway?

- Deploy the complete multi-service stack in one operation.
- Keep PostgreSQL and Pict-rs data on persistent Railway volumes.
- Route UI, API, media, and ActivityPub traffic through one HTTPS domain.
- Use Railway private networking for all internal service communication.
- Receive generated credentials instead of sharing template-wide secrets.
- Inspect logs, metrics, deployments, and volume usage from one project.

## Common Use Cases

- Run a public federated discussion community.
- Create a private or approval-only organization forum.
- Host a topic-specific alternative to centralized social platforms.
- Test ActivityPub federation and moderation workflows.
- Operate a regional or community-owned social network.

## Dependencies for Lemmy Hosting

The template includes every required server-side dependency:

- **Lemmy 0.19.21** — API, federation, moderation, and background jobs
- **Lemmy UI 0.19.21** — responsive server-rendered web interface
- **Pict-rs 0.5.25** — persistent image uploads and thumbnails
- **Postgres** — persistent application database
- **Caddy 2.11.4 Proxy** — one public HTTPS origin for UI, API, media, and federation

### Deployment Dependencies

No external database or object-storage account is required. Railway provisions two persistent volumes: one for PostgreSQL and one for Pict-rs media. The Lemmy service builds from the pinned wrapper source using the official upstream runtime image. Lemmy UI, PostgreSQL, Pict-rs, and the existing Caddy proxy adapter use digest-pinned images; the proxy adapter is unchanged by this application update.

After deployment:

1. Open the generated Proxy domain.
2. Sign in with `LEMMY_ADMIN_USERNAME` and `LEMMY_ADMIN_PASSWORD` from the Lemmy service variables.
3. Change the generated administrator password.
4. Configure the site name, description, registration policy, and federation settings.
5. Optionally attach a custom domain to Proxy.

Choose the final domain before building a public community. ActivityPub identities are tied to the instance hostname and cannot be migrated by simply changing domains.

## Upgrade precautions and validation scope

Back up PostgreSQL and the Pict-rs media volume and retain the generated secrets before upgrading. Keep Lemmy and Lemmy UI on matching versions. The 0.19.20-to-0.19.21 checks preserved the original administrator, community, post, and the originally retrieved image bytes across upgrade and redeployment. Restore matching backups if rolling back a schema change.

The English UI, authentication failures, media retrieval, and local ActivityPub/WebFinger endpoints were checked. End-to-end delivery to another federated instance was not tested. Two inherited Chinese (`zh`) locale startup diagnostics remain; Chinese-language behavior was not validated, and the warnings are not represented as fixed by this release.

## Source and Documentation

- [Template source](https://github.com/monotykamary/railway-template-lemmy)
- [Lemmy documentation](https://join-lemmy.org/docs/)
- [Lemmy source](https://github.com/LemmyNet/lemmy)
