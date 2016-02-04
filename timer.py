import winsound
import time

print """
                                                                                   
88                                                        88                       
88                                                 ,d     88                       
88                                                 88     88                       
88,dPPYba,   8b,dPPYba,   ,adPPYba,  ,adPPYYba,  MM88MMM  88,dPPYba,    ,adPPYba,  
88P'    "8a  88P'   "Y8  a8P_____88  ""     `Y8    88     88P'    "8a  a8P_____88  
88       d8  88          8PP"""""""  ,adPPPPP88    88     88       88  8PP"""""""  
88b,   ,a8"  88          "8b,   ,aa  88,    ,88    88,    88       88  "8b,   ,aa  
8Y"Ybbd8"'   88           `"Ybbd8"'  `"8bbdP"Y8    "Y888  88       88   `"Ybbd8"'  
                                                                                   
                                                                                  
"""                                                                                

def timer(seconds): 
    elapsed = 0
    while elapsed < seconds:
    	print "\tSeconds passed: %d\r" % elapsed,
    	time.sleep(1)
    	elapsed += 1
    print "\tYour meditation is complete."

minutes = int(raw_input("\tHow many minutes would you like to meditate? >> "))

seconds = minutes*60

count = 5
while count > 0:
	print "\tTimer starting in %d seconds.\r" % count,
	time.sleep(1)
	count -= 1
print "\tTimer starting.                   "

timer(seconds)

winsound.PlaySound('end.wav', winsound.SND_FILENAME)