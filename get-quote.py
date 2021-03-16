import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt",'a')
  #f.write('good day makes good mood')  #add a new line
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  last = 14
  rnd = random.randint(0,last)
  rnd2 = random.randint(0, last)
  print(quotes[rnd], end = quotes[rnd2])


if __name__== "__main__":
  primary()
