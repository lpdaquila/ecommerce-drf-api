FROM debian:stable-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc build-essential

COPY uv.lock pyproject.toml .python-version ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project 

ADD . . 

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
    
FROM debian:stable-slim
    
RUN apt-get update && \
    apt-get install -y ca-certificates libpq-dev && \
    rm -rf /var/lib/apt/lists/*
    
COPY --from=builder --chown=app:app /app/.venv /app/.venv
    
WORKDIR /app

COPY . .

RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv venv --allow-existing

ENV VIRTUAL_ENV="/app/.venv"
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "core.wsgi"]
