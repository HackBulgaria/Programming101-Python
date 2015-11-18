Data Structures 
========================

Here are the basic data structures, which will help you to solve our problems. Test them in the **REPL**.

List
----------------
It does not work like a traditional array. It is **heterogeneous**! This means it can store elements with different types in one list. 


```python
>>>things = [1 , 2, 'Ivo', [8, 'Rado']]
```

We can iterate:

```python
>>>for thing in things:
...    print(thing)
... 
1
2
Ivo
[8, 'Rado']
```

For more information: https://docs.python.org/3.4/tutorial/datastructures.html#more-on-lists.

Dictionaries
----------------
**Are hash tables, also known as associative arrays!**

```python
youtube_views = {
    'Gangnam Style': 2096709806,
    'Baby': 1091538504,
    'Waka Waka': 746709408,
}

print(youtube_views['Waka Waka']) # 746709408
```

Values are added by assigning them to `keys`.

```python
youtube_views['Wrecking Ball'] = 709604432
```

If that `key` already exists, the value held by that key will be replaced.
```python
youtube_views['Wrecking Ball'] = 85

print(youtube_views) # { 'Wrecking Ball': 859604432 , 'Gangnam Style': 2096709806, 'Waka Waka': 746709408, 'Baby': 1091538504}

```

Set
----------------
A set is an unordered collection with no duplicate elements.

Basic usage includes membership testing and eliminating duplicate entries.

Set objects also support mathematical operations like `union`, `intersection`, `difference`, and `symmetric difference`.

```python
>>> sports = set()
>>> sports.add('volleyball')
>>> sports.add('football')
>>> sports.add('basketball')
>>> 'volleyball' in sports
True
>>> 'tenis' in sports
False
```
Sets are perfect for searching elements with `in` since they can find them in `O(lgN)` time, in comparison to `O(n)` for `lists`.
For more information https://docs.python.org/3.4/tutorial/datastructures.html#sets.


List Comprehension
----------------
We use them when we want to create a new list. This way is more optimal and readable.

For example, if we have the following cycle:
```python
>>> numbers = []
>>> for x in range(4, 10):
...	numbers.append(x)
...
>>> numbers 
[4, 5, 6, 7, 8, 9]
```

The same as the following:
```python
>>> numbers = [x for x in range(4, 10)]
>>> numbers
[4, 5, 6, 7, 8, 9]
```

We can also make different operations with the element, we append in list.
Example:
```python
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
