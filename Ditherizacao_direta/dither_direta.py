import os 
from PIL import Image

# Verifica se o caminho da imagem existe
caminho_img = r"..\Img\nicolas_cage.jpeg"
if not os.path.exists(caminho_img):
    print("Caminho da imagem não encontrado.")
    exit()

# Ditherização direta usando PIL
img_dither_pil = Image.open(caminho_img).convert("1", dither=Image.FLOYDSTEINBERG)

img_dither_pil.save('../ImgDitherizadaDireta/imagem_ditherizada_pil.png')   
img_dither_pil.show()
