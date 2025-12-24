matn = "Python dasturlash tilini organish juda foydali"

sozlar = matn.split()
eng_uzun = sozlar[0]

for soz in sozlar:
    if len(soz) > len(eng_uzun):
        eng_uzun = soz

print("Eng uzun so‘z:", eng_uzun)
