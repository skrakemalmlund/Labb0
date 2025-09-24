#Program med grafiskt gränssnitt
from tkinter import *

def inches2cm(inch): 
    """ Tar en längd i inches som indata och returnerar motsvarande längd i cm """
    return 2.54*inch

def konvertera(indata):
    """ Ändrar texten i utmatningsfältet till värdet som funktionen inches2cm returnerar """
    utmatning["text"] = str(inches2cm(indata))

# Sätter konstanter för textstorlek och fonter
STORLEK = 20
TIMES = ("Times", STORLEK)
COURIER = ("Courier", STORLEK)

# Skapar rotfönstret
rot = Tk()
rot.title("Lindas konverteringsprogram")
huvudRam = Frame(rot)
huvudRam.grid()

# Sätter informationstexten överst
info = Label(text = "Konvertera inches till cm", font = TIMES)
info.grid(row = 0, column = 0, padx = 5, pady = 5)

# Skapar den vita inmatningsrutan
inmatning = Entry(font=COURIER, width = 11)
inmatning.grid(row=1, column = 0, padx = 5, pady = 5, sticky = E)
enhet_in = Label(text = "inch", font=TIMES) 
enhet_in.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

# Skapar utmatningsfältet
utmatning = Label(font=COURIER, width = 11)
utmatning.grid(row=2, column = 0, padx = 5, pady = 5, sticky = E)
enhet_ut = Label(text = "cm", font=TIMES)
enhet_ut.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

# Skapar Konvertera-knappen
knapp = Button(text = "Konvertera", font = TIMES, command = lambda: konvertera(float(inmatning.get())))
knapp.grid(row = 3, column = 1, padx = 5, pady = 5)

# Startar slingan som väntar på inmatning...
rot.mainloop()
