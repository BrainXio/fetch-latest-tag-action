# Use the lightweight Python image
FROM python:3.10-alpine

# Install dependencies
RUN apk add --no-cache curl jq

# Copy the Python entrypoint script
COPY main.py /main.py

# Set the entrypoint
ENTRYPOINT ["python3", "/main.py"]
