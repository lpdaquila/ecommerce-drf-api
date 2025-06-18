FROM debian:stable-slim AS builder

RUN apt-get update && \
    apt-get install -y ca-certificates curl tar gzip && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock .python-version ./

RUN uv sync --locked

COPY . .

RUN .venv/bin/python manage.py check
    
FROM debian:stable-slim
    
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*
    
COPY --from=builder /root/.local/bin/uv /root/.local/bin/uv
COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:/root/.local/bin:$PATH"
    
WORKDIR /app

EXPOSE 8000

RUN uv venv --allow-existing 

CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]

