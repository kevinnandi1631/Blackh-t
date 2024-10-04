def formula(x,y,operation):
    if operation == 'add':
        return x+y
    
    elif operation == 'subtract':
        return x-y
    
    elif operation == 'multiply':
        return x*y
    
    elif operation == 'divide':
        return x/y
    
    elif operation == 'modulus':
        return x%y
    
print (formula(1,2,'add'))
print (formula(1,2,'subtract'))
print (formula(1,2,'multiply'))
print (formula(1,2,'divide'))
print (formula(1,2,'modulus'))