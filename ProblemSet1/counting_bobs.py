'''
Write a program that prints the number of times the string 'bob' 
occurs in s. For example, if s = 'azcbobobegghakl', then your program 
should print:

"Number of times bob occurs is: 2"

'''

counter = 0
position = 0

for letter in s:
    if s[position:position+3]=="bob":
        counter+=1
    position+=1
print "Number of times bob occurs is: " + str(counter)