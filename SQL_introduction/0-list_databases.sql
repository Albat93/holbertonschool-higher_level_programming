#!/bin/bash

# MySQL credentials
HOST="localhost"
USER="root"
PASSWORD="password"

# Command to list all databases
mysql -h$HOST -u$USER -p$PASSWORD -e "SHOW DATABASES;"
