def greet(name1, name2):
    print(f'{name1} says hello to {name2}')

def greeter(name):
    print(f'Hello {name}!')
    
def say(word):
    print(word)

def say_hello_times(n = 10):
    for i in range(n):
        print('Hello')

#greet('Bob', 'Greg')
say_hello_times(5)