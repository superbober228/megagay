
popa = 'piska.txt '

with open (popa, "r", encoding= "UTF-8") as file:
    for line in file:
        print (line)


revo = input("хто сочинив цей дотареп")
with open (popa, "a", encoding= "UTF-8") as file:
    file.write(f"({revo})\n")

while True:
    gay = input ("цитатку стетхама добавиш (так/ні)")
    gay = gay.lower()
    if gay == "так":
        pivo = input ("введи цитатку стетхама")
        revo = input ("автора ввдеи ")
        file = open (popa, "a", encoding= "UTF-8")
        file.write(f"({pivo})\n({revo})\n")
        file.close()
    else:
        break
with open (popa, "r", encoding= "UTF-8") as file:
    for line in file:
        print(line)