from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")

auction_items = {}
repeat = "yes"

while repeat == "yes":
  name = input("What is your name? ")
  bid = int(input("What is your bid? $ "))

  auction_items[name] = bid

  repeat = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

  if repeat == "no":
    break
  else:
    clear()

max_bid = 0
winner = ""

for key in auction_items:
  if auction_items[key] > max_bid:
    max_bid = auction_items[key]
    winner = key

print(f"The winner is {winner} with a bid of ${max_bid}.")