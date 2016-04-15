'''
Write a program that counts up the number of vowels contained in the 
string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if 
s = 'azcbobobegghakl', your program should print:

"Number of vowels: 5"

'''

counter = 0
for letter in s:
    if letter.lower() in "aeiou":
        counter+=1

print "Number of vowels: "+ str(counter)