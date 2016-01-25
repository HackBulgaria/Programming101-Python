# Cinema Reservation System
We are going to cinema! But the reservation systems are down and the cinema officials don't let people without reservations. So we offered to make them a new reservation system that will allow us to go and watch the newest **"Aliens came, we built transformers and destroyed them..."** movie.

## Problem 0 - The database
No complex stuff here. Just a few simple tables:

**Movies**

| id | name | rating |
| ------------- |:-------------| :---: |
|1|The Hunger Games: Catching Fire |7.9|
|2|Wreck-It Ralph|7.8|
|3|Her|8.3|

**Projections**

| id | movie_id | type | date | time |
| ---|----------|:----:| :--: | :--: |
|1|1|3D|2014-04-01|19:10
|2|1|2D|2014-04-01|19:00
|3|1|4DX|2014-04-02|21:00
|4|3|2D|2014-04-05|20:20
|5|2|3D|2014-04-02|22:00
|6|2|2D|2014-04-02|19:30

**Reservations**

| id | username | projection_id | row | col |
| ---|----------|---------------|:----:|:---:|
|1|RadoRado|1|2|1|
|2|RadoRado|1|3|5|
|3|RadoRado|1|7|8|
|4|Ivo|3|1|1|
|5|Ivo|3|1|2|
|6|Mysterious|5|2|3|
|7|Mysterious|5|2|4|

**Things to note**
* For each projection we assume the hall will be a 10x10 matrix.
* All data presented here is just an example. If you want, you can make up your own (perhaps you are the creator of the aforementioned movie and want to include it).

## Problem 1 - The CLI (Command-Line Interface)
We don't need no GUIs! A console with green text and transparent background is all a hacker requires.
Implement a python script called ```magic_reservation_system.py``` that takes magic commands and casts an appropriate spell. Here's an ancient page of Merlin's Book:
* On spell ```show_movies``` - print all movies ORDERed BY rating
* On spell ```show_movie_projections <movie_id> [<date>]``` - print all projections of a given movie for the given date (date is optional).
  1. ORDER the results BY date
  2. For each projection, show the total number of spots available.

* On spell ```make_reservation``` - It's showtime!
  1. Make the hacker choose a name and number of tickets
  2. Cast ```show_movies``` and make the hacker choose a movie by id
  3. Cast ```show_movie_projections``` for the chosen ```<movie_id>``` and make the hacker choose a projection
    * *If the available spots for a projection are less than the number of tickets needed, print an appropriate message and stay at step 3*;
  4. Cast a spell to show all available spots for the chosen projection
  5. For each number of tickets, make the hacker choose a tuple ```(row, col)```. Check for tuple validity (10x10 matrix) and availability (reservations table)
  6. Cast a spell to show the info in an appropriate format. Then prompt for ```finalize``` spell
  7. On ```finalize``` spell, save all the info and wish a happy cinema!
  0. **At each step, allow for ```give_up``` spell to be cast. This...wait for it...waaaiit... gives up the reservation!!!** (Thanks, cap'n)

* On spell ```cancel_reservation <name>``` - disintegrate given person's reservation (**NOTE**: reservations cannot be so easily removed, but this is a magical system, after all)
* On spell ```exit``` - close Pandora's Box before it's too late.
* On spell ```help``` - show a list of learned spells


**Things to note**
* Notice how you are required to reuse code (or you'll be one messy hacker!!!).
* Try not to build everything in one place.
* Make use of the following techniques (Merlin used them to destroy the Decepticons): **OOP, TDD, SQL**.



## Examples

### Show movies

```
> show_movies
Current movies:
[1] - The Hunger Games: Catching Fire (7.9)
[2] - Wreck-It Ralph (7.8)
[3] - Her (8.3)
```

### Show movie projections ###

```
> show_movie_projections 2
Projections for movie 'Wreck-It Ralph':
[5] - 2014-04-02 19:30 (2D)
[6] - 2014-04-02 22:00 (3D)
> show_movie_projections 1 2014-04-01
Projections for movie 'The Hunger Games: Catching Fire' on date 2014-04-01:
[1] - 19:00 (3D)
[2] - 19:10 (2D)
```


### Make a reservation

```
> make_reservation
Step 1 (User): Choose name>Tedi
Step 1 (User): Choose number of tickets> 2
Current movies:
[1] - The Hunger Games: Catching Fire (7.9)
[2] - Wreck-It Ralph (7.8)
[3] - Her (8.3)
Step 2 (Movie): Choose a movie> 2
Projections for movie 'Wreck-It Ralph':
[5] - 2014-04-02 19:30 (2D) - 98 spots available
[6] - 2014-04-02 22:00 (3D) - 100 spots availabe
Step 3 (Projection): Choose a projection> 5
Available seats (marked with a dot):
   1 2 3 4 5 6 7 8 9 10
1  . . . . . . . . . .
2  . . X X . . . . . .
3  . . . . . . . . . .
4  . . . . . . . . . .
5  . . . . . . . . . .
6  . . . . . . . . . .
7  . . . . . . . . . .
8  . . . . . . . . . .
9  . . . . . . . . . .
10 . . . . . . . . . .
Step 4 (Seats): Choose seat 1> (2,3)
This seat is already taken!
Step 4 (Seats): Choose seat 1> (15, 16)
Lol...NO!
Step 4 (Seats): Choose seat 1> (7,8)
Step 4 (Seats): Choose seat 2> (7,7)
This is your reservation:
Movie: Wreck-It Ralph (7.8)
Date and Time: 2014-04-02 19:30 (2D)
Seats: (7,7), (7.8)
Step 5 (Confirm - type 'finalize') > finalize
Thanks.
```

# DISCLAIMER
The purpose of these tasks is to train your casting (programming) skills.
The purpose of these tasks is NOT to abide by the rules (we = hackers).
If you decide that something is not structured/explained/invented enough, feel free to discuss it with us!
Happy hacking!
