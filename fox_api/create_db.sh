sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
sudo -u postgres psql --command="\i create_postgres_db.sql"
