alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  end_text = ''
  if direction == 'decode':
    shift *= -1
  for letter in text:
    if letter in alphabet:
      alpha_index = alphabet.index(letter)
      new_index = alpha_index + shift
      if new_index >=26:
        new_index -= 26
      end_text += alphabet[new_index]
    else:
      # If the user enters a number/symbol/space let it be as it is
      end_text += letter

  print(f"Here's the {direction}d result: {end_text}")

# Importing and printing the logo from art.py when the program starts.
from art import logo
print(logo)

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

# If the user enters a shift that is greater than the number of letters in the alphabet.
# Used modulus as the remainder will be the repition
  shift = shift % 26
  caesar(text, shift, direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == 'no':
    should_continue = False
    print("Goodbye 👋")
