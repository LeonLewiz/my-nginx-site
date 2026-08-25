#!/bin/zsh

cd /var/www/html/my-nginx-site

git reset --hard origin/main
git pull origin main

docker compose build --no-cache
docker compose up -d --build --force-recreate

echo " Полный деплой (Nginx + Python + Postgres)."
