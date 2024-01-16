from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import time
import sys
import pygame 
# Initialize the pygame mixer
pygame.mixer.init() 

def print_receipt(items, prices, amount):
    total_price = sum(prices)
    if amount >= total_price:
        print(" ")
        print("\nReceipt:")
        print("------------------------------")
        for item, price in zip(items, prices):
            print(f"{item}: ₱{price}")
        print("------------------------------")
        print(f"Total: ₱{total_price}")
        print(f"Amount Paid: ₱{amount}")
        print(f"Change: ₱{amount - total_price}")
        print("------------------------------")
        print("Thank you sa pamimili!")
    else:
        print("Invalid. Amount is less than the total price or you're just too broke.")

def delete_last_line():
    #cursor up one line
    sys.stdout.write('\x1b[1A')
    #delete last line
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
    
print(bold_text("------- CASH REGISTER -------"))
time.sleep(1)   
    
def main():
    items = []
    prices = []
    
    while True:
        print("")
        print("Enter item name ('check out' to finish): ")
        item = input("")
        check_out = ['done', 'check out', 'finished', 'beep', 'agree', 'next', 'agreed', 'oum']
        if item.lower() in check_out:
            break
        print("")   
        price = float(input("Enter item price: ₱"))
        items.append(item)
        prices.append(price)
        sound_file ="sfx\scanner.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
    print("")
    amount = float(input("Enter the amount paid: ₱"))
    sound_file ="sfx\purchase.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    delete_multiple_lines(n=1000)
    print(bold_text("------- CASH REGISTER -------"))
    sound_file ="sfx\dot matrix.mp3"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    loading_bar(5)
    print_receipt(items, prices, amount)

if __name__ == "__main__":
    main()
    