import serial

serialConnection = serial.Serial('/dev/ttyACM0', 9600)

characterEntered = ''

while characterEntered != 'q':
    characterEntered = rawInput("Enter f, b, a, d, or q to quit: ")
    print "Character entered: ", characterEntered

    if characterEntered == 'q':
        break
    
    else if characterEntered == 'f':
        serialConnection.write('f')
        
    else if characterEntered == 'b':
        serialConnection.write('b')
        
    else if characterEntered == 'a':
        serialConnection.write('a')
        
    else if characterEntered == 'd':
        serialConnection.write('d)
