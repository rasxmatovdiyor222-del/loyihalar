FAYL="data.txt"

def yaratish():
    fayl=input("fayl nomini kiriting")
    fayl=fayl+".txt"
    with open(fayl,"w") as f:
        f.write("")

def yozish():
    with open(FAYL,"a") as f:
        matn=input("Matn kiriting: ")
        f.write("Salom Python\n")
        f.write(matn)


def oqish():
    with open(FAYL,"r") as f:
      n= f.read()
      print(n)



def menu():
 while True:
    print("""
            1-fayl yaratish
            2-faylga yozish
            3-faylni oqih
            4-dasturdan chiqish         
            """)
    buyruq=int(input("buyruqni kiriting: "))
    if buyruq==1:
        yaratish()
    elif buyruq==2:
        yozish()
    elif buyruq==3:
        oqish()
    elif buyruq==4:
        print("dastur toxtadi!")
        break

