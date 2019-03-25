"""
Write a program to do the following:
	Create to empty lists: naughty and nice
    Get the name of the child from the user:
	Get the naughty/nice status of the child
	Sort the child’s name into either the naughty or nice list
	Output the two lists
	Implement a reasonable degree of error handling
	Have the program above run on a loop that can break
	Ask the user at then end of each loop if they would like to continue
"""

naughty = []
nice = []
run = True

while run:
    name = input("What is the name of the child in question?")
    print()
    status = input("Have they been nice? (T/F)")

    if status == "T":
        status = True
    elif status == "F":
        status = False
    else:
        print("ERROR")
        break

    if status:
        nice.append(name)
    elif not status:
        naughty.append(name)
    else:
        print(status)

    print("Naughty:", naughty)
    print("Nice:", nice)

    print()
    run = bool(int(input("Run again? (1/0)")))

print("Merry Christmas")