FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN apt update
RUN apt install -y python3-dev libpq-dev build-essential
RUN pip install pipenv 
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["bash"]