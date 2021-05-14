
# A Morse code encoder/decoder
# Morse code chart using Dictionary
MORSE_CODE = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
               'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
               'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
               '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
               '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-',
               '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ':' ' }

MORSE_KEYS = list(MORSE_CODE.keys())
MORSE_VALUES = list(MORSE_CODE.values())

def print_intro():
    print('Welcome to Wolmore')
    print('This program encodes and decodes Morse code.')
    
def get_input():        
    mode = input('Would you like to encode (e) or decode (d): ')
    while mode!='e' and mode!='d':
        print('Invalid input')
        mode = input('Would you like to encode (e) or decode (d): ')
    if mode == 'd':
        msg = input('What message you like to decode: ')
    elif mode == 'e':
        msg = input('What message you like to encode: ')
        msg = msg.upper()
    return mode, msg
  
def encode(message):
    enmsg = ''
    for i in message:
        if i != ' ':
            enmsg += MORSE_CODE[i] + ' '
        else:
            enmsg += ' '
    return enmsg

def decode(message):
    demsg = ''
    message = message.split()
    for i in message:
        demsg = demsg + MORSE_KEYS[MORSE_VALUES.index(i)]
    return demsg

def main():   
    mod,message = get_input()
    if mod == 'e':
         result1 = encode(message)
         print(result1)
    else:
         result2 = decode(message)
         print(result2)

if __name__ == '__main__':
    print_intro()
    main()
    acode = input('Would you like to encode/decode another message? (y/n): ')
    while acode!='y' and acode!='n':
        print('Invalid Input')
        acode = input('Would you like to encode/decode another message? (y/n): ')
    while acode == 'y':
        main()
        acode = input('Would you like to encode/decode another message? (y/n): ')
    if acode == 'n':
        print('Thanks for  using the program, goodbye!')
        
        
