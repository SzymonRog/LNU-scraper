def thousandCaesarCipher(message, k):
    k = k % 26               # normalize shift (handles negative too)
    result = ""
    
    for char in message:
        if 'a' <= char <= 'z':
            # lowercase letter → shift within a-z
            result += chr( (ord(char) - ord('a') + k) % 26 + ord('a') )
            
        elif 'A' <= char <= 'Z':
            # uppercase letter → shift within A-Z
            result += chr( (ord(char) - ord('A') + k) % 26 + ord('A') )
            
        else:
            # preserve everything else (space, punctuation, numbers...)
            result += char
            
    return result