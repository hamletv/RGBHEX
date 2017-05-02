'''calculator to convert RGB values to Hex values and vice-versa'''

def rgb_hex(): #function converts RGB to Hex
    invalid_msg = 'Error, invalid values entered.'

    red = int(raw_input('Enter a value for Red:')) #convert red string (number) to interger
    if red < 0 or red > 255:
        print invalid_msg
        return

    green = int(raw_input('Enter a value for Green:')) #convert red string (number) to interger
    if green < 0 or green > 255:
        print invalid_msg
        return

    blue = int(raw_input('Enter a value for Blue:')) #convert red string (number) to interger
    if blue < 0 or blue > 255:
        print invalid_msg
        return

    val = (red << 16) + (green << 8) + blue #red value shifted left by 16 bits. 16 bits open/empty, 8 taken by green value, 8 left for blue value.
    print '%s' % (hex(val)[2:]).upper() #hex value first 2 index val sliced

def hex_rgb(): #function converts Hex value to RGB value
    hex_val = raw_input('Enter your hex value:')
    if len(hex_val) != 6: #hex values are 6 characters long
      print 'An invalid value was entered.'
      return
    else:
      hex_val = int(hex_val, 16) #hex_val converted to base 16/radix integer

    two_hex_digits = 2 ** 8 #2 ** 8 = 256
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print 'Red: %s, Green: %s, Blue: %s' % (red, green, blue)

def convert():
    while True:
      option = raw_input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:')
      if option == '1':
        print 'RGB to Hex...'
        rgb_hex() #call function to convert rgb to hex
      elif option == '2':
        print 'Hex to RGB...'
        hex_rgb() #call function to convert hex to rgb
      elif option == 'X' or option == 'x':
        break
      else:
        print 'Error.'

convert()
