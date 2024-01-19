from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import time
import sys
import pygame
from colorama import Fore, init
import random
import string
from tabulate import tabulate
import textwrap
from collections import Counter

# Initialize the pygame mixer
pygame.mixer.init()
# Generate a random string of length 10
random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
# Generate a random string of length 10 (number)
random_string_num = ''.join(random.choices(string.digits, k=10))

# Function to print receipt
def print_receipt(items, prices, amount, order_type, is_staff, staff_name=""):
    total_price = sum(prices)
    if amount >= total_price:
        time.sleep(1)
        print("\n" + bold_text(Fore.BLUE + "GROUP 1 COMPANY NAME EMI").center(60))
        print("OWNED & OPERATED BY: GROUP 1".center(50))
        print("Cavite Civic Center, Palico IV. Imus City, Cavite, 4103".center(50))
        print("VAT REG TIN: XXX-XXX-XXX-XXX".center(50))
        print("SN:".ljust(13) + random_string)
        time.sleep(1)
        if is_staff:
            print("Staff Name:".ljust(13) + staff_name)
        print("-" * 50)
        time.sleep(1)
        print(bold_text(Fore.BLUE + "OFFICIAL RECEIPT").center(60))
        print("OR No.:".ljust(13) + random_string_num)
        print("-" * 50)
        print(order_type.center(50))
        print("-" * 50)
        # Count the occurrences of each item
        item_counter = Counter(items)
        # Merge similar items and calculate total prices
        unique_items = list(item_counter.keys())
        merged_prices = [sum(prices[items.index(item)] for item in items if item == unique_item) for unique_item in unique_items]
        # Create a table for items and prices via tabulate
        table_data = [(count, item, f"₱{price}") for count, (item, price) in enumerate(zip(unique_items, merged_prices), start=1)]
        for count, item, price in table_data:
            print(f"{bold_text(Fore.CYAN + 'Item No:')} {count} | {bold_text(Fore.CYAN + 'Item:')} {item} | {bold_text(Fore.CYAN + 'Price:')} {price}")
        print("-" * 50)
        time.sleep(1)
        # Create a table for total amount paid and change via tabulate
        print(f"Total: ₱{total_price}")
        print(f"Amount Paid: ₱{amount}")
        print(f"Change: ₱{amount - total_price}")
        print("-" * 50)
        time.sleep(1)
        print("THIS SERVES AS YOUR OFFICIAL RECEIPT".center(50))
        print("-" * 50)
        time.sleep(1)
        print("\"THIS RECEIPT SHALL BE VALID FOR".center(50))
        print("FIVE (5) YEARS FROM THE DATE OF".center(50))
        print("PERMIT TO USE\"".center(50))
        print("-" * 50)
        print("--Thank you, and please come again-- 🤑".center(50))
    else:
        sound_file = "sfx\\notification.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        print(Fore.LIGHTMAGENTA_EX + "Invalid. Amount is less than the total price or you're just too broke.")

def delete_last_line():
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def delete_multiple_lines(n=1):
    for _ in range(n):
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")

def loading_bar(duration, steps=20):
    for i in range(1, steps + 1):
        progress = i / steps * 100
        bar = "[" + "=" * i + " " * (steps - i) + f"] {progress:.2f}%"
        print(bar, end="\r")
        time.sleep(duration / steps)

def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

sound_file = "sfx\mixkit-software.wav"
sound = pygame.mixer.Sound(sound_file)
sound.play()
print("\n" + bold_text(Fore.YELLOW + "---------- CASH REGISTER ----------").center(50))
time.sleep(1)
print("")
sound_file = "sfx\\tap-notification.mp3"
sound = pygame.mixer.Sound(sound_file)
sound.play()
print(bold_text(Fore.YELLOW + "Hi Welcome to company name"))
time.sleep(1)

def main():
    is_staff = False
    staff_name = ""
    sound_file = "sfx\\tap-notification.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    print("Are you a staff member? (yes/no)")
    staff_response = input("").lower()
    staff = ['yes', 'oo', 'yup', 'yas', 'yass', 'oum', 'ey', 'correct']
    if staff_response in staff:
        is_staff = True
        print("")
        sound_file = "sfx\\tap-notification.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        staff_name = input("Enter your name: ")

    items = []
    prices = []
    order_type = ""

    while True:
        print("")
        sound_file = "sfx\\tap-notification.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        print("Enter item name ('check out' to finish): ")
        item = input("")
        check_out = ['done', 'check out', 'finished', 'beep', 'agree', 'next', 'agreed', 'oum']
        if item.lower() in check_out:
            break

        while True:
            try:
                print("")
                print(Fore.RESET)
                sound_file = "sfx\\tap-notification.mp3"
                sound = pygame.mixer.Sound(sound_file)
                sound.play()
                price = float(input("Enter item price: ₱"))
                if price < 0:
                    sound_file = "sfx\\notification.mp3"
                    sound = pygame.mixer.Sound(sound_file)
                    sound.play()
                    print(Fore.LIGHTMAGENTA_EX + 
                    "Invalid input. Value of the item must be positive, input a non-negative number")
                    time.sleep(2)
                else:
                    break
            except ValueError:
                sound_file = "sfx\\notification.mp3"
                sound = pygame.mixer.Sound(sound_file)
                sound.play()
                print(Fore.LIGHTMAGENTA_EX +
                      "Invalid input. Please enter a valid number for the item price.")
                time.sleep(2)

        items.append(item)
        prices.append(price)
        sound_file = "sfx\scanner.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        time.sleep(1)
    print("")
    while True:
        try:
            print(Fore.RESET)
            sound_file = "sfx\\tap-notification.mp3"
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            amount = float(input("Enter the amount paid: ₱"))
            if amount > 1:
                sound_file = "sfx\livechat-129007.mp3"
                sound = pygame.mixer.Sound(sound_file)
                sound.play()
            time.sleep(1)
            if amount < 0:
                    sound_file = "sfx\\notification.mp3"
                    sound = pygame.mixer.Sound(sound_file)
                    sound.play()
                    print(Fore.LIGHTMAGENTA_EX + 
                    "Invalid input. Value of the item must be positive, input a non-negative number")
                    time.sleep(2)
            else:
                break
        except ValueError:
            sound_file = "sfx\\notification.mp3"
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            print(Fore.LIGHTMAGENTA_EX +
                    "Invalid input. Please enter a valid number for the item price.")
            time.sleep(2)

    print("")
    sound_file = "sfx\\tap-notification.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    print("Is this for dine-in or take-out?")
    while True:
        print(Fore.RESET)
        order_type = input("").lower()
        if order_type in ['dine-in', 'take-out']:
            break
        else:
            sound_file = "sfx\\notification.mp3"
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            print(Fore.LIGHTMAGENTA_EX +
                  "Invalid input. Please enter 'dine-in' or 'take-out'.")

    sound_file = "sfx\purchase.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    delete_multiple_lines(n=1000)
    print("\n" + bold_text(Fore.YELLOW + "---------- CASH REGISTER ----------").center(50))
    sound_file = "sfx\dot matrix.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    loading_bar(5)
    print_receipt(items, prices, amount, order_type, is_staff, staff_name)

if __name__ == "__main__":
    main()
