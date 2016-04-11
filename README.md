## hello-configo

```bash
docker build -t hello-configo .

docker run \
  -e CONFIGO_SOURCE_0='{"type": "http", "format": "yaml", "url": "http://localhost:8000/static/dev.yml"}' \
  hello-configo

docker run \
  -e CONFIGO_SOURCE_0='{"type": "http", "format": "yaml", "url": "https://localhost:8000/dev.yml"}' \
  hello-configo

```
