Problems
========================

In a file, called diveintopython.py, code the solutions to the following problems:

The solutions should be written in Python 3.

1.Is Number Balanced?
----------------
A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number `1238033` is balanced, because it's left part is `123` and right part is `033`.

We have : `1 + 2 + 3 = 0 + 3 + 3 = 6`.

A number with only one digit is always balanced!

Implement a function `is_number_balanced(n)` that checks if `n` is balanced.

## Test Examples
```python
>>> is_number_balanced(9)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True
```

2.Transversal
----------------
Lets have a set of sets:

`A = ( (1, 2, 3) , (4, 5, 6), (7, 8, 9) )`

A transerval `T` for `A` is a set that contains at least one element from each set of `A`.

For example: 
`T = (1, 4, 7)`

# 2.1 Is Transversal?

Implement a function `is_transversal(transversal, family)`, which check if given set is a valid `transerval` for another `family` of sets (set of sets).

## Signature
```python
def is_transversal(transversal, family):
	pass
```

### Test Examples
```python
>>> is_transversal((4, 5, 6), ((5, 7, 9), (1, 4, 3), (2, 6))))
True
>>> is_transversal((1, 2), ((1, 5), (2, 3), (4, 7)))
False
>>> is_transversal((2, 3, 4), ((1, 7), (2, 3, 5), (4, 8)))
False
```
# 2.2 All Transversals

Implement a function `generate_transversals(family)`,which find all transversals for a given `family` of sets. For this solution use `list`.

## Signature

```python
def generate_transversals(family):
	pass
```

## Test Examples
```python
>>> generate_transversals([[1, 4, 5], [2, 7], [1, 9]])
[[1, 2, 1], [1, 2, 9], [1, 7, 1], [1, 7, 9], [4, 2, 1], [4, 2, 9], [4, 7, 1], [4, 7, 9], [5, 2, 1], [5, 2, 9], [5, 7, 1], [5, 7, 9]]
>>> generate_transversals([[7,8], [2, 3, 4]])
[[7, 2], [7, 3], [7, 4], [8, 2], [8, 3], [8, 4]]
```


3. Largest Palindrome
----------------

Implement a function get_largest_palindrome(n), which return the largest palindrome smaller than `n`. Given number `n` can also be palindrome.


### Test Examples
```python
>>> get_largest_palindrome(99)
88
>>> get_largest_palindrome(252)
242
>>> get_largest_palindrome(994687)
994499
>>> get_largest_palindrome(754649)
754457
```

5. Prime Numbers
----------------

Given an integer, implement a function, called `prime_numbers(n)`.
Use [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to find all the prime numbers less than or equal to `n`.

### Test Examples
```python
>>> prime_numbers(30)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> prime_numbers(3)
[2, 3]
```