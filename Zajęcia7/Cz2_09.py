def semi_prime_number():

    n = int(input("Please enter your range: "))
    j = 1 
    prime_list = []
    semi_prime_list_1 = []
    semi_prime_list_2 = []

#-----------------------------#
#-1-Generating-Primes---------#

    while (j<=n):
        i = 1
        count = 0 
    
        while (i<=j):
        
            if(j%i==0):
                count+=1
                i +=1
            else:
                i +=1
        
        if count==2:
            prime_list.append(j)
        
        j +=1
        
#-----------------------------#
#-2-Generating-Semi-Primes-1--#

#    i = 0
#    j = 1
    
    length_prime = len(prime_list)

#    while (j<length_prime):
#        semi_prime = prime_list[j] * prime_list[i]
#        semi_prime_list_1.append(semi_prime)
#        i += 1
#        j += 1

    semi_prime_list_1=[prime_list[i]*prime_list[j] for i in range(0,length_prime) for j in range(1,length_prime)] 

#-----------------------------#
#-3-Generating-Semi-Primes-2--#

    i = 0
    
#    while (i<length_prime):
#        semi_prime = prime_list[i] * prime_list[i]
#        semi_prime_list_2.append(semi_prime)
#        i += 1
 
    semi_prime_list_2=[prime_list[x]*prime_list[x] for x in range(length_prime)] 
    
    print("Prime numbers list: " , prime_list)
    print("First list of semi primes: " , semi_prime_list_1)
    print("Second list of semi primes: " , semi_prime_list_2)

semi_prime_number()
