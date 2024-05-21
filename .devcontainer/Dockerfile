ARG VARIANT="3.10"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN pip install poetry==1.3.1
RUN poetry config virtualenvs.create false
RUN poetry lock --no-update --check
RUN poetry install

# Install wget
RUN apt-get update \
    && apt-get install -y wget

# Install utils and tools
RUN apt-get install -y bat exa fd-find fzf git htop jq less ripgrep tldr tree

WORKDIR /workspace

ENV PYTHONPATH /workspace
CMD ["uvicorn", "src.main.app:app", "--host", "0.0.0.0", "--port", "80"]
