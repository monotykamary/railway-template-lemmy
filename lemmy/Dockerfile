FROM dessalines/lemmy:0.19.21@sha256:839d72704b10d574a21dacab046d9369e241366e4092b950d801e821f779de29

USER root
COPY lemmy/entrypoint.sh /usr/local/bin/railway-lemmy-entrypoint
RUN chmod 0755 /usr/local/bin/railway-lemmy-entrypoint \
    && mkdir -p /config \
    && chown -R lemmy:lemmy /config
USER lemmy

ENTRYPOINT ["/usr/local/bin/railway-lemmy-entrypoint"]
