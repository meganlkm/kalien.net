#!/bin/bash

case "$1" in
  dev)
    rsync -avz -e ssh --exclude-from ./.build-exclude ./ kalien:~/dev/ --delete
    ;;
  production)
    rsync -avz -e ssh --exclude-from ./.build-exclude ./main-app/ kalien:~/main-app/ --delete
    rsync -avz -e ssh --exclude-from ./.build-exclude ./public_html/ kalien:~/public_html/ --delete
    ;;
  *)
    echo $"Usage: $prog {dev|production}"
esac
