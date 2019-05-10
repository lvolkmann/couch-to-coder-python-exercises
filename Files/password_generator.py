"""
You've lost your password but you know the common elements you use that you saved in passwords.txt
    - Write a program to create every combination of password elements
    - Output these combinations to another file
    - NOTE: every password has three elements separated by commas name, symbol, number
"""

# open files
fh = open("passwords.txt", "r")
out = open("Output.txt", "w")

# initialize blank lists
element1 = []
element2 = []
element3 = []

# get elements
for line in fh:
    line = line.strip('\n')
    elements = line.split(sep = ',')
    element1.append(elements[0])
    element2.append(elements[1])
    element3.append(elements[2])
    
# combine elements 
for a in element1:
    for b in element2:
        for c in element3:
            #write elements
            out.write(a+b+c+"\n")
            
# close files
fh.close()
out.close()
