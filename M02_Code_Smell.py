uncle_sam = float(1.08)
pay_the_server = float(1.15)
food_stuff = int(input("How much was your meal?"))
corprate_cut = uncle_sam * food_stuff
pocket_book_pain = corprate_cut * pay_the_server
print("You need to leave" + str(pocket_book_pain) + "on the table to cover tax and tip.")
