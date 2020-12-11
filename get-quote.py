import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  size = len(quotes)
  rnd1 = random.randint(0,size-1)
  rnd2 = random.randint(0,size-1)
  if rnd1 == rnd2: 
    rnd2 = (rnd2+3)%size

  print(quotes[rnd1].strip())
  print(quotes[rnd2].strip())

if __name__== "__main__":
  primary()
