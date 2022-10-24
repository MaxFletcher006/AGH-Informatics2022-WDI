range_from, range_to = input("Please enter the range: ").split()

index = int(range_from) 
source = 0 
inner_range = 6

for index in range(int(range_from), int(range_to)):
    print("Numbers in range: %d" % int(index))
    source = source + index

if (int(range_to) - int(range_from)) > 20:
    while (index <= int(range_to)):
        if (index == (source / int(range_to) - int(range_from)) - inner_range):
            print("Closest numbers to mean: %d" % index)
            index +=1
            inner_range -=1
    
    
    