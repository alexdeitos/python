from random import choice
dezenas = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 27, 28, 29, 30,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 56, 58, 59]
x = 0
jogo =[]
while True:
    jogo.append(choice(dezenas))
    x += 1
    if x >= 6:
        break
print(jogo)
dezenas = sorted(dezenas)
print(dezenas)