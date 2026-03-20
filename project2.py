dog = 0
cat = 0
none = 0 
print("")
print("")
print("")
print("This is a quiz PLEEEAASSEEE anwser with the letter listed not the answer")
input("")
print("")
anwser1 = input("Do you prefer A: Napping or Staying in bed , B: Walking or running, C: Working or gaming? ")
if anwser1 == "A" or anwser1 == "a":
    cat += 2
elif anwser1 == "B" or anwser1 == "b":
    dog += 2
elif anwser1 == "C" or anwser1 == "c":
    none == 2
else :
    print("Please type the letter corresponding to your answer")
    input("")
    anwser1 = input("Do you prefer A: Napping or Staying in bed , B: Walking or running, C: Working or gaming ")
    if anwser1 == "A" or anwser1 == "a":
        cat += 2
    elif anwser1 == "B" or anwser1 == "b":
        dog += 2
    elif anwser1 == "C" or anwser1 == "c":
        none == 2
print("")
anwser2 = input("Are you A: social, B: like to be alone, C: a mix of both? ")
if anwser2 == "A" or anwser2 == "b":
    dog += 2
elif anwser2 == "B" or anwser2 == "b":
    none += 2
elif anwser2 == "C" or anwser2 == "c":
    cat+= 2
else :
    print("Please type the letter corresponding to your answer")
    input("")
    anwser2 = input("Are you A: social, B: like to be alone, C: a mix of both? ")
    if anwser2 == "A" or anwser2 == "b":
        dog += 2
    elif anwser2 == "B" or anwser2 == "b":
        none += 2
    elif anwser2 == "C" or anwser2 == "c":
        cat+= 2
print("")
anwser3 = input("Do you have A:small home or apartment, B: I live in a cardboard box, C: large house or apartment with yard? ")
if anwser3 == "A" or anwser3 == "a":
    cat += 2
if anwser3 == "B" or anwser3 == "b":
    none += 2 
if anwser3 == "C" or anwser3 == "c":
    dog += 2
else :
    print("Please type the letter corresponding to your answer")
    input("")
    anwser3 = input("Do you have A:small home or apartment, B: I live in a cardboard box, C: large house or apartment with yard? ")
    if anwser3 == "A" or anwser3 == "a":
        cat += 2
    if anwser3 == "B" or anwser3 == "b":
     none += 2 
    if anwser3 == "C" or anwser3 == "c":
        dog += 2
print("")
anwser4 = input("How Much money do you make? A:50000000000 million dollars, B:100,000 dollars, C: Zero dollars? ")
if anwser4 == "C" or anwser4 == "c":
    none += 2
elif anwser4 == "A" or anwser4 == "a" or anwser4 == "b" or anwser4 == "B":
    dog += 2
    cat += 2
else :
    print("Please type the letter corresponding to your answer")
    input("")
    anwser4 = input("How Much money do you make? A:50000000000 million dollars, B:100,000 dollars, C: Zero dollars? ")
    if anwser4 == "C" or anwser4 == "c":
        none += 2
    elif anwser4 == "A" or anwser4 == "a" or anwser4 == "b" or anwser4 == "B":
        dog += 2
        cat += 2
print("")
anwser5 = input("What is your favorite animal... A: Dog, B: Cat, C:not listed? ")
if anwser5 == "A" or anwser5 == "a":
    dog += 2
elif anwser5 == "B" or anwser5 == "b":
    cat += 2
elif anwser5 == "C" or anwser5 == "c":
    none+= 2
else :
    print("Please type the letter corresponding to your answer")
    input("")
    anwser2 = input("What is your favorite animal... A: Dog, B: Cat, C:not listed? ")
    if anwser5 == "A" or anwser5 == "a":
        dog += 2
    elif anwser5 == "B" or anwser5 == "b":
        cat += 2
    elif anwser5 == "C" or anwser5 == "c":
        none += 2


print("READY FOR UR RESULTS????????!?!!?!?!?")
input("")
if dog >= cat and dog >= none:
    print("U shoud get a pupppyyyyy!!!")
elif cat >= dog and cat >= none: 
    print("GETT a KITTYYY CAAATTT")
elif none >= dog and none >= cat: 
    print(r"DO NOT get a pet... srryy :(")
