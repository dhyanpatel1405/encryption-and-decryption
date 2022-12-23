def encrypt(text, shift):
  encrypted_text = ""
  for ch in text:
    if ch.isalpha():
      shift_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
      encrypted_text += shift_ch
    else:
      encrypted_text += ch
  return encrypted_text

def decrypt(text, shift):
  decrypted_text = ""
  for ch in text:
    if ch.isalpha():
      shift_ch = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
      decrypted_text += shift_ch
    else:
      decrypted_text += ch
  return decrypted_text

# Test the functions
text = "hello"
shift = 3
encrypted_text = encrypt(text, shift)
print(encrypted_text)  # Output: "khoor"
decrypted_text = decrypt(encrypted_text, shift)
print(decrypted_text)  # Output: "hello"
