import cv2
import os
import string

# Specify the absolute path to the image file
image_path = os.path.abspath("car.jpg")

# Check if the image file exists
if not os.path.isfile("C:/Users/DELL/Downloads/cybersecurity/car.jpg"):
    print("Image file does not exist. Check the file path.")
else:
    img = cv2.imread("C:/Users/DELL/Downloads/cybersecurity/car.jpg")

    if img is not None:
        msg = input("Enter secret message")
        password = input("Enter password")

        d = {chr(i): i for i in range(255)}
        c = {i: chr(i) for i in range(255)}

        m = 0
        n = 0
        z = 0

        for i in range(len(msg)):
            img[n, m, z] = d[msg[i]]
            n += 1
            m += 1
            z = (z + 1) % 3

        cv2.imwrite("Encryptedmsg.jpg", img)
        os.system("start Encryptedmsg.jpg")

        message = ""
        n = 0
        m = 0
        z = 0

        pas = input("Enter passcode for Decryption")

        if password == pas:
            for i in range(len(msg)):
                message = message + c[img[n, m, z]]
                n += 1
                m += 1
                z = (z + 1) % 3
            print("Decryption message", message)
        else:
            print("Not a valid key")
    else:
        print("Failed to load the image. Check the image format and file integrity.")
