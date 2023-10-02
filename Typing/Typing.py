from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)

#with open("countries.txt", "r") as country_list:
    #countries = country_list.read().split()
#print (countries[69])
#i = 0
#while i <= len(countries):
for char in "From time to time I heard some vague account of his doings: of his summons to Odessa in the case of the Trepoff murder, of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee, and finally of the mission which he had accomplished so delicately and successfully for the reigning family of Holland.":
    keyboard.press(char)
    keyboard.release(char)
    #time.sleep(0.01)
