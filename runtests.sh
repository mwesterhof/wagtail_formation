#!/bin/sh

cd tests/testproject/
mkdir static
./manage.py migrate
./manage.py loaddata testbed.json
./manage.py test
rm db.sqlite3
rmdir static
