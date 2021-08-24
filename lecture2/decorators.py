def announce(f):
    def wrapper():
        print("Welcome user!")
        f()
        print("Bye!")
    return wrapper

@announce
def password():
    enter_password = input("Enter password:")
    key = "Hello"
    if enter_password == key:
        print("Login successful!")
    else:
        print("Wrong password.")

password()
