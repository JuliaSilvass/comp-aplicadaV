import os 
from PIL import Image

# Verifica se o caminho da imagem existe
caminho_img = r"comp-aplicadaV\Img\nicolas_cage.jpeg"
if not os.path.exists(caminho_img):
    print("Caminho da imagem não encontrado.")
    exit()


# Ditherização direta usando PIL
def dithizacao_direta(img):
    img_dither_pil = Image.open(img).convert("1", dither=Image.FLOYDSTEINBERG)
    return img_dither_pil


img_dither_pil = dithizacao_direta(r"comp-aplicadaV\Img\nicolas_cage.jpeg")

img_dither_pil.save('comp-aplicadaV/ImgDitherizadaDireta/imagem_ditherizada_pil.png')   
img_dither_pil.show()

