from random import choice
import sys

def makeModel(text, order):
    """ Generate a nested dictionary."""
    model = {} 
    for i in range(0, len(text) - order):
        fragment = text[i:i+order]
        next = text[i+order]

        if fragment == text[-order]:
            model[fragment] = {" ": 1}
            return model 

        if fragment not in model:
            model[fragment] = {}

        if next not in model[fragment]:
            model[fragment][next] = 1

        else:
            model[fragment][next] += 1 

def generateText(text, order):
    model = makeModel(text, order)
    output = ""
    lst = []
    for i in range(0, len(text) - order):
        current_frag = text[i:i+order]
        next = model.get(current_frag, None)
        if next == None:
            return output
        for k, v in next.items():
            n = current_frag + k
            lst.append(n) 

    output = " ".join(n)  

    print output
    return output

generateText("In a world of pure imagination", 2)












