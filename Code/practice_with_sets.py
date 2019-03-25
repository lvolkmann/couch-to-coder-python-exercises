def analyze(x,y):
    x_set = set(x)
    y_set = set(y)

    choice = 0
    while choice != 5:

        display(x_set, y_set)
        
        choice = choose()

        if choice == 1:
            print(x_set & y_set)
        if choice == 2:
            print(x_set | y_set)
        if choice == 3:
            print(x_set - y_set)
        if choice == 4:
            print(y_set-x_set)


def display(x_set, y_set):
    
    print("1) In common:", len(x_set & y_set))
    print("2) Together:", len(x_set | y_set))
    print("3) Unique to first container:", len(x_set - y_set))
    print("4) Unique to second container:", len(y_set-x_set))
    print("5) QUIT")

def choose():

    while True:
        try:
            choice =  int(input("Choose the set you would like to see or quit"))
            if choice not in range(1,6):
                raise ValueError(choice)
            return choice
        except ValueError as ex:
            print("Bad input:", ex)

x = [1, 2, 3, 4, 5, 6]
y = [1, 3, 5, 7]
analyze(x,y)
