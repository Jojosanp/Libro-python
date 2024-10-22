

import random


def guessing_game ():
 a=random.randint(0,100)

 b= a + 5

 d= a - 5

 #Esto permite que b y d se mantenga en el rango de 0 y 100
 if b not in range(0,100):
   b=b-5
 else:
    c=b

 if d not in range(0,100):
   d=d+5
 else:
     d=d

 valores_1= list(range(a,b))
 valores_2= list(range(d,a))
 valores= valores_2 + valores_1

#para saber que tan cerca se esta del numero
 primer_elemento=valores_2[0]
 ultimo_elemento=valores_1[-1]


 while True:
        numero = int(input("Introduce un número: "))

        if numero < primer_elemento:
            print("Demasiado bajo")
        elif numero > ultimo_elemento:
            print("Demasiado alto")
        elif numero == a:
            print("¡Correcto!")
            break


guessing_game()





