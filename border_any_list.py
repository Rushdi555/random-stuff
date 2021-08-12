#list of stuff
numbers = [i for i in range(7)]

#funcion to make border longer
def border():
    border = ""
    for i in numbers:
        border += "==="
    print(border)
        
#border 
def decor(func):
    def wrap():
        border()
        func()
        border()
    return wrap()
    
@decor
def print_number():
    print(numbers)
