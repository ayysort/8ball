import random
import time
print(" ")
print("You picked up an 8 ball")

def roll():
  print(" ")
  q = input('Ask your question: ')

  answer = random.choice(['"It is certain"', '"Yes - definitely"', '"It is decidedly so"', '"Without a doubt"', '"You may rely on it"', 
                          '"As I see it, yes"', '"Most likely"', '"Outlook good"', '"Yes"', '"Signs point to yes"', '"Reply hazy, try again"', 
                          '"Ask Again later"', '"Better no tell you now"', '"Cannot predict now"', '"Concentrate and ask again"', 
                          '"Do not count on it"', '"My reply is no"', '"My sources say no"', '"Outlook not so good"', '"Very doubtful"'])
  
  print('You give it a shake...')
  time.sleep(2)
  print(' ')
  print(answer)
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
