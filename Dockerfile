FROM ubuntu:noble-20250529
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y curl ca-certificates 
    # curl -LsSf https://astral.sh/install.sh | sh 

ADD https://astral.sh/uv/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock .python-version ./

RUN uv venv && \
uv pip install -r pyproject.toml

COPY . .

EXPOSE 8000

CMD ["uv", "run", "manage.py", "runserver"]