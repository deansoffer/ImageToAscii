from PIL import Image
import math


def saveFile(text):
    with open('out.html', 'w') as f:
        print(text, file=f)  # Python 3.x


def saveHTML(ascii):
   txt = '<html>' \
            '<head>' \
            '<body bgcolor="white">' \
            '<div style="color:black;font-size:9px; letter-spacing: 2px;font-family: monospace;">'
   txt += ascii.replace(' ', '&nbsp;').replace("-", "<br>")
   txt += '</div></body>'
   saveFile(txt)

def main():
    asciss = ['.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', ' ']
    im = Image.open('./surff.jpg').convert("L").resize((90, 90), Image.NEAREST)
    c = ""
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixel = im.getpixel((j, i))
            strength = math.floor(len(asciss) * (pixel / 255)) - 1
            print(asciss[strength], end="")
            c += asciss[strength]
        c += "-"
        print()
    # im.show()
    saveHTML(c)

if (__name__  ==  "__main__"):
    main()