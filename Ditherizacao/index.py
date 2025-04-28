import cv2 as cv 
import numpy as np
import os 

# Verifica se o caminho da imagem existe
caminho_img = r"nicolas_cage.jpeg"
if not os.path.exists(caminho_img):
    print("Caminho da imagem não encontrado.")
    exit()

# Carrega a imagem e coloca em cinza 
img = cv.imread(caminho_img)
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

# acessa a matriz de pixels da imagem
matriz_pixels_blue = img[:, :, 0]
# print("Matriz de pixels da imagem (blue):", matriz_pixels_blue)

matriz_pixels_green = img[:, :, 1]
# print("Matriz de pixels da imagem (green):", matriz_pixels_green)

matriz_pixels_red = img[:, :, 2]
# print("Matriz de pixels da imagem (red):", matriz_pixels_red)

# Função para fazer a quantização da imagem
def quatizar_img(canal):
    delta = 256//2
    return(canal//delta)*255

# Quantiza a imagem para cada canal de cor
img_quantizada_blue = quatizar_img(matriz_pixels_blue)
img_quantizada_green = quatizar_img(matriz_pixels_green)
img_quantizada_red = quatizar_img(matriz_pixels_red)



# # Junta os canais quantizados em uma nova imagem
# img_quantizada = cv.merge((img_quantizada_blue, img_quantizada_green, img_quantizada_red))

# print("Imagem quantizada apos juntar os canais de cores: ", img_quantizada)

# cv.imshow ('Imagem quantizada', img_quantizada)

# cv.imshow('Nicolas Cage', img)
cv.waitKey(10000)
cv.destroyAllWindows()

