fruits = ["apple","peach","Pear" ]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    
print(fruits)

################### range(a,b)

#for number in range(1, 10):
#    print(number) # not 10 -- [1,10)
    
#for number in range(1, 11):
#    print(number)# with 10


#for number in range(1, 11, 3):#step
#    print(number)
    
total = 0
for number in range(1, 101):
    total += number
print(total)