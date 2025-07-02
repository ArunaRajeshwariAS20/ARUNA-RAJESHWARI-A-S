"""Program2-Series of numbers"""

a=int(input("Enter a:"))
for i in range(a):
    print(i*2+1,end="," if i<a-1 else"")
