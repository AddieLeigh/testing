print("Hello, World!!!")

def numSum(): 
    try:
        print("first input...")
        a = int(input("First number: "))
        print("first input complete. Second input...")
        b = int(input("Second number: "))
        print("second input complete. addition...")

        print(f"{a} + {b} = {a+b}")
    except ValueError:
        print("ValueError occured")

def personalGreeting(name):
    return "Hello " + name

numSum()
print(personalGreeting(input("What is your name? ")))