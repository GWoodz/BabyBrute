# BabyBrute

This _**Python 2.7**_ program uses the method of **Brute Force** to solve a _sha-1_ or a _salted sha-1 hash_. In this program, take a dictonary and hash the words _one-by-one_ in the file and the _compare_ hashed word(words) with the user's _input hash_ to solve.  

# Requirments:
  -supports ubuntu and windows

# Tools:
All you need to run program is to download this dictonary text --> [file](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt) into project folder(for ease of use). Save file as "10-million-password-list-top-1000000.txt", or name it what you would like just make sure you _change the file name in the open/read function on line: 3_. 

# Running Program:
Currently I built and ran program in **PyCharm**. to run, open PyCharm IDE and click on the file tab at the top right corner. Once the dropdown menu appears, click the _open file_. A window will appear and then navigate to the folder that you saved the program to. Select the **Brute.py** file and then click the ok button. Once the program loads click the the run button on the top tool bar and select run or  shift+f10. 

# Solutions:
**Non-salt**: To solve the sha-1 hash, had to import hashlib. Then had to open 'dictionary' file and read whats inside. prompt user for inputs and save inputs as variable. create variable for counter and set to zero. Using a for loop, loop through the the dictionary breaking at new line '\n'. creating new varibale 'hash_try' which hashes each word individually and digesting hash with 'hexdigest()'. Next, using a if statement to compare hash_try to user's input hash, if found print password and counter then quit. If not not found print guesses and quit. 
