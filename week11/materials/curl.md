# HTTP Client with curl

`curl` is a very helpful and useful tool when you have to deal with HTTP calls.

Since it may not be available in your distro, make sure that you install it:

```
$ sudo apt-get install curl
```

## Making GET requests

The simplest thing you can do with `curl` is to make a GET request to a URL

```
$ curl https://hackbulgaria.com/

<some html here>
```

If you want to see the response headers, you can call curl with `-I`:

```
$ curl -I https://hackbulgaria.com/
HTTP/1.1 200 OK
Server: nginx/1.8.0
Date: Wed, 10 Feb 2016 12:03:57 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
Content-Language: bg
Vary: Accept-Language, Cookie
```

This is very helpful in order to debug things.

If you want to see request headers, you can do the following things:


1. Start a netcat server at some port: `$ nc -l 8000`
2. Execute: `$ curl https://localhost:8000`
3. On the `nc` tab you will see the **request headers**

```
GET / HTTP/1.1
User-Agent: curl/7.37.1
Host: localhost:8000
Accept: */*
```


The other way is to execute:

```
$ curl -vs https://hackbulgaria.com > /dev/null

... some output ...
> GET / HTTP/1.1
> User-Agent: curl/7.37.1
> Host: hackbulgaria.com
> Accept: */*
> 
< HTTP/1.1 200 OK
* Server nginx/1.8.0 is not blacklisted
< Server: nginx/1.8.0
< Date: Wed, 10 Feb 2016 12:06:01 GMT
< Content-Type: text/html; charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-Frame-Options: SAMEORIGIN
< Content-Language: bg
< Vary: Accept-Language, Cookie
< 
```

`-vs` means `verbose` and `silent` and we redirect the HTML output to `/dev/null`

## Making POST requests

**We are going to use our simple Flask HTTP server that is located in `materials` folder.**

In order to run it, you have to follow these two simple steps:

1. Install requirements: `$ pip install -r requirements.txt` in a proper virtualenv.
2. Run: `$ python3 simple_http_server.py`

---

In order to make a `POST` request, we can use the `-X` flag from the curl command.

```
$ curl -X POST http://localhost:5000
{
    "get_data": {},
    "post_data": {},
    "method": "POST",
    "headers": {
        "Host": "localhost:5000",
        "Content-Type": "",
        "Content-Length": "",
        "User-Agent": "curl/7.37.1",
        "Accept": "*/*"
    }
}%
```

If we want to send some POST data, we can use the `-d` flag:


```
$ curl -X POST -d "name=rado&age=23" http://localhost:5000
{
    "get_data": {},
    "post_data": {
        "age": "23",
        "name": "rado"
    },
    "method": "POST",
    "headers": {
        "Host": "localhost:5000",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "16",
        "User-Agent": "curl/7.37.1",
        "Accept": "*/*"
    }
}% 
```

Also, we can send a GET request with parameters, placed in the URL:

```
curl http://localhost:5000\?name\=rado\&age\=23
{
    "get_data": {
        "age": "23",
        "name": "rado"
    },
    "post_data": {},
    "method": "GET",
    "headers": {
        "Host": "localhost:5000",
        "Content-Type": "",
        "Content-Length": "",
        "User-Agent": "curl/7.37.1",
        "Accept": "*/*"
    }
}%
```

If we want to send some custom headers, we can use `-H` flag:

```
$ curl -H "Content-Type: application/json" http://localhost:5000\?name\=rado\&age\=23
{
    "get_data": {
        "age": "23",
        "name": "rado"
    },
    "post_data": {},
    "method": "GET",
    "headers": {
        "Host": "localhost:5000",
        "Content-Type": "application/json",
        "Content-Length": "",
        "User-Agent": "curl/7.37.1",
        "Accept": "*/*"
    }
}
```

[**You can see a list of valid HTTP headers here**](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)


Play with that simple server.
