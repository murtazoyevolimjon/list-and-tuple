number1 = 1
number2 = 12
number3 = 22
number4 = 7
to_save = 0

print (number1)
print (number2)
print (number3)
print (number4)
print ("Almashtirilgan qiymat:\n")

if number1 < number2 :
    to_save = number1
    number1 = number2
    number2 = to_save
if number3 < number4:
    to_save = number3
    number3 = number4
    number4 = to_save
  
print (number1)
print (number2)
print (number3)
print (number4)
