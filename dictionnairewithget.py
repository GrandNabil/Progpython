mot = str(input("Enter your text : "))

dic = dict()

for letter in mot:
    dic[letter] = dic.get(letter, 0) + 1

print(dic) 