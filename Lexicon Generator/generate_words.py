import sys
import random

already_generated = []
characters = [
('あ','ア'),
('い','イ'),
('う','ウ'),
('え','エ'),
('お','オ'),
('か','カ'),
('き','キ'),
('く','ク'),
('け','ケ'),
('こ','コ'),
('さ','サ'),
('し','シ'),
('す','ス'),
('せ','セ'),
('そ','ソ'),
('た','タ'),
('ち','チ'),
('っ','ッ'),
('て','テ'),
('と','ト'),
('な','ナ'),
('に','ニ'),
#('ぬ','ヌ'),
#('ね','ネ'),
('の','ノ'),
('は','ハ'),
('ひ','ヒ'),
('ふ','フ'),
('へ','ヘ'),
('ほ','ホ'),
('ま','マ'),
('み','ミ'),
('め','メ'),
('も','モ'),
('や','ヤ'),
('ゆ','ユ'),
('よ','ヨ'),
('ら','ラ'),
('り','リ'),
('る','ル'),
('れ','レ'),
('ろ','ロ'),
('わ','ワ'),
('ん','ン'),
('む','ム'),
('ゔ','ヴ'),
('⊀','⌶'),
('⊁','⌸'),
('⊂','⌹'),
('⊃','⌺'),
('⊄','⌻'),
('⊅','⌼'),
('⊆','⌽'),
('⊇','⌾'),
('⊈','⌿'),
('⊉','⍀'),
('⊊','⍁'),
('⊋','⍂'),
('⊌','⍢'),
('⊍','⍕'),
('▣','◈'),
]

def random_word():
  total_hiragana = ""
  total_katakana = ""
  for i in range(random.randint(3,9)):
    rand_index = random.randint(0, len(characters) - 1)
    total_hiragana += characters[rand_index][0]
    total_katakana += characters[rand_index][1]
  return (total_hiragana, total_katakana)

random.seed()
if len(sys.argv) < 3:
  print("Usage: python generate_words.py [input-file] [output-file]")
else:
  input_file_path = sys.argv[1];
  output_file_path = sys.argv[2];

  input_file = open(input_file_path, 'r', encoding="utf-8")
  output_file = open(output_file_path, 'w', encoding="utf-8")

  hiragana = ""
  for word in input_file:
    word = word.strip()
    (hiragana, katakana) = random_word()
    while hiragana in already_generated:
      (hiragana, katakana) = random_word()
    already_generated += [hiragana]
    output_file.write(word + "\t" + hiragana + "\t" + katakana + "\n")
  input_file.close()
  output_file.close()
    
    