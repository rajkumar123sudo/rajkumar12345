import random
import string
import qrcode

def generate_otp(length=6):
    """Generate a random OTP of specified length."""
    return ''.join(random.choices(string.digits, k=length))

# creating a qr code in otp generator in sabse pehle otp generate karna hoga uske baad qr code generate karna hoga
def generate_qr_code(data, filename):
    """Generate a QR code for the given data and save it to a file."""
    qr = qrcode.make(data)
    qr.save(filename)

print("Welcome to the OTP Generator!")
otp_length = int(input("Enter the desired length of the OTP (default is 6): "))
if otp_length <= 0:
    print("Invalid length. Using default length of 6.")
    otp_length = 6

otp = generate_otp(otp_length)
print(f"Generated OTP: {otp}")
# qr code in a otp generator
generate_qr_code(otp, "otp_qr.png")
print("QR code generated and saved as 'otp_qr.png'")
# this is a qr code generator for the otp generator
print("Thank you for using the OTP Generator!")
restart = input("Do you want to generate another OTP? (yes/no): ").strip().lower()
while restart == 'yes':
    otp_length = int(input("Enter the desired length of the OTP (default is 6): "))
    if otp_length <= 0:
        print("Invalid length. Using default length of 6.")
        otp_length = 6
    otp = generate_otp(otp_length)
    print(f"Generated OTP: {otp}")
    restart = input("Do you want to generate another OTP? (yes/no): ").strip().lower()
    