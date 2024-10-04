from cryptography.fernet import Fernet

'''
key + password + text to encrypt = random text
random text + key + password = original text
'''

'''
# Generate key to encrypt password, and store it in a key file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# read the key file to get key
def load_key():
    #file = open("key.key", "rb")
    file = open("key.key", "r")
    key = file.read()
    file.close()
    return key

key = load_key()
#initialise encryption module
fer = Fernet(key)

def add():
    username = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as file:
        #encode and encrypt password entered and write in file
        file.write(username + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 

def view():
    with open("password.txt", "r") as file:
        for line in file.readlines():
            name, password = line.rstrip().split("|")
            print(f"Username: {name} | Password: {fer.decrypt(password.encode()).decode()}")
    pass

while True:
    mode = input("Would you like to add a new password or view existing passwords? (add/view), or press q to quit : ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Invalid Mode.")