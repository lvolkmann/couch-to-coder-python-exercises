while True:
	try:
		file_name = input("Please enter the name of the file you would like to read")
		fh = open(file_name)
		break
	except:
		print("Couldn't open file. Please try again")

while True:
	try:
		line_cnt = int(input("How many lines would you like to read?"))
		if(line_cnt <= 0):
			raise ValueError
		if(line_cnt >1000):
			raise OverflowError
		break
	except ValueError:
		print("Must enter an integer greater than 0")
	except OverflowError:
		print("Nobody's got time for that.")
	except:
		print("Strange input. Muste enter a legit int")

try:
	for line in range(1, line_count+1):
		print(fh.readline())
except EOFError:
	print("Ya hit the end of the file at line:",line)
except:
	print("Something went terribly wrong at line:",line)
finally:
	fh.close()
