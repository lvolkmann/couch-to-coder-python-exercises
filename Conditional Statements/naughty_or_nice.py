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

