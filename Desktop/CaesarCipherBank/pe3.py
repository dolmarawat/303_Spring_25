import string
import datetime

# Function to encode text using Caesar cipher
def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""
    for char in input_text:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            encoded_text += shifted_char
        else:
            encoded_text += char
    return alphabet, encoded_text

# Function to decode text using Caesar cipher
def decode(input_text, shift):
    decoded_text = ""
    for char in input_text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            decoded_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decoded_text += char
    return decoded_text

# BankAccount class
class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=datetime.date.today(), balance=0):
        if creation_date > datetime.date.today():
            raise Exception("Account creation date cannot be in the future.")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            print("Negative deposit amounts are not allowed.")
            return
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            print("Negative withdrawals are not allowed.")
            return
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")
    
    def view_balance(self):
        return self.balance

# SavingsAccount subclass
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            print("Withdrawals are not permitted within the first 180 days of account creation.")
            return
        if self.balance - amount < 0:
            print("Overdrafts are not permitted in SavingsAccount.")
            return
        super().withdraw(amount)

# CheckingAccount subclass
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount)
        if self.balance < 0:
            self.balance -= 30  # Overdraft fee
            print("Overdraft incurred. Additional $30 fee applied.")

