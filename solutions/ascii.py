encoded_flag = "IYJ~U4cQ1Q[<mL[(U;`'Ynk/M-i"

result = ""
for i, c in enumerate(encoded_flag):
    key = 6 - i
    result += chr(ord(c) - key)

print(result)  # → le flag !