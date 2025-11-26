# runs top to bottom, once and close, no access to variables without add ons

l = [1, 2, 3]

u = input("give us a number, please")

if u.isnumeric():
    print("thank you for the number")
else:
    print("Hey why did you not give us a number?")


from human import Human

print(Human)  # just to show can reuse code
