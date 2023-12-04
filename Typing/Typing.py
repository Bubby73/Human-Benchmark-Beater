from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)

#with open("countries.txt", "r") as country_list:
    #countries = country_list.read().split()
#print (countries[69])
#i = 0
#while i <= len(countries):
for char in "It's impossible to think of flamingos without picturing a bright splash of pink. But where do they get their signature color? The answer lies in their diet. The flamingo feeds mainly on shrimps and insects, scraping them from the mud with its hook-shaped beak. These can contain a pigment that gives its feathers that particular shade of pink. Their shade changes depending on what they feed on, with the American flamingo being one of the brightest and flashiest.":
    keyboard.press(char)
    keyboard.release(char)
    #time.sleep(0.01)
