"""#Ask user for name
name = input("What's your name?")
#Remove whitespace
name = name.strip()
#Capitalize username
name = name.title()
#Say hello
print(f"Hello, {name}")"""

"""name = input("What's your name?").strip().title() #Ask for name
print(f"Hello, {name}") #Say hello"""

"""name = input("What's your name?").strip().title()

def hello():
    print(f"Hello, {name}")

hello()"""

def main():
    name = input("What's your name?").strip().title()
    hello(name)

def hello(user_name):
    print(f"Hello, {user_name}")

main()