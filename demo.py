print("Hello, World!!!")

def numSum():
    try: 
        a = int(input("First number: "))
        b = int(input("Second number: "))

        print(f"{a} + {b} = {a+b}")
    except ValueError:
        print("ValueError occured")

def personalGreeting(name):
    return "Hello " + name

numSum()
print(personalGreeting(input("What is your name? ")))
