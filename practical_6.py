file=open("practical-6.txt",'w')
factorial=1
number=int(input("number:"))
for i in range(1,number+1):
    factorial=factorial*i
file.write(f"factorial of {number} is: {factorial}")