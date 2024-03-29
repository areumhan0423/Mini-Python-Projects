
# use the cryptography library's Fernet module for encryption and decryption
from cryptography import fernet

# create function that generates a key and writes it to a file named key.key
def write_key():
    key = fernet.Fernet.generate_key()
    with open("key.key" , "wb") as key_file:  # write in byte
        key_file.write(key)

# create function that loads the key from the key.key file.
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

key = load_key() 
fer = fernet.Fernet(key)

# create function to read the passwords file and shwos descrypted passwords with its username
def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, " | Password: ", fer.decrypt(passw.encode()).decode())

# create function to prompt user to input the account name and password
# and encrypt the password and append it to the password.txt file 
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

# use while loop to ask the user to choose between adding a new password or viewing existing ones until the user chooses to quit.
while True:
    mode = input("Would you like to add a new password" 
                 " or view existing ones (view/ add)? press q to quit. ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

