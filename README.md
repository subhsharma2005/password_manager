In today’s digital age, managing passwords for various online accounts is a critical task. With numerous accounts to handle, it’s easy to fall into the trap of reusing passwords or choosing weak ones. This project report details the creation of a Password Manager application, a user-friendly, secure tool that helps users store and retrieve their passwords with ease. The project leverages the cryptography and Tkinter libraries in Python. 

Encryption: Uses Fernet symmetric encryption from the cryptography library to securely store passwords

Key Management: Automatically generates and stores an encryption key in "key.key" file if one doesn't exist

Password Storage: Saves encrypted passwords in a text file ("passwords.txt") with associated website names

Password Retrieval: Allows users to retrieve and decrypt stored passwords when needed

Users can add new passwords by entering a website and password, then clicking "Add Password"

Users can retrieve stored passwords by entering the website and clicking "Get Password"

The application handles all encryption/decryption automatically
