
```shell
# Dumping model data into json
python3 manage.py dumpdata shop.Product --format json --output product.json
python3 manage.py dumpdata shop.ProductImage --format json --output productImage.json
python3 manage.py dumpdata shop.ProductImages --format json --output productImage.json
python3 manage.py dumpdata shop.ProductSecondaryImages --format json --output productImage.json
python3 manage.py dumpdata shop.Review --format json --output review.json
```
```shell
python manage.py loaddata app_name_dump.json
```