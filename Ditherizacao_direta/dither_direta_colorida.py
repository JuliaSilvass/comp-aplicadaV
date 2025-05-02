import os 
from PIL import Image
import cv2 as cv
import numpy as np

# Verifica se o caminho da imagem existe
caminho_img = r"comp-aplicadaV\Img\nicolas_cage.jpeg"
if not os.path.exists(caminho_img):
    print("Caminho da imagem não encontrado.")
    exit()

img = cv.imread(caminho_img)
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

# # acessa a matriz de pixels da imagem
matriz_pixels_blue = img[:, :, 0]
cv.imwrite(os.path.join('comp-aplicadaV/Ditherizacao/canais', 'imagem_blue.png'), matriz_pixels_blue)
# print("Matriz de pixels da imagem (blue):", matriz_pixels_blue)

matriz_pixels_green = img[:, :, 1]
cv.imwrite(os.path.join('comp-aplicadaV/Ditherizacao/canais','imagem_green.png'), matriz_pixels_green)
# print("Matriz de pixels da imagem (green):", matriz_pixels_green)

matriz_pixels_red = img[:, :, 2]
cv.imwrite(os.path.join('comp-aplicadaV/Ditherizacao/canais','imagem_red.png'), matriz_pixels_red)
# print("Matriz de pixels da imagem (red):", matriz_pixels_red)


# Ditherização direta usando PIL
def dithizacao_direta(img):
    img_dither_pil = Image.open(img).convert("1", dither=Image.FLOYDSTEINBERG)
    return  np.array(img_dither_pil).astype(np.uint8) * 255

img_dither_pil_blue = dithizacao_direta(r"comp-aplicadaV/Ditherizacao_direta/canais/imagem_blue.png")
img_dither_pil_green = dithizacao_direta(r"comp-aplicadaV/Ditherizacao_direta/canais/imagem_green.png")
img_dither_pil_red = dithizacao_direta(r"comp-aplicadaV/Ditherizacao_direta/canais/imagem_red.png")

#junta os canais ditherizados
imagem_ditherizada_colorida = cv.merge((img_dither_pil_blue, img_dither_pil_green, img_dither_pil_red))

cv.imwrite('comp-aplicadaV/ImgDitherizadaDireta/imagem_ditherizada_colorida_pil.png', imagem_ditherizada_colorida)
cv.imshow('Imagem Ditherizada Colorida', imagem_ditherizada_colorida)
cv.waitKey(4000)
cv.destroyAllWindows()

