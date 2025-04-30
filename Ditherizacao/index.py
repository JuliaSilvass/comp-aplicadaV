import cv2 as cv 
import numpy as np
import os 
from PIL import Image

# Verifica se o caminho da imagem existe
caminho_img = r"comp-aplicadaV/Ditherizacao/nicolas_cage.jpeg"
if not os.path.exists(caminho_img):
    print("Caminho da imagem não encontrado.")
    exit()

# Carrega a imagem 
img = cv.imread(caminho_img)
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Exibe e salva a imagem
cv.imshow('Imagem em Cinza', img_cinza)
cv.imwrite('imagem_cinza.png', img_cinza)

# # acessa a matriz de pixels da imagem
# matriz_pixels_blue = img[:, :, 0]
# # print("Matriz de pixels da imagem (blue):", matriz_pixels_blue)

# matriz_pixels_green = img[:, :, 1]
# # print("Matriz de pixels da imagem (green):", matriz_pixels_green)

# matriz_pixels_red = img[:, :, 2]
# # print("Matriz de pixels da imagem (red):", matriz_pixels_red)

# Função para fazer a quantização da imagem
def quatizar_img(canal):
    delta = 256//2
    return(canal//delta)*255

# Quantiza a imagem para cada canal de cor
# img_quantizada_blue = quatizar_img(matriz_pixels_blue)
# img_quantizada_green = quatizar_img(matriz_pixels_green)
# img_quantizada_red = quatizar_img(matriz_pixels_red)

img_quatizada_cinza = quatizar_img(img_cinza)

#ditherizacao dos canais 

def ditherizacao(canal):
    canal = canal.astype(np.float32) 
    altura, largura = canal.shape
    for i in range(altura):
        for j in range(largura):
            old_pixel = canal[i, j]
            new_pixel = 255 if old_pixel > 127 else 0
            canal[i, j] = new_pixel
            error = old_pixel - new_pixel

            # Distribui o erro para os pixels vizinhos
            if j + 1 < largura:
                canal[i, j + 1] += error * 7 / 16
            if i + 1 < altura:
                canal[i + 1, j] += error * 5 / 16
                if j > 0:
                    canal[i + 1, j - 1] += error * 3 / 16
                if j + 1 < largura:
                    canal[i + 1, j + 1] += error * 1 / 16


    return np.clip(canal, 0, 255).astype(np.uint8)        


# imagem_ditherizada_blue = ditherizacao(img_quantizada_blue)
# imagem_ditherizada_green = ditherizacao(img_quantizada_green)  
# imagem_ditherizada_red = ditherizacao(img_quantizada_red)
imagem_ditherizada_cinza = ditherizacao(img_quatizada_cinza)

# Junta os canais quantizados em uma nova imagem
# img_ditherizada = cv.merge((imagem_ditherizada_blue, img_quantizada_green, imagem_ditherizada_red))

# print("Imagem quantizada apos juntar os canais de cores: ", img_ditherizada)

# cv.imshow ('Imagem quantizada', img_ditherizada)
cv.imwrite('imagem_ditherizada_cinza.png', imagem_ditherizada_cinza)
cv.imshow ('Imagem ditherizada', imagem_ditherizada_cinza)

# cv.imshow('Nicolas Cage', img)
cv.waitKey(50000)
cv.destroyAllWindows()

# Ditherização direta usando PIL
def dithizacao_direta(img):
    img_dither_pil = Image.open(img).convert("1", dither=Image.FLOYDSTEINBERG)
    return img_dither_pil


img_dither_pil = dithizacao_direta(img)

cv.imwrite('imagem_ditherizada_direta.png', img_dither_pil)
cv.imshow('Imagem ditherizada direta', img_dither_pil)
cv.waitKey(50000)   
cv.destroyAllWindows()   

