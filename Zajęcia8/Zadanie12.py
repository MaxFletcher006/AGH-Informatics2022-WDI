tab=[]

with open('test.txt', 'r') as f:

    for line in f.readlines():

        tab.append(line.split())

print(tab)

while True:

    n = input('==> ')

    for row in tab:

        if n == row:
            print(row[0])


