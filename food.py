my_list = []
print(input("What is your favorite food? "))
my_list.append(input)

while True:
    question = (input("Add another:\y|n: "))
    if question == "y":
        my_list.append(input("Give me another food "))
        continue
    elif question == "n":
        break
    else:
        print("You did not give a food item!")
for i in my_list:
    print(my_list)
    print(" all of your food items!!!!")

#for i in my_list
#   print(i, end=" ")
#
#print("are all my fovorite food")


