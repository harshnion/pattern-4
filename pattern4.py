## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
inc=(n+1)//2
dec=n-inc
i=1
while i<=inc:
    q=1
    while q<=i-1:
        print(" ",end="")
        q=q+1

    j=1
    while j<=i:
        print("* ",end="")
        j=j+1
    print()
    i=i+1
i=1
while i<=dec:
    q=1
    while q<= dec-i:
        print(" ",end="")
        q=q+1


    j=1
    while j<=dec-i+1:
        print("* ",end="")
        j=j+1
    print()
    i=i+1
