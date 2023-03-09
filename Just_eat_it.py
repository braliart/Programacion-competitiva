# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:25:03 2023

@author: ALIERAB
"""

def _main() -> None:
  # TODO: fixme.
  test_cases =  int(input()) #Digite número de pruebas

  for i in range(test_cases):
    n = int(input()) #Digite número de cupcakes
    cupcakes_bad = input() #Digite la magnitud de sabor de los cupcakes como sigue: 1 -4 7 -3 \n
    cupcakes = cupcakes_bad.split(" ")
    #cupcakes = [int(i) for i in cupcakes]
    top = 0
    suma = 0
    sumcup = 0
    
    for cup in cupcakes:
      cupcake = int(cup)
      if cupcake >= 0:
        suma += cupcake
      else:
          suma = 1
      top = max(top,suma)
      sumcup += cupcake
        

    if top > sumcup:
      print("NO")
    else:
      print("YES")

  pass

if __name__ == '__main__':
  _main()