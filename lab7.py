def f1():
    from PIL import Image
    a = "cat.jpg"
    with Image.open(a) as img:
        img.load()
    img.show()
    w, h = img.size
    format = img.format
    mode = img.mode
    print('Ширина: ',w)
    print('Высота: ',h)
    print('Формат: ', format)
    print('Цветовой мод: ',mode)

def f2():
    from PIL import Image
    b = 'cat.jpg'
    with Image.open(b) as img:
        img.load()
    img2 = img.resize((img.width //3, img.height //3))
    img2.save('cat2.jpg')

def f3():
    from PIL import Image, ImageFilter
    for i in range(1, 6):
        i = str(i)
        img = Image.open(f"7lab/{i}.jpg")
        img = img.filter(filter=ImageFilter.EMBOSS)
        img.save(f"7lab/edited/{i}f3.jpg")

def f4():
    from PIL import Image, ImageDraw, ImageFont

    def add_watermark(input_image_path, output_image_path, watermark_text):
        original_image = Image.open(input_image_path).convert("RGBA")

        watermark = Image.new("RGBA", original_image.size)

        draw = ImageDraw.Draw(watermark)

        font_size = 60
        font = ImageFont.truetype("arial.ttf", font_size)

        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        text_position = (original_image.width - text_width - 10, original_image.height - text_height - 10)

        draw.text(text_position, watermark_text, fill=(255, 255, 255, 128), font=font)

        combined = Image.alpha_composite(original_image, watermark)  # чтобы учесть прозрачность использую это

        combined.show()
        combined = combined.convert("RGB")
        combined.save(output_image_path, "JPEG")

    input_image = "7lab/Cirno.png"  # путь к изображению
    output_image = "7lab/Cirno_watermarked.png"  # куда сохранять, под каким именем
    watermark_text = "Сырники"  # текст вотермарки

    add_watermark(input_image, output_image, watermark_text)
f4()