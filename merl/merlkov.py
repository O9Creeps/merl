import random
"""
reply = {
  "cap":["I'm glad you asked! I can", " do basic math with numbers ", "up to fifty seven now. Go on, give ", "me a problem!"],
  "copy":["I'm sorry, but I am designed to be a ", "guide for 'Minecraft', and not to be ", "copied. Can I help you with anything ", "else?"],
  "update":["If you are wishing to know the next ", "update, prerelease, or preview, then ", "sorry. I cannot provide that information ", "yet. Can I help you with something else?"],
  "pb":["Are you talking about my cat, Peanut ", "Butter? If so, then bad news. They ", "died a while ago. :_("],
  "iCanHelp":["I can help you with questions related ", "to Minecraft! What do you need ", "assistance with?"],
  "greet":["Hello there! I am Merl, a support AI ", "made by Mojang. How can I help you ", "today on the topic of Minecraft?"],
  "idk2":["I don't know. Can I help you with a ", "question related to Minecraft?"]
}
"""
msg_blank = {
  "_init_" : [["1", "2"], [1, 1]],
  "item" : [["blank"],[1]],
  " S" : [[" o", " b"],[1, 1]],
  "a" : [["blank"], [1]]
}

msg_test_jackenstien = {
  "_init_" : [["YOUR", "YOU'RE"], [1, 1]],
  "YOUR" : [[" TAKING", " TOO", " LONG"], [3, 1, 1]],
  " TAKING" : [[" TOO"], [1]],
  " TOO" : [[" LONG!", " TOO!"], [2, 1]],
  "YOU'RE" : [[" TAKING", " TOO", " LONG"], [3, 1, 1]]
}

msg_minecrap = {
  "_init_": [["No.", "Sorry", "Nuh uh,"], [4, 2, 1]],
  "No." : [[" No"],[1]],
  " No" : [[" no", " no.", " no!"],[3, 1, 1]],
  " no" : [[" no", " no.", " no!"],[3, 1, 1]],
  " no." : [[" I am NOT", " I will NOT"],[1, 1]],
  " no!" : [[" I am NOT", " I will NOT"],[1, 1]],
  "Nuh uh," : [[" I am NOT", " I will NOT"],[1, 1]],
  " I am NOT" : [[" going to"],[1]],
  " going to" : [[" talk about"],[1]],
  " I will NOT" : [[" talk about"], [1]],
  " talk about" : [[" 'A Minecraft Movie'.", " the movie."],[1, 1]],
  "Sorry" : [[", but I don't", " about your"],[5, 1]],
  " about your" : [[" interest in", " stupid phase concerning"],[100, 1]],
  " interest in" : [[" 'A Minecraft Movie'.", " the movie."],[1, 1]],
  ", but I don't" : [[" feel like talking about", " want to"],[1, 1]],
  " want to" : [[" talk about"],[1]],
  " feel like talking about" : [[" 'A Minecraft Movie'.", " the movie."],[1, 1]]
}

def retmark(d: dict):
  final = ""
  cur = "_init_"
  while True:
    if cur in d.keys():
      cur = random.choices(d[cur][0], d[cur][1])[0]
      final = f"{final}{cur}"
    else: break
  return final


for x in range(10):
  print(retmark(msg_minecrap))
