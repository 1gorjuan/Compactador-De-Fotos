import sys
import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image as RLImage

def redimensionar_imagem(filename, pasta):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        return None
    
    with Image.open(filename) as img:
        largura_maxima = 1000
        img.thumbnail((largura_maxima, largura_maxima), Image.ANTIALIAS)
        novo_nome_arquivo = os.path.join(pasta, f"redimensionada_{os.path.basename(filename)}")
        try:
            img.save(novo_nome_arquivo, optimize=True, quality=80)
        except IOError:
            return None
        
        return novo_nome_arquivo

pasta = input('Por favor, insira o caminho para a pasta contendo as imagens a serem redimensionadas: ')
if not os.path.exists(pasta):
    print('A pasta especificada não existe. Por favor, insira um caminho válido e tente novamente.')
    sys.exit()

imagens_redimensionadas = []

for filename in os.scandir(pasta):
    if filename.is_file() and filename.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        caminho_imagem = filename.path
        novo_nome_arquivo = redimensionar_imagem(caminho_imagem, pasta)
        
        if novo_nome_arquivo is not None:
            novo_caminho_imagem = os.path.join(pasta, f"redimensionada_{os.path.basename(filename)}")
            if os.path.exists(novo_caminho_imagem):
                print(f'Warning: {novo_caminho_imagem} already exists and will be overwritten.')
            os.rename(novo_nome_arquivo, novo_caminho_imagem)
            imagens_redimensionadas.append(novo_caminho_imagem)

if imagens_redimensionadas:
    pdf_filename = os.path.join(pasta, "imagens_redimensionadas.pdf")
    
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    story = []

    for imagem in imagens_redimensionadas:
        story.append(RLImage(imagem, width=400, height=400))

    doc.build(story)
    
    print(f'O PDF com as imagens redimensionadas foi criado em {pdf_filename}.')
else:
    print('Nenhuma imagem válida foi redimensionada.')
