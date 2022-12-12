#Hanoi-Tower-XD-OMGSKDFDSJFDSJKFHSDJKFHDSFKHSDLFKSDHFKLSDHFKLSDAHFKLSDAFHSDKL

source = ([4, 3, 2, 1], "Source")
target = ([], "Target")
helper = ([], "Helper")

def tower(n, source, helper, target):

    if n > 0:

        tower(n - 1, source, target, helper)


        if source[0]:

            disk = source[0].pop()

            print("Move (" + str(disk) + ") from (" + source[1] + ") to " + "(" + target[1] + ")")

            target[0].append(disk)

        tower(n - 1, helper, source, target)

        print(source, helper, target)

print(source)

tower(len(source[0]), source, helper, target)

print(source, helper, target)
