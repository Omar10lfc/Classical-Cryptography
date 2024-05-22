def classical_cryptography(text, key) -> str:
    
    '''''''''' 
      This function implements the Classic Cryptography encryption method.
      It takes a text and a key as input parameters and returns the encrypted message and 
      decrypt any text by passing a negative key value.
      
    '''''''''''
    
    result = ''
    for char in text:
        if char.isupper():
            result += chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        elif char.islower():
            result += chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        else:
            result += char
    return result

if __name__ == '__main__':
    text = str(input('Enter the text you want to encrypt or decrypt:')) 
    key = int(input('Enter a number between -25 and 25 (positive for encryption, negative for decryption):'))
    result = classical_cryptography(text, key)
    print(result)


