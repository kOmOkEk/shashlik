def h1():
    import os
    from PIL import Image
    os.mkdir('pics')
    for i in os.listdir('forlab9'):

        img = Image.open(i)

        img = img.resize((img.width // 3, img.height // 3))
        img.save(f"forlab9/pics/{k}h1.jpg")

def h2():
    k=1
    import os
    from PIL import Image
    os.mkdir('pics')
    for i in os.listdir('forlab9'):
        if i.endswith('.jpg') or i.endswith('.png'):
            img = Image.open(i)
            img = img.resize((img.width // 3, img.height // 3))
            img.save(r"C:\Users\capit\OneDrive\Документы\1-мд-8\АиП\пересдача\pics\img" + str(k) + ".jpg")
            k+=1

def h3():
    import csv
    itog=0
    print('покупочки:')
    with open('data.csv') as file:
        file = csv.reader(file)
        for row in file:
            info = str(row[0]).split(';')
            name=info[0]
            kolvo=int(info[1])
            cn=int(info[2])
            itog+=kolvo*cn
            print(f"{name} - {kolvo}шт. за {cn}руб.,")
        print(f"Итоговая сумма: {itog}руб.")
h3()