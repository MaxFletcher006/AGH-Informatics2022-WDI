n = int(input("Enter the height of three: "))
for i in range(n):
    for j in range(n-i):
        print(' ', end='')
    print('\b', end='') 
    for k in range(i+n-j):
        print('*', end='')
    print('')