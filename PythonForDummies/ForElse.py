"""
Value = input("Type something of 6 characters:")
LetterNum=1
Counter = 0

for Letter in Value:
    print("Letter {} is {}".format(LetterNum,Letter))
    LetterNum +=1
    Counter +=1
else:
    print("The String is blank!")

print("The String that you typed have {} characters!".format(Counter))
"""
#################################### Another Example ######################################


X = 1
Y = 1

print('{:>8}'.format(' '), end=' ')

for X in range(1,11):
    print('{:>8}'.format(X),end=' ')

print()

for X in range(1,11):
    print('{:>8}'.format(X),end=' ')
    while Y <= 10:
        print('{:>8}'.format(X*Y),end=' ')
        Y += 1
    print()
    Y=1


