# Dockerfile for myweb

FROM python:3.9-slim

WORKDIR /app

# 1. Install TailPySCSS (Local Library)
COPY . /app
RUN pip install -e .

# 2. Setup Project
WORKDIR /app/my-website/myweb
COPY my-website/myweb/start.sh /app/my-website/myweb/start.sh
RUN chmod +x /app/my-website/myweb/start.sh

# 3. Serve via start script (Watch + Serve)
CMD ["./start.sh"]
