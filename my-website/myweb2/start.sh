#!/bin/sh
# Start the watcher in the background
# -u uses unbuffered output so logs show up immediately in Docker
python -u -m tailpyscss.cli watch &

# Start the web server in the foreground
python -u -m http.server 8000
