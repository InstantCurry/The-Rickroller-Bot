import json
import random

with open("rickrolls.json") as f:
    data = json.load(f)

def roll():
    out = random.choice(data)
    return("<" + str(out) + ">")
