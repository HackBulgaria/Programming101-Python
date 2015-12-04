#Formula1

You should implement a whole `championship`. A `championship` has several `races`. You have a `cars.json` file in this repo. Every `driver` has `car` (model and max_speed). 

Write program:
- Read cars.json file as an argument in the console.
- After every race - in new file `rating.(json or csv file)` write information about current points for every driver. 

## Car
`Car` class will have the following methods:
- Constructor takes `car`, `model` and `max_speed`
- All dunders you need 

## Driver
`Driver` class will have the following methods:
- Constructor takes `name`, `car` (which is a object from `Car` class) 
- All dunders you need 

## Race
`Race` class will have:
- Constructor takes `drivers`(list of `Driver`-s) and crash_chance (chance for crash for every race- number between 0 and 1)
- crash() - some of the drivers crash and take no points
- race() - returns the standing after the race. 
Every driver takes a points for his place in a ranking list. For first place - 8, second place - 6, third place - 4. You must save the result in the `rating.json`.

## Championship
`Championship` class will have:
- Constructor takes count_races 
- top_3() - returns the best 3 drivers after final race
`count_races` are number of rices, which comprises a `championship`.