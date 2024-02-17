FROM alpine:latest

# Install Python 3, pip for Python 3, and iproute2
RUN apk update && \
    apk add --no-cache python3 py3-pip iproute2

WORKDIR /app

COPY app.py /app/
COPY IF.txt /home/data/
COPY Limerick-1.txt /home/data/

# Set the entrypoint script as the entrypoint for the container
CMD ["python3", "app.py"]
