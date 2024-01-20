n = int(input("enter no of customers : "))
height_inches = []
print("enter heights in inches")
for i in range(0,n):
    height_inches.append(int(input()))
height_cm = [round(x/2.205,2) for x in height_inches]
print(height_cm)