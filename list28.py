text = "Python programming is amazing!"
word = list(text)

print (word)

list_text = text.split()
word = ''
for i in list_text:
    word += i[0]
print(word)