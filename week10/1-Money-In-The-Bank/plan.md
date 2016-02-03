


1. Validator -> return self
2. Storing passwords in plain text & hash functions
  -> https://en.wikipedia.org/wiki/Hash_function
  -> hashlib - https://docs.python.org/3.5/library/hashlib.html
  -> https://en.wikipedia.org/wiki/Security_of_cryptographic_hash_functions
3. On register -> h(password)
4. On login -> hashed_from_db == h(input_password) 
5. Rainbow tables -> https://en.wikipedia.org/wiki/Rainbow_table
6. Salts. hashed_password = h(password + random_generated_salt). Store hashed_password and random_generated_salt together
  -> hashed_password == h(input_password + random_generated_salt from db for that user)
7. https://docs.python.org/3.5/library/random.html#random.getrandbits
8. Timing for bruteforce attacks - unix timestamps.
