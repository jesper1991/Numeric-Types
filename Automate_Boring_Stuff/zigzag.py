import time,sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Wheter increasing or not

try:
    while True: # Main program loop
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.01)

        if indentIncreasing is True:
            # Increase the number of spaces
            indent = indent + 1
            if indent == 20:
                # Change direction
                indentIncreasing = False

        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # Change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
    
