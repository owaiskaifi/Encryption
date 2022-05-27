from time import time
from hashlib import sha256 
from random import choice
import argparse
import pandas as pd
 
#use like this
#for single hash
# SHA256 [hash] 

#for an input file

# SHA256 [filename.csv] -hashlist
 
def hash_password(password, hash_type):
    if hash_type.upper() == 'SHA256':
        return sha256(password.encode()).hexdigest()
   

 #check for verifyimg hash
def detect_hash(hashed_password):
    if  len(hashed_password) == 64:
        return 'SHA256'
  
    else:
        print('Could not auto detect hash type\n')
        return None

#generate random strings and compare them against hashed_password
def bruteforce(hashed_password, hash_type , bruteforce_range  , charsstr , hashlist=False):
    chars = list(charsstr)
    bruteforce_range = list(bruteforce_range)

    #check if the hash list has the correct file extension
    if hashed_password.find('.csv') == -1 and hashlist:
        hashed_password += '.csv'
    
    #get the hash list from the text file 
    hashes = []
    try:
        if hashlist:
            df=pd.read_csv('sha256_hashes.csv')  
            hashes=df['hash']
        else:
            hashes.append(hashed_password)
    except FileNotFoundError:
        print(f'{hashed_password} doesn\'t exist')
        exit()

    #set detect to true if hash type is AUTO
    detect = False
    if hash_type.upper() == 'AUTO':
        detect = True

    try:
        for h in hashes:
            
            if detect:
                hash_type = detect_hash(h)
                if hash_type == None:
                    continue
            t0 = time()
            print(f'[?] Attempting to crack: {h}')
            while True:
                #generate random string based on bruteforce range and chars
                pw = ''.join([choice(chars) for i in range(choice(bruteforce_range))])
                #print(pw)
                if h == hash_password(pw, hash_type):
                     
                    print(f'[~] password is: {pw}\n[~] password was found in: {time()-t0} seconds\n')
                    if not hashlist:
                         
                        with open('result.txt', 'w') as res:
                            res.write(pw)
                        exit()
                    else:
                        #save the password in a text file then move onto the next hash
                        with open('result.txt', 'a') as res:
                            res.write(f'{pw} = {h} \n')
                        break
        print(f'All passwords were found')

    except KeyboardInterrupt:
        t1 = time()
        print(f'[!] Password could not be found, tried for: {t1-t0} seconds')

 

if __name__ == '__main__':
 










 
    #parse arguments with argparse library
    parser = argparse.ArgumentParser()
    parser.add_argument('type', nargs=1, default=['SHA256'] ,help='hash algorithm ( SHA256 )')
    parser.add_argument('hash', nargs=1, help='hashed password (or text file contaning hashes if -hashlist is used)')
    
    parser.add_argument('-mode', nargs=1, default=['bruteforce'], help='bruteforce, list')
    parser.add_argument('-range', nargs=2, help='bruteforce password length range(use space to separate)',
    default=['3', '5'])
    parser.add_argument('-chars', nargs=1, default=['abcdefghijklmnopqrstuvwxyz0123456789!$'],
    help='string of characters to pick from when generating random strings for bruteforce')
    parser.add_argument('-hashlist', help='use list of hashes instead of single hash', action='store_true')

    arguments = parser.parse_args()

    #check if the mode is bruteforce or list (if it's neither, print an error message)
    if arguments.mode[0] == 'bruteforce':
        bruteforce(arguments.hash[0], arguments.type[0], range(int(arguments.range[0]), int(arguments.range[1])),
        arguments.chars[0], arguments.hashlist)
   
    else:
        print('Invalid mode')
     