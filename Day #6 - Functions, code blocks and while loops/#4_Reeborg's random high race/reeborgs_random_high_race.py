print('''
      
Paste the following code into: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        turn_left()

while not at_goal():
    jump()

''')

# English explanation:

# Always move forward if the front is clear. 
# As soon as you face the hurdle, the else statement will turn you left. 
# Then the front is clear again and you can round the hurdle no matter the length of the hurdle - because right is clear statement will turn you around the hurdle. 
# When you between the hurdles you move forward until the front is clear and turn left the first time when you face with the ground and turn left second time when you face with the next hurdle.

# Explicación en español:

# Siempre avanza hacia adelante si el frente está despejado. 
# Tan pronto como te encuentres con el obstáculo, la declaración else te hará girar a la izquierda. 
# Luego, cuando el frente esté despejado nuevamente, podrás rodear el obstáculo sin importar su longitud, porque la declaración right is clear te girará alrededor del obstáculo. 
# Cuando te encuentres entre los obstáculos, avanzarás hasta que el frente esté despejado y girarás a la izquierda la primera vez que te encuentres con el suelo, y girarás a la izquierda por segunda vez cuando te encuentres con el próximo obstáculo.