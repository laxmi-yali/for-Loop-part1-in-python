# for loop
for i in range(1,11):
  print(i,end = "  ")
  
#
  
bag = ["red","green","blue"]
for ball in bag:
    print(ball)
    
# using step
for i in range(2,11,2):
    print(i,end="  ")
    
# Looping over string
# example: Printing over Strings

name = "Laxmi"
for letter in name:
    print(letter*3)
    
# 
name = "chandan"
for index, letter in enumerate(name):
    print(letter*(index+1))

#
l = [12,1354,14,1244]
for index, num in enumerate(l):
    print(f"{num} is in {index}th index")
    

for num in l:
    print(num)
else:
    print("all printed")
    
# using break in a for Loop
# example : stop the loop when you find a specific item   

cities = ["Bengalure","mysure","hasan","hubli"]
for city in cities:
    if city == "gadag":
        print(f"Found {city}")
        break
    print(city)
    
# example : Skip specific item in list

cities = ["Bengalure","mysure","hasan","hubli"]
for city in cities:
    if city == "hasan":
        continue
    print(city)
    
# using else with for Loop
for city in cities:
    print(city)
else :
    print("no more cities")

