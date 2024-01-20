n = int(input("enter no of customers : "))
height_inches = []
height_cm = []
print("enter heights in inches")
for i in range(0,n):
    height_inches.append(int(input()))
    height_cm.append(round(height_inches[i]/2.205,2))
print(height_cm)