# -*- coding: utf-8 -*-
"""課題_条件分岐のif文で処理を切り替えよう

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xF5lQdOyjRABiPQPNx4Jt0ygxpaoILxW
"""

import random

var = random.randint(1,15)

print(var)

if var % 3 == 0 and var % 5 == 0:
  print("FizzBuzz")
elif var % 3 == 0:
  print("Fizz")
elif var % 5 == 0:
  print("Buzz")
else:
  print(var)