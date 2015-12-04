# Car Racing

You are a big car racing fan!

You want to implement a Python program, that is going to simulate a car race. It feels good to add all your friends and their cars and watch them go round and round. And, of course, some times - even crash.

Your championship is going to consist of several races.

The contestants are located in an extral `cars.json` file that you have to load. There is a sample [`cars.json`](cars.json) file in this repository.

Your final idea is to implement a progrma that:

- Loads `cars.json` file
- Runs the races
- And after every race - store the result in  `rating.json` - you should keep the points of every contestant for the given race. 

Here is a complete breakdown of the classes that you want to have:

## Car

`Car` class will have the following methods:

- `__init__`, which takes `car`, `model` and `max_speed`
- All dunders you need - for example, `__str__` would be nice

## Driver

`Driver` class will have the following methods:

- `__int__` takes `name`, `car` (which is a object from `Car` class) 
- All dunders you need - for example, `__str__` would be nice

## Race

`Race` class will have:
- `__int__` takes `drivers`(list of `Driver`-s) and `crash_chance` (chance for crash for every race - number between 0 and 1)
- `crash()` - some of the drivers crash and take no points
- `standings()` - returns the standings after the race.

Every driver takes a points for his place in a ranking list. 

For first place - 8, second place - 6, third place - 4. All other places are scored with 0.

You must save the result for the given race in `rating.json`.

## Championship

`Championship` class will have:

- `__int__` takes `races_count` - how many races we need to make for the given championship. 
- `top3()` - returns the best 3 drivers after final race

## Bundling everything together

In order to make the race happen, we need to glue everything together.

Here is an example usage:

```
$ python3 race.py
Hello to PyRacer!
Please, call the command with the proper argument:
 $ python3 race.py start 10 -> This will start a new championship with 10 races and drivers from cars.json
 $ python3 race.py standings -> This will print the standings for each race and championship that has taken place.
```

If we want to start:

```
$ python3 race.py start 3
Starting a new championship with 3 races. The unique id for this championship is panda3
Running 3 races ...

Race #1
###### START ######

```
