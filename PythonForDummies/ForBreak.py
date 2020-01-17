value = input("Type something that has maximum of 6 letters:")
LetterNum = 0
for Letter in value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum +=1
    if (LetterNum > 6):
        print("The string is to long")
        break

print("\n Im out!")

