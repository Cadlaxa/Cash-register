# python modules
from os import environ #to read local environment
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # hides the welcom message ng pygame
import cv2 # OpenCV python library for scanner
from pyzbar.pyzbar import decode # pang decode ng QR code and Bar Codes
import time
import sys # used to use reg ex
import pygame #for sfx and such
from colorama import Fore # for colored texts
import random
import string
from tabulate import tabulate # for creating tables
import textwrap # unused might remeove soon
from collections import Counter #item counter

# Initialize the pygame mixer
pygame.mixer.init()
# Generate a random string of length 10
random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
# Generate a random number of length 10 
random_string_num = ''.join(random.choices(string.digits, k=10))
# For printing cuurent date and time sa receipt
dateNtime = time.localtime(time.time())
local_time = time.asctime(dateNtime)

# Function to read QR/bar code
def scanner():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                print(obj.data.decode("utf-8"))
                return obj.data.decode("utf-8")
            cv2.imshow("QR/Bar Code Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

# Function to print receipt
def print_receipt(items, prices, amount, order_type, is_staff, staff_name=""):
    total_price = sum(prices)
    if amount >= total_price:
        time.sleep(1)
        print('')
        print(Fore.LIGHTYELLOW_EX + '''             ──────▄▀▄─────▄▀▄
            ─────▄█░░▀▀▀▀▀░░█▄
            ─▄▄──█░░░░░░░░░░░█──▄▄
            █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█'''.center(50) + Fore.RESET)
        print(Fore.LIGHTGREEN_EX + "𝐋𝐚𝐱'𝐬 𝐁𝐨𝐮𝐥𝐚𝐧𝐠𝐞𝐫𝐢𝐞 𝐞𝐭 𝐏𝐚𝐭𝐢𝐬𝐬𝐞𝐫𝐢𝐞".center(50) + Fore.RESET)
        print("OWNED & OPERATED BY: GROUP 1".center(50))
        print("Cavite Civic Center, Palico IV. Imus City, Cavite, 4103".center(50))
        print("VAT REG TIN:".ljust(28), "XXX-XXX-XXX-XXX".rjust(20))
        print("SN:".ljust(28) + random_string.rjust(20))
        time.sleep(1)
        if is_staff:
            print("Staff Name:".ljust(28) + staff_name.rjust(20))
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        time.sleep(1)
        print(bold_text(Fore.LIGHTGREEN_EX + "OFFICIAL RECEIPT").center(63))
        print("OR No.:".ljust(28) + random_string_num.rjust(20))
        print(bold_text(local_time.center(50)))
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        print(bold_text(Fore.LIGHTGREEN_EX + order_type.center(50).upper()+ Fore.RESET))
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        # Combine items and prices into a list of tuples
        item_price_pairs = list(zip(items, prices))
        # Count the occurrences of each unique item-price pair (bilangin kung ilan yung unique items then count kung ilan)
        item_price_counter = Counter(item_price_pairs)
        # Create a table for items and prices via tabulate
        table_data = [(count, item, f"₱{price}", f"₱{count * price}") for (item, price), count in item_price_counter.items()]
        table_headers = [bold_text(Fore.LIGHTCYAN_EX + 'No:'), bold_text(Fore.LIGHTCYAN_EX + 'Item/s'), bold_text(Fore.LIGHTCYAN_EX + 'Price per Item'), bold_text(Fore.LIGHTCYAN_EX + 'Price Total')]
        time.sleep(1)
        table = tabulate(table_data, headers=table_headers, tablefmt="fancy_grid")
        print(table.center(50))
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        time.sleep(1)
        # Create a table for total amount paid and change via tabulate module
        print("Total:".ljust(28), f"₱{total_price:.2f}".rjust(20))
        print("Amount Paid:".ljust(28), f"₱{amount:.2f}".rjust(20))
        print("Change:".ljust(28), f"₱{amount - total_price:.2f}".rjust(20))
        time.sleep(2)
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        vat_rate = 0.12 # 12% VAT
        vat = total_price * vat_rate
        #vat_amount = prices * vat_rate
        print("Sales:".ljust(28), f"₱{total_price:.2f}".rjust(20))
        print("Net sales:".ljust(28), f"₱{total_price - vat:.2f}".rjust(20))
        print("Vat Amount:".ljust(28), f"₱{vat:.2f}".rjust(20))
        time.sleep(1)
        print("Amount Due:".ljust(28), f"₱{total_price:.2f}".rjust(20))
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        time.sleep(1)
        print("THIS SERVES AS YOUR OFFICIAL RECEIPT".center(50))
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        time.sleep(1)
        print("\"THIS RECEIPT SHALL BE VALID FOR".center(50))
        print("FIVE (5) YEARS FROM THE DATE OF".center(50))
        time.sleep(1)
        print("PERMIT TO USE\"".center(50))
        print(bold_text(Fore.YELLOW + "-" * 50 + Fore.RESET))
        print("--Thank you, and please come again-- 🤑".center(50))
        print(Fore.LIGHTRED_EX +
'''        ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█
        ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█'''.center(50))
    else:
        sound = pygame.mixer.Sound("sfx\\notification.mp3")
        sound.play()
        print(Fore.LIGHTMAGENTA_EX + "Invalid. Insufficient amount. Please enter an amount equal to or greater than the item price 😥")

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

# SFXs
start_notif = "sfx\mixkit-software.wav"
pop_notif = "sfx\\tap-notification.mp3"
error_notif = "sfx\\notification.mp3"
scan_notif = "sfx\scanner.mp3"
open_notif = "sfx\open.wav"
close_notif = "sfx\close.wav"
void_notif = "sfx\mixkit-interface-option-select-2573.wav"

sound = pygame.mixer.Sound(open_notif)
sound.play()
print(Fore.GREEN + '''
█████████████████████████████████████████▀█████████████████████████████
█─▄▄▄─██▀▄─██─▄▄▄▄█─█─███▄─▄▄▀█▄─▄▄─█─▄▄▄▄█▄─▄█─▄▄▄▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█
█─███▀██─▀─██▄▄▄▄─█─▄─████─▄─▄██─▄█▀█─██▄─██─██▄▄▄▄─███─████─▄█▀██─▄─▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀'''.center(50))
time.sleep(1)
print("")
sound = pygame.mixer.Sound(pop_notif)
sound.play()
print(bold_text(Fore.YELLOW + "Hi Welcome to Lax's Boulangerie et Patisserie"))

time.sleep(1)
print("")

def main():
    # Enable/disable scanner input
    use_scanner = False
    sound = pygame.mixer.Sound(pop_notif)
    sound.play()
    print(bold_text("Use camera to scan QR/Bar code? (yes/no)"))
    qr_response = input("").lower()
    if qr_response in ['yes', 'oo', 'yup', 'yas', 'yass', 'oum', 'ey', 'correct', 'y', 'yeah']:
        sound = pygame.mixer.Sound(pop_notif)
        use_scanner = True
        time.sleep(1)
        
    # staff 
    is_staff = False
    staff_name = ""
    sound = pygame.mixer.Sound(pop_notif)
    sound.play()
    print("")
    print(bold_text("Are you a staff member? (yes/no)"))
    staff_response = input("").lower()
    staff = ['yes', 'oo', 'yup', 'yas', 'yass', 'oum', 'ey', 'correct', 'y', 'yeah']
    if staff_response in staff:
        is_staff = True
        print("")
        sound = pygame.mixer.Sound(pop_notif)
        sound.play()
        staff_name = input("Enter your name: ")

    items = []
    prices = []
    order_type = ""
    if staff_response in staff:
        is_staff = True
        delete_multiple_lines(10)
    else:
        delete_multiple_lines(8)
    while True:  # Dito yung item/price item via qr/bar code scanner or console input
        print(Fore.RESET)
        sound = pygame.mixer.Sound(pop_notif)
        sound.play()
        if use_scanner:  # Use scanner input
            print(bold_text(Fore.YELLOW + "Scan item/product (scan staff id to 'check out', 'void' to remove item): "+ Fore.RESET))
            item = scanner()
            sound = pygame.mixer.Sound(scan_notif)
            sound.play()
            # Split the scanned data using '=' as the delimiter/splitter
            parts = item.split('=')
            if len(parts) == 2:
                item = parts[0].strip()  # Extract item name
                try:
                    price = float(parts[1].replace('₱', '').strip())  # Extract and convert price
                except ValueError:
                    sound = pygame.mixer.Sound(scan_notif)
                    sound.play()
                    print(Fore.LIGHTMAGENTA_EX + "Invalid price format in the QR/Bar code try again." + Fore.RESET)
                    continue
        else:  # Use console input
            print(bold_text(Fore.LIGHTBLUE_EX + "Enter item name ('check out' to finish, 'void' to remove item): "+ Fore.RESET))
            item = input("")

            # Initialize price before checking qr_response (very important kasi nag aapend pa rin sya if the user switches input)
            price = None
        
        # Void item/s (removes the last item if user types the keyword)
        void = ['void', 'Void', 'VOID', 'delete', 'del','DEL','item void']
        if item in void:
                if items:
                    deleted_item = items.pop()
                    deleted_price = prices.pop()
                    time.sleep(1)
                    print("")
                    sound = pygame.mixer.Sound(void_notif)
                    sound.play()
                    print(Fore.LIGHTYELLOW_EX + f"Deleted last item: {deleted_item} - ₱{deleted_price}" + Fore.RESET)
                    time.sleep(1)
                else:
                    time.sleep(1)
                    print("")
                    sound = pygame.mixer.Sound(void_notif)
                    sound.play()
                    print(Fore.LIGHTMAGENTA_EX + "No items to delete." + Fore.RESET)
                    time.sleep(1)
                continue
            
        # Console to Scanner, Scanner to Console override
        override = ['override', 'switch input', 'switch', 'next', 'new']
        if item in override:
            use_scanner = not use_scanner
            time.sleep(1)
            sound = pygame.mixer.Sound(open_notif)
            sound.play()
            print("")
            print(Fore.LIGHTGREEN_EX + "Scanner Overridden. Switching input mode. Now using Console input" + Fore.RESET if not use_scanner
                else Fore.LIGHTGREEN_EX + "Console Overridden. Switching input mode. Now using Scanner input" + Fore.RESET)
            time.sleep(1)
            continue

        # Check-out conditions # May bug sya pag no items then check out, nag piprint nmn yung error message but the loop continues sa enter
        check_out = ['done', 'check out', 'finished', 'beep', 'agree', 'next', 'agreed', 'oum', 'check-out']
        if item.lower() in check_out:
            break

        # Check if the price needs to be obtained via console input
        if not use_scanner:
            while True:
                try:
                    print(Fore.RESET)
                    sound = pygame.mixer.Sound(pop_notif)
                    sound.play()
                    price = float(input(bold_text("Enter item price: ₱")))
                    sound = pygame.mixer.Sound(scan_notif)
                    sound.play()
                    if price < 0:
                        sound = pygame.mixer.Sound(error_notif)
                        sound.play()
                        print(Fore.LIGHTMAGENTA_EX +
                            "Invalid input. Value of the item must be positive, input a non-negative number")
                        time.sleep(2)
                    else:
                        break
                except ValueError:
                    sound = pygame.mixer.Sound(error_notif)
                    sound.play()
                    print(Fore.LIGHTMAGENTA_EX +
                        "Invalid input. Please enter a valid number for the item price." + Fore.RESET)
                    time.sleep(2)

        # Append the item and price to the respective lists (sum of items sa console or scanner or switch input vice versa)
        items.append(item)
        prices.append(price)
        sound = pygame.mixer.Sound(scan_notif)
        sound.play()
        time.sleep(1)

    while True: # Dito na yung ibabayad (enter yung amount) via console
        try:
            time.sleep(1)
            print(Fore.RESET)
            sound = pygame.mixer.Sound(pop_notif)
            sound.play()
            amount = float(input(bold_text("Enter the amount paid: ₱")))
            if amount >= 1:
                sound_file = "sfx\livechat-129007.mp3"
                sound = pygame.mixer.Sound(sound_file)
                sound.play()
            time.sleep(1)
            if amount < 0:
                    sound = pygame.mixer.Sound(error_notif)
                    sound.play()
                    print(Fore.LIGHTMAGENTA_EX + 
                    "Invalid input. Value of the item must be positive, input a non-negative number" + Fore.RESET)
                    time.sleep(2)
            else:
                break
        except ValueError:
            sound = pygame.mixer.Sound(error_notif)
            sound.play()
            print(Fore.LIGHTMAGENTA_EX +
                    "Invalid input. Please enter a valid number for the item price." + Fore.RESET)
            time.sleep(2)

    # Dine-in or Take-out the products
    print("")
    sound = pygame.mixer.Sound(pop_notif)
    sound.play()
    print(bold_text("Is this for dine-in or take-out?"))
    while True:
        order_type = input("").lower()
        dine_inout = ['dine-in', 'dine in', 'dine', 'take-out', 'take out', 'take', 'in', 'out']
        if order_type in dine_inout:
            break
        else:
            sound = pygame.mixer.Sound(error_notif)
            sound.play()
            print(Fore.LIGHTMAGENTA_EX +
                  "Invalid input. Please enter 'dine-in' or 'take-out'" + Fore.RESET)
            time.sleep(2)
            print("")
            print("Is this for dine-in or take-out?"+ Fore.RESET)

    sound_file = "sfx\purchase.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

    # Delete lahat ng console output and proceed sa printing ng receipt for cleaner output
    delete_multiple_lines(n=1000)
    print(Fore.LIGHTMAGENTA_EX + '''
█████████████████████████████████████████▀█████████████████████████████
█─▄▄▄─██▀▄─██─▄▄▄▄█─█─███▄─▄▄▀█▄─▄▄─█─▄▄▄▄█▄─▄█─▄▄▄▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█
█─███▀██─▀─██▄▄▄▄─█─▄─████─▄─▄██─▄█▀█─██▄─██─██▄▄▄▄─███─████─▄█▀██─▄─▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀'''.center(50))
    sound_file = "sfx\dot matrix.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    loading_bar(5)
    total_price = sum(prices)
    if amount >= total_price:
        print_receipt(items, prices, amount, order_type, is_staff, staff_name)
    else:
        sound = pygame.mixer.Sound(error_notif)
        sound.play()
        print(Fore.LIGHTMAGENTA_EX + "Invalid. Insufficient amount. Please enter an amount equal to or greater than the item price 😥")

if __name__ == "__main__":
    main()
