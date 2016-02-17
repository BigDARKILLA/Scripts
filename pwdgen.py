# Generate a password with length "passlen" with no duplicate characters in the password
import random
import sys
#Every possible character 
'''s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"'''
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#If there is more than one parameter on the command line, use the second argument (after the file name) to dictate the size of the output string.
if (len(sys.argv)> 1):
	passlen = int(sys.argv[1])
else: 
	passlen = 8
	print ("Try: pwdgen.py 10 for an output string of size 10 ")
#list.join() smushes lists into strings; random.sample(s, passlen) generates a list of random elements from "s" of length "passlen"
try:
	p = "".join(random.sample(s,passlen))
	print (p)
except ValueError:
	print ("Do you really want to have to remember a password that is "+ str(passlen) + " characters long? Please try a smaller number.")

