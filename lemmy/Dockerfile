FROM dessalines/lemmy:0.19.20

USER root
COPY lemmy/entrypoint.sh /usr/local/bin/railway-lemmy-entrypoint
RUN chmod 0755 /usr/local/bin/railway-lemmy-entrypoint \
    && mkdir -p /config \
    && chown -R lemmy:lemmy /config
USER lemmy

ENTRYPOINT ["/usr/local/bin/railway-lemmy-entrypoint"]
