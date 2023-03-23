FROM python:3.10-slim-buster

# Create working directory
WORKDIR /opt

# Copy dependencies and source code
COPY ["./", "./"]

# Install dependencies
RUN python3 -m pip install -e ".[dev]"

# Entry point. Run the app
CMD ["python", "./app/main.py", "--port", "8001", "host", "0.0.0.0"]
