import math

class rightTriangle:

    def __init__(self):
        self.P = None
        self.R = None
        self.Q = None

    def creatingLines(self, coordinates):

        i = 0
        j = 1
        m = 2

        while m < len(coordinates):

            self.P = math.sqrt(
                pow((coordinates[j][0] - coordinates[i][0]) , 2) + pow((coordinates[j][1] - coordinates[i][1]) , 2))

            self.Q = math.sqrt(
                pow((coordinates[m][0] - coordinates[j][0]) , 2) + pow((coordinates[m][1] - coordinates[j][1]) , 2))

            self.R = math.sqrt(
                pow((coordinates[i][0] - coordinates[m][0]) , 2) + pow((coordinates[i][1] - coordinates[m][1]) , 2))

            print(f'P = {self.P}')
            print(f'Q = {self.Q}')
            print(f'R = {self.R}')

            i += 1
            j += 1
            m += 1

    def checkingLines(self, coordinates):

        value = False

        i = 0
        j = 1
        m = 2

        while m < len(coordinates):

            if (pow(self.P , 2) == pow(self.Q , 2) + pow(self.R , 2)) or \
                    (pow(self.Q , 2) == pow(self.P , 2) + pow(self.R , 2)) or \
                    (pow(self.R , 2) == pow(self.P , 2) + pow(self.Q , 2)):

                if abs(coordinates[i][1]) == abs(coordinates[i][0]) or abs(coordinates[j][1]) == abs(coordinates[j][0]) or \
                        abs(coordinates[m][1]) == abs(coordinates[m][0]) or abs(coordinates[i][0] == 0) or \
                        abs(coordinates[i][1] == 0) or abs(coordinates[j][1] == 0) or abs(coordinates[j][0] == 0) or \
                        abs(coordinates[m][1] == 0) or abs(coordinates[m][0] == 0):

                        print(f'[False]: Coordinates: {coordinates[i]} ; {coordinates[j]} ; {coordinates[m]} are [Parallel]')
                        value = False

                else:
                    print(f'[True]: Coordinates: {coordinates[i]} ; {coordinates[j]} ; {coordinates[m]} are [Right Triangle]')
                    value = True

            else:
                print(f'[False]: Coordinates: {coordinates[i]} ; {coordinates[j]} ; {coordinates[m]} are [Not Right Triangle]')
                value = False

            i +=1
            j +=1
            m +=1

            if value:
                print("SUCCESSED")
            if not value:
                print("FAILED")


#coordinates = [(2,3),(-3,-1),(2,-1)]
#coordinates = [(2,3),(-3,-1),(2,-1),(3,5),(6,8),(9,1),(3,1),(-9,6),(10,6),(10,-7),(-2,-4),(4,-4),(4,4)]
coordinates = [(-2,-4),(4,-4),(4,4)]
#coordinates = [(-9,6),(10,6),(10,-7),(9,-6),(0,3),(7,4),(-1,9),(-2,5),(7,10),(3,-4),(3,2),(1,-2),(5,-4)]

s = rightTriangle()
s.creatingLines(coordinates)
s.checkingLines(coordinates)





