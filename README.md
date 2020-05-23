# Dystematic
### Description
REST api backed by a PostgreSQL instance to expose historical market data from Yahoo! finance.
## Installation
### Clone project
Clone project using Git over SSH.
```sh
$ git clone git@github.com:jeandias/dystematic.git
$ cd dystematic
```
### Install dependencies for project
```sh
$ docker build .
$ docker-compose build
$ docker-compose up -d
```
## Testing our API
```sh
$ http://localhost:28000
```
