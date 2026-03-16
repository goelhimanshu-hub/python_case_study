import random
def guess():
  num=random.randint(0,100)
  attempt=1
  opt=int(input("enter: "))
  while num!=opt:
    if(opt>num):
      print("Too High")
    elif(opt<num):
      print("Too Low")
    opt=int(input("enter: "))
    attempt+=1
  else:
    print(f"congrats u did it after {attempt} attempt")
    return
    
guess()