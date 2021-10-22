from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
dict, add = {}, True

def add_person(name, bill):
  dict[name] = bill
  
def print_result(dict):
  bid = 0
  for item in dict:
    if int(dict[item]) > int(bid):
      winner = item
      bid = dict[item]
  print(f"The winner is {winner} with the bid of ${bid}")

while add:
  name = input("What is your name ? : ")
  bid = input("What is your bid ? : ")
  add_person(name, bid)
  choice = input("Continue? ")
  if choice == 'no':
    add = False 
  else:
    clear()

print_result(dict)


  