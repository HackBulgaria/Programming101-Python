# Car Racing

You are a big car racing fan!

You want to implement a Python program, that is going to simulate a car race. It feels good to add all your friends and their cars and watch them go round and round. And, of course, some times - even crash.

Your championship is going to consist of several races.

The contestants are located in an extral `cars.json` file that you have to load. There is a sample [`cars.json`](cars.json) file in this repository.

Your final idea is to implement a program that:

- Loads `cars.json` file
- Runs the races
- After every race - store the result in  `result.json` - you should keep the points of every contestant for the given race. 

Here is a complete breakdown of the classes that you want to have:

## Car

`Car` class will have the following methods:

- `__init__`, which takes `car`, `model` and `max_speed`
- All dunders you need - for example, `__str__` would be nice

## Driver

`Driver` class will have the following methods:

- `__init__` takes `name`, `car` (which is an object from `Car` class) 
- All dunders you need - for example, `__str__` would be nice

## Race

`Race` class will have:
- `__init__` takes `drivers`(list of `Driver`-s) and `crash_chance` (chance for crash for every race - number between 0 and 1)
- `result()` - returns the standings after the race + the crashed drivers.

Every driver takes a points for his place in a ranking list:

* For first place - 8
* Second place - 6
* Third place - 4.
* All other places are scored with 0.

**If someone crashes, he takes no points for the given race.**

You must save the result for the given race in `result.json`.

## Championship

`Championship` class will have:

- `__init__` takes `name` and `races_count` - how many races we need to make for the given championship. 
- `top3()` - returns the best 3 drivers after final race

Use the name of the championship as a unique key for it. This will help you store the data.

## Bundling everything together

In order to make the race happen, we need to glue everything together.

Here is an example usage:

```
$ python3 race.py
Hello PyRacer!
Please, call command with the proper argument:
 $ python3 race.py start <name> <races_count> -> This will start a new championship with the given name, races count and drivers from cars.json
 $ python3 race.py standings -> This will print the standings for each championship that has ever taken place.
```

If we want to start:

```
$ python3 race.py start pandarace 3
Starting a new championship called pandarace with 3 races.
Running 3 races ...

Race #1
###### START ######
Ivo - 8
Pavlin - 6
Slavqna - 4

Race #2
###### START ######
Ivo - 8
Slavqna - 6
Rado - 4

Unfortunately, Pavlin has crashed.

Race #3
###### START ######
Rado - 8

Unfortunately, Ivo has crashed.
Unfortunately, Slavqna has crashed.
Unfortunately, Pavlin has crashed.

Total championship standings:

Ivo - 16
Rado - 12
Slavqna - 10
Pavlin - 6
```

Figure out how to store everyting in the `result.json` file!
