import os
import time
import random
import sys

class message(str):
    def __new__(cls, text, speed):
        self = super(message, cls).__new__(cls, text)
        self.speed = speed
        self.y = -1 * len(text)
        self.x = random.randint(0, display().width - 1)  # Asegúrate de que x esté dentro del rango
        self.skip = 0
        return self
 # definicion de move . funcion
    def move(self):
        if self.speed > self.skip:
            self.skip += 1
        else:
            self.skip = 0
            self.y += 1
# definicion de display f
class display(list):
    def __init__(self):
        self.height, self.width = os.get_terminal_size()  # Obtener el tamaño de la terminal
        self[:] = [' ' for _ in range(self.height * self.width)]

    def set_vertical(self, x, y, string):
        string = string[::-1]  # Invertir el string
        if x < 0:
            x = self.width + x
        if x >= self.width:
            x = self.width - 1
        if y < 0:
            string = string[abs(y):]
            y = 0
        if y + len(string) > self.height:
            string = string[0:self.height - y]
        if y >= self.height:
            return
        start = y * self.width + x
        length = self.width * (y + len(string))
        step = self.width
        self[start:length:step] = string

    def __str__(self):
        return ''.join(self)

i_message = input("Input a message: ")  # Cambiado a input para Python 3
messages = [message(i_message, random.randint(1, 5))]

for t in range(1000):  # Cambiado a range para Python 3
    messages.append(message(i_message, random.randint(1, 5)))
    d = display()
    for text in messages:
        d.set_vertical(text.x, text.y, text)
        text.move()
    sys.stdout.write(str(d))
    sys.stdout.flush()
    del d
    time.sleep(0.1)