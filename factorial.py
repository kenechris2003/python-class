while True:        
    try:
        n = int(input("Enter a number: "))
        factorial = n
        
        for i in range(1,n):
            f = (n-i)
            factorial = factorial * f
            
        print(factorial)
        break
    except:
        print("invalid input")
    
    
