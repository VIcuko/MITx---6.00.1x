#This code gets a number between 0 and 100 by using the bisection search.

print ("Please think of a number between 0 and 100!")
upper=100
lower=0
correct_answer=True
while (correct_answer):
    result=lower+(upper-lower)/2
    print("Is your secret number "+str(result)+"?")
    help = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (help == "h"):
        upper=result
    elif (help == "l"):
        lower=result
    elif (help == "c"):
        print ("Game over. Your secret number was:"+str(result))
        correct_answer=False
    else:
        print ("Sorry, I did not understand your input.")