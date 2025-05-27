n = int(input("Enter an integer: "))  
fact = 1  
i = n  

while i > 0:  
    fact = fact * i  
    i = i - 1  

print("Factorial of", n, "is", fact)  
