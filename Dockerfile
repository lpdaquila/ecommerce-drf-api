FROM alpine AS builder

RUN apk add --no-cache ca-certificates curl tar gzip && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

FROM debian:stable-slim

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local/bin/uv /root/.local/bin/uv

WORKDIR /app

COPY . .

ENV PATH="/root/.local/bin:${PATH}"

EXPOSE 8000

RUN uv run manage.py check

CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]

