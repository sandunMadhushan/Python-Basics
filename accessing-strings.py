# Accessing Strings


# You need to make a program that counts the number of vowels in a given text.
# The vowels are a, e, i, o, and u.

# Take a string as input and output the number of vowels.

# Sample Input:
# this is great

# Sample Output:
# 4
# Hint - There are 4 vowels in the given text.

i=input()
count=0
for w in i:
    if w=="a" or w=="e" or w=="i" or w=="o" or w=="u" :
        count +=1
print(count )
