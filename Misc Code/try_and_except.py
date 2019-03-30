def divider():
    try:
        x = int(input("First Number"))
        y = int(input("Second Number"))

        if y == 7:
            raise TypeError("7 isn't even a real number")

        return x/y

    except ValueError:
        print("Must input a number")

    except ZeroDivisionError:
        print("Can't divide by zero")
        
    except TypeError as baddy:
        print (baddy)
    except:
        print("Something Went Wrong")
        
    
