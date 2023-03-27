def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans
plaintext = "The quick brown fox jumps over the lazy dog"
n = 3
print("Cipher Text is : " + encrypt_text(plaintext,n))
