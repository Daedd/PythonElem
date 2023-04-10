import os
import time

auction = {}


def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    # Add name and bid to auction Dict
    auction[name] = bid
    for a, b in auction.items():
        print(f"DEBUG: {a} > {b}")


main()
while True:
    more = input("Is there another bidder? ")
    if more == "y" or more == "yes:":
        cls()
        main()
    else:
        # Iterate through Dict
        winner = max(auction, key=auction.get)
        print(f'The winner of the auction is: {winner} with a bid of: ${auction[winner]}!')
        time.sleep(3)
        break
