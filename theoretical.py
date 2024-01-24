import math
import random

def calculation():

  red_total = 70
  red_wanted = 40
  white_total = 30
  white_wanted = 20

  repeats = 1000
  sucess = 0
  k = 0

  while k < repeats:

    list = ['R'] * red_total + ['W'] * white_total
    n = 100

    red = 0
    white = 0
    choices = 60

    for i in range(choices):

      r = random.randint(0, n - 1)

      if list[r] == 'R':

        red += 1

      else:

        white += 1

      list[r] = list[n-1]
      n -= 1


    if red == red_wanted and white == white_wanted:
      sucess += 1

    k += 1

  return(sucess/repeats)
  #print(sucess/repeats)





