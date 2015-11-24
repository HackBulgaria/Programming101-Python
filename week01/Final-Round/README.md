# Some serious problems reside here!

## Count words

Given a list of strings, implement a function, called `count_words(arr)` which returns a dictionary of the following kind:

```python
{ "word" : count }
```

Where `count` is the count of occurrences of the __word__ in the list `arr`.


### Signature

```python
def count_words(arr):
    pass
```

### Test examples

```python
>>> count_words(["apple", "banana", "apple", "pie"])
{'apple': 2, 'pie': 1, 'banana': 1}
>>> count_words(["python", "python", "python", "ruby"])
{'ruby': 1, 'python': 3}
```

## NaN Expand

In most programming languages, `NaN` stands for `Not a Number`.

If we take a look at the following JavaScript code:

```javascript
typeof NaN === 'number' // true
```

We will see that in JavaScript, `NaN` stands for `Not a NaN`, which is recursive by nature.

Implement a Python function, called `nan_expand(times)`, which returns the expansion of `NaN` (In JavaScript terms :P) that many `times`.

For example:

* If we expand `NaN` once (`times=1`), we will have `"Not a NaN"`
* If we expand `NaN` twice (`times=2`), we will have `"Not a Not a NaN"`
* If `times=3`, we have `"Not a Not a Not a NaN"`
* And so on ...

### Examples

```python
>>> nan_expand(0)
""
>>> nan_expand(1)
"Not a NaN"
>>> nan_expand(2)
"Not a Not a NaN"
>>> nan_expand(3)
"Not a Not a Not a NaN"
```

## Iterations of NaN Expand

Implement a function, called `iterations_of_nan_expand(expanded)` that takes a string `expanded`,
which is an unkown iteration of NaN Expand (check the problem for more information)

The function should return the number of iterations that have been made, in order to get to `expanded`.

For example, if we have `"Not a Not a Not a NaN"` - this is the 3rd iteration of `NaN`.

**If `expanded` is not a valid NaN expand string, the function should return false! (This is the hard part)**

### Examples

```python
>>> iterations_of_nan_expand("")
0
>>> iterations_of_nan_expand("Not a NaN")
1
>>> iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
10
>>> iterations_of_nan_expand("Show these people!")
False
```

## The group function

We are going to implement a very helpful function, called `group`.

`group` takes a list of things and returns a list of group, where each group is formed by all **equal consecutive elements** in the list.


For example:

```python
group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]
group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]]
```

## Longest subsequence of equal consecutive elements

Implement the function `max_consecutive(items)`, which takes a list of things and returns an integer - the count of elements in the longest subsequence of equal consecutive elements.

For example, in the list `[1, 2, 3, 3, 3, 3, 4, 3, 3]`, the result is 4, where the longest subsequence is formed by `3, 3, 3, 3`

### Signature

```python
def max_consecutive(items):
    pass
```

#### Test examples

```python
>>> max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])
4
>>> max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
3
```

## Gas Stations

We are implementing a smart GPS software.

- We are taking a long trip from Sofia to Plovdiv and we know the distance between the two cities.It is a positive integer and we mark it as ``distance``.

- We know how much our car can ride with a full tank of gas. It is a positive integer in kilometers. We mark it as ``tank_size``.

- We have a list of gas stations. We know the distance between Sofia and the current gas station. ``stations = [50, 80, 110, 180, 220, 290]`` The list is sorted!

By using this information we will implement a function that returns the shortest `list` of gas stations that we have to visit in order to travel from Sofia to Plovdiv. Know that are allways starting with a full tank_size.

### Signature
```python
def gas_stations(distance, tank_size, stations):
	pass
```

#### Test Example
```python
>>> gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
[80, 140, 220, 290]
>>> gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
[70, 140, 210, 280, 350]
```

## Sum all numbers in a given string

You are given a string, where there can be numbers. Return the sum of all numbers in that string (not digits, numbers)

Examples:

```
sum_of_numbers("1111") = 1111
sum_of_numbers("1abc33xyz22") = 1 + 33 + 22 = 56
sum_of_numbers("abcd") = 0
```
### Signature
```python
def sum_of_numbers(st):
    pass
```

#### Test Examples
```python
>>> sum_of_numbers("ab125cd3")
128
>>> sum_of_numbers("ab12")
12
>>> sum_of_numbers("ab")
0
```

## 100 SMS

Before the smartphones, when you had to write some message, the keypads looked like that:

![Nokia 3310 Keypad](nokia.jpg)

For example, on such keypad, if you want to write **Ruby**, you had to press the following sequence of numbers:

```
7778822999
```

Each key contains some letters from the alphabet. And by pressing that key, you rotate the letters until you get to your desired one.

It's time to implement some encode / decode functions for the old keypads!

### `numbers_to_messege(pressed_sequence)`

First, implement the function that takes a list of integers - the sequence of numbers that have been pressed. The function should return the corresponding string of the message. 

There are a few special rules:

* If you press `1`, the next letter is going to be capitalized
* If you press `0`, this will insert a single white-space
* If you press a number and wait for a few seconds, the special breaking number `-1` enters the sequence. This is the way to write different letters from only one keypad!

Few examples:

```
numbers_to_messege([2, -1, 2, 2, -1, 2, 2, 2]) = "abc"
numbers_to_message([2, 2, 2, 2]) = "a"
numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
=
"Ivo e Panda"
```

### `message_to_numbers(messsage)`

This function takes a string - the `message` and returns the **minimal** keystrokes that you ned to write that `message`

Few examples:

```
message_to_numbers("abc") = [2, -1, 2, 2, -1, 2, 2, 2]
message_to_numbers("a") = [2]
message_to_numbers("Ivo e panda")
=
[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
messageToNumbers("aabbcc") = [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
```
