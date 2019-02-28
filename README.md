# SaltyBrute

This _**Python 2.7**_ program uses the method of **Brute Force** to solve a _salted sha-1 hash_. In this program, taks two hashes and a dictonary file. Hashing the words _one-by-one_ in the file and then _comparing_ hashed words with the user's _input hash_ to solve.  

# Requirments:
  -Supports
   * Linux 
   * MacOS
   * Windows

# Tools: 
-Dictionary included in folder, if not found - link to dictonary text file from [Daniel Miessler](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt) 
* download into project folder(for ease of use). Save file as "10-million-password-list-top-1000000.txt", or name it what you want, just make sure you _change the file name in the open/read function on line: 3_. 
# Install:
### Git
* `git clone https://github.com/GWoodz/Salty_Brute.git`
### Zip
* `wget -c https://github.com/GWoodz/Salty_Brute.git \ && unzip Salty_Brute\ && rm -f Salty_Brute`


# Running Program:
Salty_Brute is ran through commanline arguments.
* Open terminal and navigate by changing directory(Linux ex: `cd`) to folder `Brute`
* type in, `python `PATH to `Salty_Brute.py` `salt hash` `password hash`
  * (ex. python /home/DarthBane/PycharmProjects/Brute/`Salty_Brute.py` f0744d60dd500c92c0d37c16174cc58d3c4bdd8e      ece4bb07f2580ed8b39aa52b7f7f918e43033ea1)
 

# Solution:
**Saled-Hash**: To solve the salted sha-1 hash, import modules from the standard libiaries `import hashlib` , `import sys` & `timeit`. Then had to open 'dictionary' file and read whats inside. Taking both hashes from the commmanline, saving inputs as variables. create variables for counters and set to zero. create variable for timer and setting to start before main function running.  Using a for loop, loop through the the dictionary breaking at new line '\n'. creating new varibale '_hash_try_'_ which hashes each word individually and digesting hash with `hexdigest()`. Then, using a `if statement` to compare _hash_try_ to user's salt hash, if found for loop through the dictonary again with a new hashed variable(`concat_pass`) that is the solved salted hash concatanted with hashed passwords in the dictionary. With the resulting hash(`guessSoSalty`), compare with user's hashed password(`sha1_pass`). If found, print result(`guessSoSalty`) with counter(`pass_count`). To Stop the timer minus new variable with `end_time` minus `start_time`. Then print time of the timer, rounded two decimal places.   
