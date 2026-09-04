#import random
#num = random.randint(1,10)
#print(num)
import emoji
import emoji

# Testando diferentes emojis usando os códigos da lista
#https://github.com/carpedm20/emoji/blob/d26c675190a6b6c0edee959d7b896721a9c3641d/emoji/unicode_codes/emoji_pt.json
#https://github.com/carpedm20/emoji/blob/d26c675190a6b6c0edee959d7b896721a9c3641d/emoji/unicode_codes/emoji_pt.json
#print(emoji.emojize("Olá mundo :earth_americas:"))
#print(emoji.emojize("Python é fantástico! :snake:"))
#print(emoji.emojize("Deu tudo certo! :thumbs_up: :party_popper:"))
#print(emoji.emojize(":dog:"))

for codigo, dados in emoji.EMOJI_DATA.items():
    print(f"{codigo} -> {dados['pt']}")

