# Defines the unicode characters and print (UTF - 8, UTF - 16, UTF - 32)
# Go to start --> type character map to know the unicode symbols of every character
# https://www.pythonsheets.com/notes/python-unicode.html
# J --> U + 004A, Utf - 8 Dec : 74
# Ö --> Utf - 8 : 0xc3 0x96(Dec : 195 150), UTF -16 : 0x00D6 (Dec :214) 
# S --> U + 0053, Utf - 8 Dec : 83
# ï -->  Utf - 8 : 0xc3 0xAF(Dec : 195 175), UTF -16 : 0x00EF (Dec :239)
# G --> U + 0047, Utf - 8 Dec : 71
# A --> U + 0041, Utf - 8 Dec : 65
# ASCII - 7 bits , UTF-8 --> 8bits, UTF-16 --> 16 bits, UTF-32 --> 32 bits
# ord() --> function to print the unicode for the given character
# chr() --> function to print the character for the given unicode

print(ord("J"))
print(chr(74))
print(ord("Ö"))
print(chr(214))
print(ord("S"))
print(chr(83))
print(ord("ï"))
print(chr(239))
print(ord("G"))
print(chr(71))
print(ord("A"))
print(chr(65))

print("Define the Unicode - 16 as strings and print \n")
s = "JÖSïGA"
print(type(s))
print([ord(c) for c in s])
print([_c for _c in s])
b = s.encode('utf-16')
print([_c for _c in b])
print(b)
print([_c for _c in b])
c = b.decode('utf-16')
print(c)
print([_c for _c in c])

print("Define the Unicode - 8 as strings and print \n")
s = "JÖSïGA"
# J --> U + 004A, Utf - 8 Dec : 74
# Ö --> Utf - 8 : 0xc3 0x96(Dec : 195 150), UTF -16 : 0x00D6 (Dec :214) 
# S --> U + 0053, Utf - 8 Dec : 83
# ï -->  Utf - 8 : 0xc3 0xAF(Dec : 195 175), UTF -16 : 0x00EF (Dec :239)
# G --> U + 0047, Utf - 8 Dec : 71
# A --> U + 0041, Utf - 8 Dec : 65
print(type(s))
print([_c for _c in s])
b = s.encode('utf-8')
print([_c for _c in b])
print(b)
print([_c for _c in b])
c = b.decode('utf-8')
print(c)
print([_c for _c in c])

# Printing the unicode characters by name (UTF-16)
print(u"\N{DAGGER}")
print(u"\N{SECTION SIGN}")
print(u"\N{CENT SIGN}")
print(u"\N{Latin Capital Letter J}")
print(u"\N{Latin Capital Letter O with Diaeresis}")
print(u"\N{Latin Capital Letter S}")
print(u"\N{Latin Capital Letter I with Diaeresis}")
print(u"\N{Latin Capital Letter G}")
print(u"\N{Latin Capital Letter A}")

# Printing the unicode characters by value (UTF-16)
print(u"\u004A")
print(u"\u00D6")
print(u"\u0053")
print(u"\u00EF")
print(u"\u0047")
print(u"\u0041")

# Printing the unicode characters by value (UTF-32)
print(u"\U0000004A")
print(u"\U000000D6")
print(u"\U00000053")
print(u"\U000000EF")
print(u"\U00000047")
print(u"\U00000041")




