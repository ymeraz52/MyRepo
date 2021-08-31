num = int(input("Gove me a numbe: "))
print(num)

while True:
    try:
        num = int(input("Give me a number: "))
        break
    except:
        print("you did not enter a number: ")
        continue
    print(num)
