from PIL import Image
from src.constants import CROP_SIZE_X, SIZE_RATIO, GREYSCALE_MAX, NUM_CHARS

CROP_SIZE_Y = round(CROP_SIZE_X * SIZE_RATIO)

def createAsciiArt(path):
    image = getImage(path)
    f = open("ascii_art.txt", 'w')

    for y in range(0, image.height - CROP_SIZE_Y, CROP_SIZE_Y):
        for x in range(0, image.width - CROP_SIZE_X, CROP_SIZE_X):
            section = getImageSection(image, x, y, x + CROP_SIZE_X, y + CROP_SIZE_Y)
            brightness = shade(section)
            char = getChar(brightness)
            f.write(char)
        
        f.write("\n")
    
    f.close()

def getImage(path):
    image = Image.open(path)

    width, height = image.size
    width = width - (width % CROP_SIZE_X)
    height = height - (height % CROP_SIZE_Y)
    
    image_resized = image.crop((0, 0, width, height))
    image_greyscale = image_resized.convert("L")
    
    return image_greyscale
    
def getImageSection(image, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    cropped_image = image.crop((top_left_x, top_left_y, bottom_right_x, bottom_right_y))

    return cropped_image

def shade(image):
    pixel_total = 0

    for y in range(0, image.height):
        for x in range(0, image.width):
            pixel_total += image.getpixel((x,y))

    mean_brightness = pixel_total // (image.height * image.width)

    return mean_brightness

def getChar(brightness):
    char_value = round((brightness / GREYSCALE_MAX) * NUM_CHARS)
    char = ascii_light_to_dark[char_value]

    return char

ascii_light_to_dark = "@&%QWNM0gB$#DR8mHXKAUbGOpV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}C{iF|(7J)vTLs?z/*cr!+<>;=^,_:'-.' "