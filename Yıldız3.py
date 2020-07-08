number = int(input("Number:"))
for row in range(1,number+1):
    for col in range(row,number+1):
        print("*",end=" ")
    print(" ")