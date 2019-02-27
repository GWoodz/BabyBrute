# Author: G.W
# This program Brute Force salted hashes
# Takes two commmandline arguments to run


import hashlib
import sys
import timeit


salty = sys.argv[1]                              # accepting user's hashed salt commandline argument

sha1_pass = sys.argv[2]                          # accepting user's hashed password commandline argument

salt_count = 0                                   # counter set to zero

pass_count = 0                                   # password count set to zero


# ******Open and read dictionary file, Need to implement your PATH to dictionary********
sha1_openFile = open('****YOUR PATH HERE****/10-million-password-list-top-1000000.txt').read()


start_time = timeit.default_timer()                     # sets and starts timer

for password in sha1_openFile.split('\n'):              # looping through file stopping at whitespace line

    hash_try = hashlib.sha1(password).hexdigest()       # hashing each tried word in file

    if hash_try == salty:                               # comparing hashed guesses in file to user's salted input

        print("Found salt: " + password + ", Guesses: " + str(salt_count))        # Print if salt found

        for guessSoSalty in sha1_openFile.split('\n'):                       # looping through file again

            concat_pass = hashlib.sha1(password + guessSoSalty).hexdigest()  # Hashing concatenated password & salt

            if concat_pass == sha1_pass:                            # Checking concatenated guess equals user's password

                print("\nFound: " + guessSoSalty + ", Guesses: " + str(pass_count))   # Printing results if found

                end_time = timeit.default_timer() - start_time      # Calculates function execution time

                print("Time: " + str(round(end_time, 2)) + "s")  # Prints execution time in seconds, rounds two decimals

                quit()                                              # Exit execution

            elif concat_pass != sha1_pass:                          # If new combined hash equal to password hash

                print("we tried: " + guessSoSalty)                  # Print tried guesses

                pass_count += 1                                     # Adds 1 to counter for every missed guess

    elif hash_try != salty:                     # if salted term not found

        print("We tried: " + password)          # print used guesses

        salt_count += 1                              # Count used guesses

print("Cannot Find it, Total Guesses: " + str(salt_count))       # print if nothing is found


