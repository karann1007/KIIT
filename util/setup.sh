#!/usr/bin/env bash

# Start mysql
mysqld_safe --skip-grant-tables &
sleep 2
mysql -e "FLUSH PRIVILEGES"
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'admin'"
service mysql start
sleep 2
mysql -u root --password=admin -e "create database db"

# Start mongo
#/usr/bin/mongod --port 27017 --dbpath /data/db
/usr/bin/mongod --port 27017 --dbpath /data/db >/dev/null 2>&1 &
ps aux | grep mongo
sleep 5
wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/backend-project/database/mongo-database.js
mongo < mongo-database.js

# Start server
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000