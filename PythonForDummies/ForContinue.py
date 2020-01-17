LetterNum = 1
for Letter in "Howdy!":
    if Letter == "w":
        continue
        print("Encountered w, not processed.")

    print("Letter {} is {}".format(LetterNum,Letter))
    LetterNum +=1

