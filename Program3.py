"""Program3"""

a=int(input("Enter a:"))

if a%2==0:
    a=a-1
for i in range(a):
    print(i*2+1,end="," if i<a-1 else "")
