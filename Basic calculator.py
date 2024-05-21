def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(add(3, 2))        
print(subtract(3, 2))   
print(multiply(3, 2))   
print(divide(3, 2))    
print(divide(3, 0))  

