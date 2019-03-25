file_name = input("Enter file name")
try:
    if 'classified' in file_name:
        raise ValueError(file_name)
    f = open(file_name)
except ValueError as ex:
    print(ex, "is classified")
except FileNotFoundError:
    print("File not in given directory")
except:
    print("Something went wrong")

