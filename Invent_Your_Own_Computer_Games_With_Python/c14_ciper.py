# Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encript or decript or brute-force a message?')
        mode = input().lower()
        if mode in ['encript', 'e', 'decrept', 'd', 'brute', 'b']:
            return mode
        else:
            print('Enter either "encrept" or "e" or "decript" or "d" or "brute" or "b".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # Symbol not found in SYMBOLS.
            # Just add this symbol without any change.
            translated += symbol
        else:
            # Encript or decript.
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]
    return translated

# ========
# Main
# ========

print('''================================
        ENCRIPTION      
================================''')

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your translated text is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrept', message, key))

