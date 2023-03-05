# function will print("detonation in... "+str(seconds_left)+" secondes.")



def detonation_in(seconds_left):
    print("detonation in... "+str(seconds_left)+" secondes.")

timer = 10

while (timer > 0):
  detonation_in(timer)
  timer -= 1