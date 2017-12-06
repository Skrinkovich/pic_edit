from PIL import Image, ImageFilter, ImageChops,ImageOps, ImageDraw, ImageEnhance
import random

def BLUR(img1):
    img1 = img1.filter(ImageFilter.BLUR)
    img1.show()
def CONTOUR(img2):
    img2 = img2.filter(ImageFilter.CONTOUR)
    img2.show()
def DETAIL(img3):
    img3 = img3.filter(ImageFilter.DETAIL)
    img3.show()
def EDGE_ENHANCE(img4):
    img4 = img4.filter(ImageFilter.EDGE_ENHANCE)
    img4.show()
def EMBOSS(img5):
    img5 = img5.filter(ImageFilter.EMBOSS)
    img5.show()
def FIND_EDGES(img6):
    img6 = img6.filter(ImageFilter.FIND_EDGES)
    img6.show()
def SMOOTH(img7):
    img7 = img7.filter(ImageFilter.SMOOTH)
    img7.show()
def SHARPEN(img8):
    img8 = img8.filter(ImageFilter.SHARPEN)
    img8.show()

def sad(img9):
    area=(img9.size)
    if area[1]>=area[0]:
        image2 = Image.open('pics/pic1.jpg')
        image2=ImageOps.fit(image2, area)
        newi=ImageChops.add(img9, image2, scale=3.7, offset=20)
        newi.show()
    else:
        image2 = Image.open('pics/pic2.jpg')
        image2=image2.resize(area)
        newi=ImageChops.add(img9, image2, scale=3.7, offset=20)
        newi.show()
    #newi.save("C:/Users/wital/Desktop/i.jpg")

def worhl(imageW):
    areasmall = (imageW.size)
    areabig = (areasmall[0]*2, areasmall[1]*2)
    finale = Image.new("RGB", areabig, 0)
    g = ImageOps.grayscale(imageW)
    g = ImageOps.posterize(g, 2)
    bbb1 = (155,5,175)
    www1 = (28,221,32)
    bbb2 = (10,1,178)
    www2 = (224,232,0)
    bbb3 = (27,111,186)
    www3 = (226,117,0)
    bbb4 = (173,0,0)
    www4 = (0,202,216)
    a = ImageOps.colorize(g, bbb1, www1)
    b = ImageOps.colorize(g, bbb2, www2)
    c = ImageOps.colorize(g, bbb3, www3)
    d = ImageOps.colorize(g, bbb4, www4)
    finale.paste (a, None)
    finale.paste(b, (areasmall[0],0))
    finale.paste(c, (0, areasmall[1]))
    finale.paste(d, areasmall)
    finale.show()

def noise(imageN):
    # imageNN = imageN.copy()
    width = imageN.size[0]
    height = imageN.size[1]
    draw = ImageDraw.Draw(imageN)
    pix = imageN.load()
    # factor = int(input('factor: '))
    factor = 75
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    imageN.show()

def vintage(imageV):
    imageVV = imageV.copy()
    draw = ImageDraw.Draw(imageV)
    width = imageV.size[0]
    height = imageV.size[1]
    pix1 = imageV.load()
    for i in range(width):
        for j in range(height):
            a = pix1[i, j][0] + random.randint(100, 160)
            b = pix1[i, j][1] + random.randint(60, 100)
            c = pix1[i, j][2] + random.randint(20, 50)
            draw.point((i, j), (a, b, c))
    newV = ImageEnhance.Color(imageV).enhance(0.7)
    newV.show()
    # return imageVV

def glitch(imageG):
    r, g, b = (imageG.split())
    g = ImageChops.offset(g,10,10)
    b = ImageChops.offset(b,-20,20)
    newG = Image.merge("RGB", (r, g, b))
    newG.show()


def mem(img):
    command = input("Есть такие мемчики:\n think\n success\n loser\n stupid\n wait\n session\n sad\n какой хотите?)\n")
    img = img
    x, y = img.size
    if command == "think":
        fin_temp = Image.open("pics/mems/finger.jpg")
        fin_temp = fin_temp.resize(img.size)
        img = Image.blend(img, fin_temp, 0.5)
        img.show()
    elif command == "success":
        Ir_temp = Image.open("pics/mems/Iron_man.jpg")
        Ir_temp = Ir_temp.resize((x, y))
        img = Image.blend(img, Ir_temp, 0.5)
        img.show()
    elif command == "loser":
        los_temp = Image.open("pics/mems/loser.jpg")
        los_temp = los_temp.resize((x, y))
        img = Image.blend(img, los_temp, 0.5)
        img.show()
    elif command == "stupid":
        rob_temp = Image.open("pics/mems/robert_downey_jr.jpg")
        rob_temp = rob_temp.resize((x, y))
        img = Image.blend(img, rob_temp, 0.5)
        img.show()
    elif command == "wait":
        wait_temp = Image.open("pics/mems/wait.jpg")
        wait_temp = wait_temp.resize((x, y))
        img = Image.blend(img, wait_temp, 0.5)
        img.show()
    elif command == "session":
        army_temp = Image.open("pics/mems/военком-захаров-оригинал.jpg")
        army_temp = army_temp.resize((x, y))
        img = Image.blend(img, army_temp, 0.5)
        img.show()
    elif command == "sad":
        sad(img)

def filter(image):
    command = input("Есть такие фильтры:\n worhl\n noise\n vintage\n glitch\n")
    image = image
    if command == "worhl":
        worhl(image)
    elif command == "noise":
        noise(image)
    elif command == "vintage":
        vintage(image)
    elif command == "glitch":
        glitch(image)

image = input("Введите путь до фото, которое нужно обработать: ")
image = Image.open(str(image))
# image = Image.open("pics/house.jpg")
image0 = image.copy()
image00 = image.copy()
c = input("Введите mem, filter или all: ")
if c == "mem":
    mem(image)
elif c == "filter":
    filter(image)
elif c == "all":
    BLUR(image)
    CONTOUR(image)
    DETAIL(image)
    EDGE_ENHANCE(image)
    EMBOSS(image)
    FIND_EDGES(image)
    SMOOTH(image)
    SHARPEN(image)
    worhl(image)
    noise(image)
    vintage(image0)
    glitch(image00)
    mem(image0)