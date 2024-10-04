import hashlib

user=input("Enter the username :")

password=input("Enter the password :").encode()

h=hashlib.sha256()

h.update(password)

print(h.hexdigest())    

while user != "" and password != h :

    print('username or password is wrong')

else:

    print('Enter the main menu')