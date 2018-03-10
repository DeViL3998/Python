temperature=-3.7                    #takes the float value of temperature
celsius= True                       #takes the boolean value of celsius

if celsius == True:                 #checks whether the value is in celsius or fahrenheit
    if temperature<=0:              #checks value of temperature
        print('Freezing!')          #prints output

    else print('Not Freezing')      #prints output

else :                              #runs if temperature is in fahrenheit
    if temperature<=32:             #checks value of temperature
        print('Freezing')           #prints output
    else print('Not Freezing')      #prints output
