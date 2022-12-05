import numpy as np 

def ascii_convert():

    str = np.loadtxt(
        'test.txt',
        dtype= 'str',
        skiprows= 1,
    )

    #ascii = np.array(str, dtype='b').tobytes().decode("ascii")

    print(str)


ascii_convert()


