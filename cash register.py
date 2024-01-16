from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import time
import sys
import pygame
from colorama import Fore
import random
import string

# Initialize the pygame mixer
pygame.mixer.init()
# Generate a random string of length 10
random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
# Generate a random string of length 10 (number)
random_string_num = ''.join(random.choices(string.digits, k=10))

def print_receipt(items, prices, amount, order_type):
    total_price = sum(prices)
    if amount >= total_price:
        print(" ")
        print(bold_text(Fore.BLUE + "\nGROUP 1 COMPANY NAME EMI"))
        print("OWNED & OPERATED BY: GROUP 1")
        print("Cavite Civic Center, Palico IV. Imus City, Cavite, 4103")
        print("VAT REG TIN: XXX-XXX-XXX-XXX")
        print("SN:", random_string)
        print("------------------------------")
        time.sleep(1)
        print(bold_text(Fore.BLUE + "OFFICIAL RECEIPT"))
        print("OR No.:", random_string_num)
        print("------------------------------")
        print("Order Type:", order_type)
        print("------------------------------")
        print(bold_text(Fore.CYAN + "Description        Amount"))
        print("------------------------------")
        for item, price in zip(items, prices):
            print(f"{item}:         ₱{price}")
        print("------------------------------")
        print(f"Total:         ₱{total_price}")
        print(f"Amount Paid:         ₱{amount}")
        print(f"Change:         ₱{amount - total_price}")
        print("------------------------------")
        print("THIS SERVES AS YOUR OFFICIAL RECEIPT")
        print("------------------------------")
        print("\"THIS RECEIPT SHALL BE VALID FOR")
        print("FIVE (5) YEARS FROM THE DATE OF")
        print("PERMIT TO USE\"")
        print("------------------------------")
        print("--Thank you, and please come again-- 🤑")
    else:
        print("Invalid. Amount is less than the total price or you're just too broke.")

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

print(bold_text(Fore.YELLOW + "------- CASH REGISTER -------"))
time.sleep(1)


def main():
    items = []
    prices = []
    order_type = ""

    while True:
        print("")
        print("Enter item name ('check out' to finish): ")
        item = input("")
        check_out = ['done', 'check out', 'finished', 'beep', 'agree', 'next', 'agreed', 'oum']
        if item.lower() in check_out:
            break
        print("")

        while True:
            try:
                print("")
                price = float(input("Enter item price: ₱"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the item price.")

        items.append(item)
        prices.append(price)
        sound_file = "sfx\scanner.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

    print("")
    while True:
        try:
            print("")
            amount = float(input("Enter the amount paid: ₱"))
            break
        except ValueError:
            print("Invalid input.", bold_text("Please enter a valid number"), "for the amount paid.")

    print("")
    print("Is this for dine-in or take-out?")
    while True:
        order_type = input("").lower()
        if order_type in ['dine-in', 'take-out']:
            break
        else:
            print("Invalid input. Please enter 'dine-in' or 'take-out'.")

    sound_file = "sfx\purchase.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    delete_multiple_lines(n=1000)
    print(bold_text(Fore.YELLOW + "------- CASH REGISTER -------"))
    sound_file = "sfx\dot matrix.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    loading_bar(5)
    print_receipt(items, prices, amount, order_type)

if __name__ == "__main__":
    main()
