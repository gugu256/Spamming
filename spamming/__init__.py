import pyautogui as pgi
import random

try:
  from winsound import Beep as b
  can_beep = True
except:
  can_beep = False

"""
Spamming: a simple package for spamming people
go to www.pypi.org/project/spamming/0.1.3/ to see its documentation
"""

class nonsense:

  dafuq = "#~é'}])([{è-/ç^à@°+=£$¤µ*%ù§!:.;?,><0123456789azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN "


  def main(nbr: int, slw: int):
    """
    nbr: the number of messages to send
    slw: the interval at which said messages have to be sent
    """
    print("STARTING IN 5 SECONDS")
    if slw <= 5:
      slw = 0
    else:
      slw -= 5

    pgi.sleep(5)
    if can_beep:
      b(660, 500)

    for i in range(0, nbr):
      msg = ""
      for j in range(0, 128): 
        msg += random.choice(nonsense.dafuq)
      pgi.write(msg)
      pgi.press("enter", 1, 0.1)
      pgi.sleep(slw)

class spamclick:

  def main(clicks: int):
    """
    clicks: the number of times you want to click
    """

    print("STARTING IN 5 SECONDS")

    pgi.sleep(5)

    if can_beep:
      b(660, 500)

    for i in range(0, clicks):
      pgi.leftClick(interval=0.01)