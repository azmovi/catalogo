FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app

WORKDIR /app
RUN uv sync --frozen

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "--host", "0.0.0.0", "catalogo.app:app"]
