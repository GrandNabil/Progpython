mot = str(input("Enter your text : "))

dic = dict()

for letter in mot:
    if letter not in dic:
        dic[letter] = 1
    else:
        dic[letter] = dic[letter] + 1

print(dic) 