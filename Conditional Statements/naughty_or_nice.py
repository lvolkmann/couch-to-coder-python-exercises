"""
Write a program to do the following:
	Create to empty lists: naughty and nice
    Get the name of the child from the user:
	Get the naughty/nice status of the child
	Sort the child’s name into either the naughty or nice list
	Output the two lists
	Implement a reasonable degree of error handling

STRETCH GOAL:
	Have the program above run on a loop that can break
	Ask the user at then end of each loop if they would like to continue
"""

naughty = []
nice = []
run = True

while run:

    # Get user input
    name = input("What is the name of the child in question?")
    print()
    status = input("Have they been nice? (T/F)")

    # Check and save child status
    if status == "T":
        status = True
    elif status == "F":
        status = False
    else:
        print("ERROR")
        break

    # Add student name based on status
    if status:
        nice.append(name)
    elif not status:
        naughty.append(name)
    else:
        print(status)

    # Print results
    print("Naughty:", naughty)
    print("Nice:", nice)

    print()

    # Break or continue loop
    run = bool(int(input("Run again? (1/0)")))

print("Merry Christmas")