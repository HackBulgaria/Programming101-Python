# Consuming JSON APIs

We are going to introduce the concept for HTTP clients by using the famous [requests](http://docs.python-requests.org/en/master/) Python library.

Your job is to consume 2 APIs:

* [The first one returns a list of all airlines and the countries they are from.](http://astral.hacksoft.io/api/airline/)
* Since country codes are not very descriptive, we are going to use [another API that maps country code to country name](http://data.okfn.org/data/core/country-list/r/data.json)

Write a Python program that produces the following histogram: `country_name: # of airports in it`.

Save that histogram to a JSON file.

It should look something like this:

```json
{
  "Moldova": 5,
  "USA": 555,
  ...
}
```

## Extra Credit

Using the `simple_http_server.py` and SQLAlchemy, make a Flask server that can answer the following question: **How many airlines are there in a country?**

The server should answer with the following routes:

```
GET /airlines?country=Bulgaria
GET /airlines?country_code=BG
```

Some steps that can help you structure your program:

1. Make models in SQLAlchemy
2. Import the JSON data into SQL database via that models
3. Implement a Flask serve with that models & database
4. Make the `/airlines` route answer the question.
