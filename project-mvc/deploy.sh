#!/bin/bash
docker pull ghcr.io/zulfachmad/mvc-app:v2-prod
docker stop app-v1 || true && docker rm app-v1 || true
docker run -d --name app-v2 -p 8081:5000 ghcr.io/zulfachmad/mvc-app:v2-prod