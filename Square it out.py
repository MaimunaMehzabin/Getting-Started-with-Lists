def digit(begin, finish):
    
    for i in range(begin, finish + 1):
        
        x = i*i
        
        if x % 2 == 0:
            print(f"Number: {i}, its Square: {x}, which is an Even Number")
        else:
            print(f"Number: {i}, its Square: {x}, which is an Odd Number")
            
            
begin = int(input("Provide the beginning position: "))
finish = int(input("Provide the finishing position: "))

digit(begin, finish)