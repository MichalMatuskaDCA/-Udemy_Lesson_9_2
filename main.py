from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
dict, add = {}, True

def add_person(name, bill):
  dict[name] = bill
  
def print_result(dict):
  bill = 0
  for item in dict:
    if int(dict[item]) > int(bill):
      winner = item
      bill = dict[item]
  print(f"The winner is {winner} with the bill of {bill}")

while add:
  name = input("What is your name ? : ")
  bill = input("What is your bill ? : ")
  add_person(name, bill)
  choice = input("Continue? ")
  if choice == 'no':
    add = False 
  else:
    clear()

print_result(dict)


  