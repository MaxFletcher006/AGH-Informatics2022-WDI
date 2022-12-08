ascii_list = []

with open('test.txt', 'r') as f:

    for line in f.readlines():

        ascii_list.append(line.split())

while True:

    char = input('==> ')

    for row in ascii_list:

        if char in row:
            print(row[0])
