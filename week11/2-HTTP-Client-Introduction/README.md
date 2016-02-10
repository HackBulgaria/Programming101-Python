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
