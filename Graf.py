import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """ Funktionen som ska plottas """
    y = np.cos(x)
    return y

# Skapa alla x-värden: 999 punkter från 0 till 2*pi
x = np.linspace(0, 4*np.pi, 999)

# Beräkna funktionsvärden för alla dessa x-värden
y = f(x)

# Skapa grafen
plt.plot(x, y)

# Lägg till en titel och text för axlarna
plt.title('Skrake och Adams plot')
plt.xlabel('x')
plt.ylabel('cos(x)')

# Visa grafen
plt.show()
