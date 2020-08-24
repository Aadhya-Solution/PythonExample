n=input("Enter N:")
flag="Green"
for i in range(2,n):
    if n%i==0:
        flag="Red"

if flag=="Green":
    print("Given Num Prime")
elif flag == "Red":
    print("Given Num not prime")
    print("Numbver is not ")