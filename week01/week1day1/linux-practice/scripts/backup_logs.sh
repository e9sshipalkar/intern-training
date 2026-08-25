#!/bin/bash
SOURCE_DIR="$1"
if [ ! -d  "$SOURCE_DIR" ]; then
  echo "Error: Source directory does not exist : $SOURCE_DIR"
  exit 1
fi
KEEP="$2" 
if [ -z "$KEEP" ]; then
  echo "Usage: $0 <source_directory> <number_of_backups_to_keep>"
  exit 1
fi
ARCHIVE_DIR="./archives"
mkdir -p "$ARCHIVE_DIR" 

NAME="$(basename "$SOURCE_DIR")" 
DATE="$(date +%F)"
ARCHIVE="$ARCHIVE_DIR/$NAME-$DATE.tar.gz"

tar -czf "$ARCHIVE" "$SOURCE_DIR" 
echo "Backup created: $ARCHIVE"

ARCHIVES=$(ls -t "$ARCHIVE_DIR"/"$NAME"-*.tar.gz 2>/dev/null)

COUNT=$(echo "$ARCHIVES" | wc -l)
if [ "$COUNT" -gt "$KEEP" ]; then
    echo "$ARCHIVES" | tail -n +$((KEEP + 1)) | while read FILE
    do
        rm "$FILE"
        echo "Deleted old backup: $FILE"
    done

fi
echo "Backup process completed."