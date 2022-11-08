def euler_function():
    n = int(input("Please input the n number: "))

    i = 1
    storage = 0
    fac = 1

    euler_numbers = [ ]
    (app_list) = [ ]

    while (i<=n):

        fac = fac * i
        storage = storage + (1 / fac)
        euler_numbers.append(storage)
        print("Result: n = [%d] ; e = [%lf]" % (i , storage))
        i += 1

    i = 0
    j = 1 

    while (j<n):
        app_elem = euler_numbers[j] - euler_numbers [i]
        app_list.append(app_elem)
        i += 1
        j += 1
    
    print("\n" + "Euler's numbers list: " + str(euler_numbers) + "\n")
    print("Approx list: " + str(app_list))

euler_function()
