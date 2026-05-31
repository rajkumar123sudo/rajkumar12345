import random
import string
from time import time
import qrcode

# this is password generation
length = int(input("Enter the desired password length: "))
charactors = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(charactors)for _ in range(length))
    
print("Generated password: ", password)
print("Time taken to generate the password: ", time())
print("This is a strong password. Make sure to keep it safe and secure!")
print("kya haal meri jaan?")

# Generate QR code for the password
qrcode.make(password).save("password_qr.png")
print("QR code generated and saved as 'password_qr.png'")

# restart button
while True:
    restart = input("Do you want to generate another password? (yes/no): ").lower()
    
    if restart == "yes":
        length = int(input("Enter the desired password length: "))
        password = ''.join(random.choice(charactors)for _ in range(length))
        print("Generated password: ", password)
    
    
    else:
        print("Thank you for using the password generator!")
        print("this is strongest password ")
        break
    