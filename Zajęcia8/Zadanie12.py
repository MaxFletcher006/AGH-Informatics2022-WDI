tab=[]

with open('test.txt', 'r') as f:

    for line in f.readlines():

        tab.append(line.split())

print(tab)

for i in tab:
        print(i)
        print("\n")


        while True:

            n = input('> ')

            for row in tab:

                if n in row:
                    print(row[0])


