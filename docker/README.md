# Build a scrapers-ca Docker development environment:
```
docker pull ubuntu:17.10
docker-compose build
docker-compose up -d
docker-compose exec scrapers-ca service postgresql start
docker-compose exec scrapers-ca sudo -u postgres createuser root
docker-compose exec scrapers-ca sudo -u postgres psql -c 'ALTER USER root WITH SUPERUSER;'
docker-compose exec scrapers-ca sudo -u postgres psql -c "ALTER USER root WITH PASSWORD 'root';"
docker-compose exec scrapers-ca sudo -u postgres createdb pupa
docker-compose exec scrapers-ca sudo -u postgres psql pupa -c "CREATE EXTENSION postgis;"
docker-compose exec scrapers-ca sed -i -e 's/localhost/root:root@localhost/' /src/scrapers-ca/pupa_settings.py
```

# Alter pupa_settings:
`docker-compose exec scrapers-ca sed -i -e 's/localhost/root:root@localhost/' /src/scrapers-ca/pupa_settings.py`

# ssh into the Docker environment:
`docker-compose exec scrapers-ca /bin/bash`

# Usage
```
cd scrapers-ca
mkvirtualenv scrapers-ca --python=`which python3`
pip install -r requirements.txt
pupa dbinit ca
```
You can now run your scraper. Ex: `pupa update ca_on_candidates`

# To wipe the database:
```
docker-compose exec scrapers-ca sudo -u postgres dropdb pupa
docker-compose exec scrapers-ca sudo -u postgres createdb pupa
docker-compose exec scrapers-ca /bin/bash
pupa dbinit ca
```