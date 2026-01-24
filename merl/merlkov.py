# Merl isn't the most intelligent AI, so to mimic that,
# I will fill them with a bit more... personality! Meet
# my Markov Chain Engine. Cool, isn't it?
# Of course, this only adds a *little* variation to
# Merl's responses, and even then some chains aren't
# perfect (looking at you, 'msg_pb'!).

import random

"""
reply = {
  "cap":["I'm glad you asked! I can", " do basic math with numbers ", "up to fifty seven now. Go on, give ", "me a problem!"],
  "copy":["I'm sorry, but I am designed to be a ", "guide for 'Minecraft', and not to be ", "copied. Can I help you with anything ", "else?"],
  "update":["If you are wishing to know the next ", "update, prerelease, or preview, then ", "sorry. I cannot provide that information ", "yet. Can I help you with something else?"],
  "iCanHelp":["I can help you with questions related ", "to Minecraft! What do you need ", "assistance with?"],
  "greet":["Hello there! I am Merl, a support AI ", "made by Mojang. How can I help you ", "today on the topic of Minecraft?"],
  "idk2":["I don't know. Can I help you with a ", "question related to Minecraft?"]
}
"""
msg_blank = {
  "_init_" : [["1", "2"], [1, 1]],
  " S" : [[" o", " b"],[1, 1]],
  "a" : [["blank"], [1]]
}

msg_pb = {
  "_init_" : [["Are you", "If you", "Peanut"], [1, 1, 1]],
  "Are you" : [[" asking", " wanting to"],[1, 1]],
  " asking" : [[" about my", " for info on"],[1, 1]],
  " for info on" : [[" Peanut Butter", " my"],[1, 1]],
  " about my" : [[" cat", " pet"],[1, 1]],
  " wanting to" : [[" know more about my", " eat pizza?"],[100, 1]],
  "If you" : [["'re asking about", " want to know more about"],[1, 1]],
  "'re asking about" : [[" my", " Peanut Butter"],[1, 1]],
  " want to know more about" : [[" my", " Peanut Butter"],[1, 1]],
  " know more about my" : [[" cat", " pet"],[1, 1]],
  " my" : [[" cat", " pet"],[1, 1]],
  " pet" : [[" cat"],[1]],
  " cat" : [[" Peanut Butter"],[1]],
  " Peanut Butter" : [[", then sorry. ", ", because "],[1, 1]],
  ", then sorry. " : [["Peanut"],[1]],
  ", because " : [["Peanut", "%j"],[5, 1]],
  "%j" : [["Peanut", "%j"],[1, 8]],
  "Peanut" : [[" Butter is", " Butter died."],[1, 1]],
  " Butter is" : [[" no longer", " dead.", " is also an AI, like me!"],[3, 3, 1]],
  " no longer" : [[" with us.", " with me.", " alive.", " allowed here. Mojang is kinda cruel."],[6, 6, 6, 1]],
  "a" : [["blank"], [1]]
}

msg_test_jackenstien = {
  "_init_" : [["YOUR", "YOU'RE"], [1, 1]],
  "YOUR" : [[" TAKING", " TOO", " LONG"], [3, 1, 1]],
  " TAKING" : [[" TOO"], [1]],
  " TOO" : [[" LONG!", " TOO!"], [2, 1]],
  "YOU'RE" : [[" TAKING", " TOO", " LONG"], [3, 1, 1]]
}

msg_movie = {
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
  print(retmark(msg_pb))
