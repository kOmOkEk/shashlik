from PIL import Image, ImageDraw, ImageFont
def g1():
    p = Image.open('img111.jpg')
    p2 = p.crop((0, 300, 450, 800))
    p2.show()
    p2.save('p2.JPG')

def g2():
    otkr = {
        '8 марта' : 'img8.jpg',
        '23 февраля' : 'img23.jpg',
        'новый год' : 'img01.jpg',
        '14 февраля' : 'img14.jpg',
        'день рождения' : 'img666.jpg'
    }
    o = []
    prazd = input('Введите название праздника:')    #no pics stored, try creating some using g3()
    if prazd in otkr:
        card = Image.open(otkr[prazd])
        card.show()
    else:
        print('Открытки к данному празднику нет')

def g3():
    name = input('Введите имя того, кого вы хотите поздравить?') + ', поздравляю!'
    p = Image.open('img111.jpg')
    print(p.size)
    p2 = p.crop((0, 300, 450, 800))
    draw = ImageDraw.Draw(p2)
    font = ImageFont.truetype('arial.ttf',36)
    draw.text((20,20), name, font=font, fill=(0,0,0))
    p2.save('p3.PNG')
    p2.show()
