# LC_API

This repo contains the code for the LendingClub API

![Test](https://github.com/chineidu/LC_API/actions/workflows/test.yml/badge.svg)

## Table of Content

- [LC\_API](#lc_api)
  - [Table of Content](#table-of-content)
  - [Note](#note)
    - [Dockerfile](#dockerfile)
    - [docker-compose file](#docker-compose-file)

## Note

- Deploy the API using `Railway App` works best without a custom docker-compose file.
- The files shown below are the Dockerfile and the docker-compose file that was used locally.

### Dockerfile

```Dockerfile
FROM python:3.10-slim-buster

# Create working directory
WORKDIR /opt

# Copy dependencies and source code
COPY ["./", "./"]

# Install dependencies
RUN python3 -m pip install -e ".[dev]"

# Entry point. Run the app
CMD ["python", "./app/main.py", "--port", "8001", "host", "0.0.0.0"]
```

### docker-compose file

```docker-compose
version: "3.7"

services:
  lc_api:
    build:
        context: .
    ports:
      - "8001:8001"
    volumes:
      - .:/opt

```
