import math
import random

#coordinates = [(-2,-4),(4,-4),(4,4),(5,1),(6,3),(2,3),(-3,-1),(2,-1),(0,3),(0,0),(1,0),(-9,0)]
#coordinates = [(2,3),(-3,-1),(2,-1),(3,5),(6,8),(9,1),(3,1),(-9,6),(10,6),(10,-7),(-2,-4),(4,-4),(4,4)]
#coordinates = [(-9,6),(10,6),(10,-7),(9,-6),(0,3),(7,4),(-1,9),(-2,5),(7,10),(3,-4),(3,2),(1,-2),(5,-4)]

#num = int(input("Please enter the numbers of coordinates: "))
#coordinates = [[random.randint(-10, 10) for i in range(2)] for i in range(num)]

'''for i in range(num):

    x = int(input("Please enter X point: "))
    y = int(input("Please enter Y point: "))
    coordinates.append((x , y))'''

print(coordinates)

i = 0
j = 1
m = 2

while m < len(coordinates):

        P = math.sqrt(
            pow((coordinates[j][0] - coordinates[i][0]) , 2) + pow((coordinates[j][1] - coordinates[i][1]) , 2))

        Q = math.sqrt(
            pow((coordinates[m][0] - coordinates[j][0]) , 2) + pow((coordinates[m][1] - coordinates[j][1]) , 2))

        R = math.sqrt(
            pow((coordinates[i][0] - coordinates[m][0]) , 2) + pow((coordinates[i][1] - coordinates[m][1]) , 2))

        #print(P,Q,R)

        if (pow(P,2) == pow(Q,2) + pow(R,2)) or (pow(Q,2) == pow(P,2) + pow(R,2)) or (pow(R,2) == pow(P,2) + pow(Q,2)):

            if abs(coordinates[i][1]) == abs(coordinates[i][0]) or abs(coordinates[j][1]) == abs(coordinates[j][0]) or \
                    abs(coordinates[m][1]) == abs(coordinates[m][0]) or abs(coordinates[i][0] == 0) or \
                    abs(coordinates[i][1] == 0) or abs(coordinates[j][1] == 0) or abs(coordinates[j][0] == 0) or \
                    abs(coordinates[m][1] == 0) or abs(coordinates[m][0] == 0):


                    print(f'[False]: Coordinates: {coordinates[i]} ; {coordinates[j]} ; {coordinates[m]} are [Parallel]')

            else:
                print(f'[True]: Coordinates: {coordinates[i]} ; {coordinates[j]} ; {coordinates[m]} are [Right Triangle]')


        else:
            print(f'[False]: Coordinates: {coordinates[i]} ; {coordinates[j]} ; {coordinates[m]} are [Not Right Triangle]')

        i +=1
        j +=1
        m +=1










