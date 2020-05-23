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
$ docker-compose build
$ docker-compose up -d
```
## Testing our API
Return a timeseries with the price info of the company associated with a ticker for the specified start_date and end_date dates
```sh
$ http://localhost:28000/api/prices/?ticker=GOOG&start_date=2020-05-01&end_date=2020-05-24
```
Company info
```sh
$ http://localhost:28000/api/companies/
```
Recommendations
```sh
$ http://localhost:28000/api/recommendations?ticker=NFLX&start_date=2020-01-01&end_date=2020-05-24
```