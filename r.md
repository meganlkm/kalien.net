kalien.net
===========

## Deploy

### DEV
	$> rsync -avz -e ssh --exclude-from .build-exclude ./ kalien:~/dev/ --delete

###  PROD
	$> rsync -avz -e ssh --exclude-from .build-exclude ./main-app/ kalien:~/main-app/ --delete
	$> rsync -avz -e ssh --exclude-from .build-exclude ./public_html/ kalien:~/public_html/ --delete
