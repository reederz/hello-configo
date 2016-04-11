FROM node

RUN curl -L https://github.com/zeroturnaround/configo/releases/download/v0.1.0/configo.linux-amd64 >/usr/local/bin/configo && \
    chmod +x /usr/local/bin/configo

ADD . /app
WORKDIR /app

CMD ["configo", "node", "server.js"]
