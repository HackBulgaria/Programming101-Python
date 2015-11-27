# Food Diary - Extended

Now it's time to extend our previous problem - [Food Diary](../04-FoodDiary/)

## Database with calories

We are going to have a file, called `calories.json`, where we are going to have calories information for different foods.

The file is going to have the following structure:

```json
{
  "pizza": 100,
  "broccoli": 100
}
```

**We keep calories per 100g of the given food.**


## Keeping information about calories too

Now, when we add a food into our diary, we are going to provide more information:

* The amount (either in `g` or `kg`) of what we have eaten

Now, using the `calories.json` we can calculate how much calories have we taken with that food.

For example:

```
Enter command> meal pizza
How much have you eaten?> 500g
Ok, this is a total of 500 calories for this meal.
```

OR

```
Enter command> meal broccoli
How much have you eaten?> 2kg
OK, this is a total of 200000 calories for this meal.
```

### If you eat something that is not on the calories database - add it

Now, if you have eaten something that is not located in the `calories.json` database, have the program ask you for the calories of that food for 100g.

After this, update the `calories.json` database.

For example

```
$ cat calories.json
{
  "pizza": 100,
  "broccoli": 100
}
$ python3 food.py
Enter command> meal icecream
How much have you eaten?> 100g
I don't have icecream in the calories database.
How much calories per 100g?> 100
OK, this is a total of 100 calories for this meal.
Enter command>goodye
Goodbye!
$ cat calories.json
{
  "pizza": 100,
  "broccoli": 100,
  "calories": 100
}
```

## Serializing our food diary into a CSV file

Now, we are going to remove the free file structure from the previous problem and start saving our diary in a CSV file!

Figure out the columns.
