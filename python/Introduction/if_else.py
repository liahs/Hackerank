n = int(input().strip())
if ((n%2)!=0):
    print('Weird')
elif(n%2==0):
    if(2<=n<=5):
        print('Not Weird')
    if(6<=n<=20):
        print('Weird')
    if(n>20):
        print('Not Weird')
