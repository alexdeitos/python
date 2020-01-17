LetterNum=1

for Letter in "Howdy!":
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum +=1

LetterNum = 0
print("\n")
for Letter in "Alexsandro Oliveira Deitos":
    if(Letter.isspace()):
        print("")
        LetterNum += 1;
    else:
        print("Letra ", LetterNum, " is ", Letter)
        LetterNum +=1;
print("GoodBye!")