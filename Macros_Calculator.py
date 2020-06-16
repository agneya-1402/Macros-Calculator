# Macros Calculator
print("------Macros Calculator------")
Cal=int(input("Enter Total Calories :"))

carb=int(input("Enter Carbohydrate % :"))
pro=int(input("Enter Protein % :"))
fat=int(input("Enter Fat % :"))

a1=carb/100
b1=pro/100
c1=fat/100

a2=Cal*a1 #so u eat ..... calories worth of carbs each day
b2=Cal*b1
c2=Cal*c1

a3=a2/4 #gms of carbs
b3=b2/4
c3=c2/9

print("Carbs :"+str(a3)+" grams")
print("Proteins :"+str(b3)+" grams")
print("Fats :"+str(c3)+" grams")