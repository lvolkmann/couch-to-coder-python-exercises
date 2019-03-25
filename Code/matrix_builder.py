def build(x,y,n):
    matrix = []
    for cnt in range(0,x):
        row = []
        for cnt in range(0,y):
            row.append(n)
        matrix.append(row)
    return matrix
    
