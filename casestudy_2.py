import random

l=['Journey','Imagine','Freedom','Courage','Harmony','Inspire','Curious','Balance','Triumph','Whisper']
n=random.randint(0,10)
flag=0
a=list(l[n].lower())
random.shuffle(a)
a="".join(a)
print("Lets start the game\nYour letters are:",a)
for i in range(0,3):
  ans=input(f"{i+1}st ans: ")
  if ans==l[n].lower():
    flag=1
    print(f"Contrats you did it in {i+1} attempts")
    break
  else:
    print("You Can Do It! let's try again")
if(flag==0):
  print(l[n].lower())