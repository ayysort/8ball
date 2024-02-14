import random
print(" ")
print("You picked up an 8 ball")

def roll():
  print(" ")
  q = input('Ask your question: ')

  num = random.randint(1, 9)

  if num == 1:
    print('Yes - definitely.')
    another()
  elif num == 2:
    print('It is decidedly so.')
    another()
  elif num == 3:
    print('Without a doubt.')
    another()
  elif num == 4:
    print('Reply hazy, try again.')
    another()
  elif num == 5:
    print('Ask again later.')
    another()
  elif num == 6:
    print('Better not tell you now.')
    another()
  elif num == 7:
    print('My sources say no.')
    another()
  elif num == 8:
    print('Outlook not so good.')
    another()
  elif num == 9:
    print('Very doubtful.')
    another()

def another():
  while True:
    print(" ")
    again = input("Ask another question? (y/n): ")
    if again == 'y':
      roll()
    elif again == 'n':
      print(" ")
      print("You put down the 8 ball")
      exit()
    else:
      print("Wrong Input..")
      continue

roll()