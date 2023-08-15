from PIL import Image
import math

width = int(input("poe um numero pequeno pfv (quantidade de bits)\n:"))
height = 2**width

image_bin = Image.new(mode="RGB", size=(width,height), color=(255,255,255))

def dectobin(num):
    listadigitos = []
    dividido = num
    for i in range(image_bin.width):
        if dividido%2 == 0:
            listadigitos.insert(0,0)
        else:
            listadigitos.insert(0,1)
        dividido = math.floor(dividido/2)
    return listadigitos

for i in range(image_bin.height):
    altura_atual = i
    largura_atual = 0
    for i in dectobin(i):
        if i == 1: 
            image_bin.putpixel( xy = (largura_atual,altura_atual),value=(0,0,0))
        largura_atual+=1


image_bin.show()