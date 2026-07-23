FROM dessalines/lemmy:0.19.20

USER root
COPY --chmod=755 entrypoint.sh /usr/local/bin/railway-lemmy-entrypoint
RUN mkdir -p /config && chown -R lemmy:lemmy /config
USER lemmy

ENTRYPOINT ["/usr/local/bin/railway-lemmy-entrypoint"]
