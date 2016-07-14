import os
import math

i=0
while i<200:
  print("yo")
  i=i+1

def stupid(i):
  if i>=200:
    q = input("how fictional are your octo-parakeets?")
    print(q)
    print("that's a stupid answer, try again")
    stupid(i)

stupid(i)
  
