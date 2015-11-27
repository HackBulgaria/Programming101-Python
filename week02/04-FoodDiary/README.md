FoodDiary
========

The problem where you write what you are eating write now. That program would be really helpful if you are a fat panda and you are trying to track your meals.

Write a program that have two options:
- Ask "what are you eating now?" and save the given information.
- List all the meals that you took for a given date.

Write all that information in file in such a format that you could read it later.


```
$ python3 food.py
```

```
Hello and Welcome!
Choose an option.
1. meal - to write what are you eating now.
2. list <dd.mm.yyyy> - lists all the meals that you ate that day,

Enter command>

```

## meal

meal - food you are eating write now

That option saves in to file the meal and the date write now.


```
$ python3 food.py
```

```
Hello and Welcome!
Choose an option.
1. meal - to write what are you eating now.
2. list <dd.mm.yyyy> - lists all the meals that you ate that day,

Enter command> meal pizza
Ok it is saved
Enter command> meal pasta
Ok it is saved
```

## list

That option list all the meals that you took in a current day.

### Example:

```
Hello and Welcome!
Choose an option.
1. meal - to write what are you eating now.
2. list <dd.mm.yyyy> - lists all the meals that you ate that day,

Enter command> list 25.11.2015
pizza
pasta
```

Google "how to get current date in python"

Good luck!
