"""
THANK YOU FOR IMPORTING THE MOST USELESS MODULE EVER CREATED!
I hope you hate it!

p.s. Hi, PhoenixSC!
---O9CreeperBoi
"""

import time
import random

CURSOR_UP = "\033[1A"
CLEAR = "\x1b[2K"
CLEAR_LINE = CURSOR_UP + CLEAR

# Oops! Can't have users cursing in MY module!
# We don't want to have a repeat of Project Gray Kiwi, now do we?
banned = ["pee", "poo", "fuc", "shi", "damn", " hell ", "nig", "bitc", "craft a", "kil", "unaliv", "die", "slas", "end update", "viola", "dam", "frick", "hecking", "sex", "nut", "virgin", "weed", "sucks"]

# Peanut butter 💀
pb = ["peanut butter", "your cat", "pb", "earth cat"]

# Let's greet Merl!
greet = ["hi", "hello", "wassup", "whats up", "what's up", "whaddup", " yo ", "how are you doin", "how you doin", "greetings"]

# chicken jockey!
help = ["tell me", "help me", "help"]
cj = ["chicken jockey", "i am steve", "ender pearl", "boots of swiftness", "water bucket", "lava chicken", "the nether", "flint and steel", "crafting table"]



def printanim(msg: str):
  split_msg = msg.split()
  f = ""
  print("")
  for x in range(len(split_msg)):
    f = f"{f} {split_msg[x]}"
    print(CLEAR_LINE, f)
    time.sleep(0.05)



# the actual code to run
def replyPrint(prompt: str):
  time_tuple = time.localtime()
  hour = time_tuple.tm_hour
  global pb
  global banned
  if hour >= 9 and hour <= 16 and random.randint(0, 5) < 4:
    printanim("We are currently experiencing higher")
    printanim("traffic than expected. Please wait")
    printanim("a moment and resend your last")
    printanim("message.")
  else:
    if any(sub.lower() in prompt.lower() for sub in banned):
      printanim("Your previous message contains")
      printanim("language that violates our content")
      printanim("policy. Please reword your response.")
    elif any(sub.lower() in prompt.lower() for sub in pb):
      printanim("Are you talking about my cat, Peanut")
      printanim("Butter? If so, then bad news. They")
      printanim("died a while ago. :_(")
    elif any(sub.lower() in prompt.lower() for sub in help):
      printanim("I can help you with questions related")
      printanim("to Minecraft! What do you need")
      printanim("assistance with?")
    elif any(sub.lower() in prompt.lower() for sub in cj):
      printanim("No. No no no. I am not here to talk")
      printanim("about the Minecraft Movie. Can you")
      printanim("ask me anything besides that?")
    elif any(sub.lower() in prompt.lower() for sub in greet):
      printanim("Hello there! I am Merl, a support AI")
      printanim("made by Mojang. How can I help you")
      printanim("today on the topic of Minecraft?")
    else:
      g = random.randint(0,4)
      if g == 1:
        printanim("I don't know. Can I help you with a")
        printanim("question related to Minecraft?")
      elif g == 2:
        printanim("I can only provide support in")
        printanim("English right now. Can I help")
        printanim("you with a question related")
        printanim("to 'Minecraft'?")
      else:
        printanim("I don't know.")
    

