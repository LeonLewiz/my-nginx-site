#!/bin/sh
set -e

export PGPASSWORD="$DB_PASSWORD"

STAMP=$(date +%Y-%m-%d-%H%M)
FILE="/tmp/db-$STAMP.sql.gz"

pg_dump -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" | gzip > "$FILE"

aws --region ru-central1 --endpoint-url=https://storage.yandexcloud.net \
  s3 cp "$FILE" "s3://devops-study-backops/db-$STAMP.sql.gz"

rm -f "$FILE"
echo "backup done: db-$STAMP.sql.gz"
