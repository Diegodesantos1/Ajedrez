import random
import sys
def numeros():
    numero1= random.randint(1,4)
    numero2= random.randint(1,4)

    if numero1 or numero2 == 1:
        print ("Viti")
    elif numero1 or numero2 == 2:
        print("Rumen")
    elif numero1 or numero2 == 3:
        print("DIego")
    elif numero1 or numero2 == 4:
        print("LLoren")
    else:
        sys.exit

numeros()
