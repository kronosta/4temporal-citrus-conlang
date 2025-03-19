import re
import sys

chars_hiragana = 'あいうえおかきくけこさしすせそたちってとなにぬねのはひふへほまみめもやゆよらりるれろわんむゔ⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍▣'
chars_katakana = 'アイウエオカキクケコサシスセソタチッテトナニヌネノハヒフヘホマミメモヤユヨラリルレロワンムヴ⌶⌸⌹⌺⌻⌼⌽⌾⌿⍀⍁⍂⍢⍕◈'


s_notated = sys.argv[1]
total_hiragana = ''
total_katakana = ''
for match in re.findall("S\\d\\d?", s_notated):
    num = int(match[1:])
    total_hiragana += chars_hiragana[num - 1]
    total_katakana += chars_katakana[num - 1]

print("Hiragana: " + total_hiragana + "\n")
print("Katakana: " + total_katakana + "\n")
