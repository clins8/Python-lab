num = int(input("Enter an integer: "))  
fact = 1  

print(f"Factorial of {num} is:")  
for i in range(1, num + 1):  
    fact *= i  
    print(fact)  
