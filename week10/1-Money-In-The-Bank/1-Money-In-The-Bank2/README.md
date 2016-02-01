# Money In The Bank

## 0. Setup the project

Your first task is to set up the project! You can find the code within that folder.

Then run the program from `start.py`. 

__Try to run the tests.__ If everything is OK you are ready to continue.

## 1. Refactor it

We have provided you a "piece of shit" code. Yep. Blame us all you want. But you need to provide some refactoring and make it look cleaner.

**You have tests. Use them for easier refactoring!**

## 2. SQL injection

Take a look at the code. You may recognize that is not secure at all. Your second task is to protect your that program from SQL injections using prepared statements.

You can try to login and give the following username:

```
' OR 1 = 1 --
```

and give anything for the password. You will login successfuly!

__Make some unit tests to proof your security.__


## 3. Strong passwords

In this program you can register people and there are no any requirements for the password.

To increase the level of security of your clients, they all must have a STRONG password. By strong we mean:

* More then 8 symbols
* Must have capital letters, and numbers and a special symbol
* Username is not in the password (as a substring)

Implement that requirements in the register and change password function and test them.

## 4. Hash them passwords!

__All the passwords of your users are in plain text.__

You know that this is not good for security reasons. You have to store the passwords in a hash. Use the `SHA1` hashing algorithm. Make some research on that topic.

Write some tests to proof your work.

You would find this useful -> http://www.pythoncentral.io/hashing-strings-with-python/

## 5. Hide passwords while typing

As a UI (User Interface)  of your application you are using the console.

If you are typing your password in a web form, it appears as `***`. Sadly, this is not the case in our console.

[__Make some research and fix that problem.__](https://docs.python.org/3.4/library/getpass.html#getpass.getpass)

No, you can not test that at all. :D

## 6. Bruteforce protection

You can catch if a user tries to login too many times within a minute. If he tries 10 or 20 times, it can be a signal for a brute-force attack! You have to protect the bank software from that.

__If someone enters 5 wrong passwords in a row, block him from trying for the next 5 minutes.__

This should work even if the user exits the bank software and tries to login again.

It is a good idea to use the help of the database, to achieve that!
__As always, don't forget the tests.__

## 7. Reset password email

Your customers need a reset password function!

__Add an email field in the client module and in the database.__
Your command must look like this:

```
send-reset-password Ivaylo
```

It sends an email to the user, with a unique random hash code.

```
reset-password Ivaylo
```

That will ask you for the hash code, that was send to the user. If you know the hash it will led you to change your passwords. That proofs that you are the owner of that email.

Try sending emails by using a gmail SMTP. GOOGLE IT!

## 8. Transactions in the bank

Since this is a bank, every user should be able to make transactions to his bank account.

For now, every user will have only 1 bank account.

All users must be able to perform the following actions:

* Deposit money in the bank account
* Withdraw money from the bank account
* Diplay the current balance from the bank accont

The restrictions are as follow:

* One cannot withdraw more money than the current balance

Implement the following commands for every bank account. Those commands should work only if the user has been logged in to the system.

Remember, TDD is your friend!


## 9. More secure transactions - TAN

TAN (Transaction Authenticanon Number) is a extra layer of security.

Now, for every transaction we want to make, we have to provide this extra piece of authentication - a 32 characters long code, that is unique for the user and the system!

For example:

```
$$$>login
Enter your username: rado
Enter your password:
Welcome you are logged in as: rado
Logged>>deposit
Enter amount: 1 000 000
Enter TAN code: 8490c2c992d10003370509e7a008f659c8220b6db62e591449106d04a45174cc
Transaction successful!
1 000 000 were deposited to the bank
```

Here are the details for the TAN codes:

* TAN codes are required only for depositing and withdrawing transactions
* __Every code can only be used once.__ After this, the code becomes inactive and cannot be given to complete a transactions
* Once registered, a bank user starts without TAN codes - he have to ask for them

Implement a command, called ```get-tan``` that does the following thing:

* Can only be used for a logged-in user
* Asks for the user password again
* Emails the user a list of 10 unique TAN codes, that he can use for his next 10 transactions
* If the command is called again, it says : `You have 10 remaining TAN codes to use` where 10 can be any number between 1 and 10
* If there are 0 TAN codes remaining, generate 10 new for that user and email them to him!
