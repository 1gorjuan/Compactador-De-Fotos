import sys
import os
from PIL import Image
from fpdf import FPDF

def resize_image(filename, folder):
    # Code to resize the image
    pass

def create_pdf(folder):
    pdf = FPDF()
    # Iterate through all images in the folder
    for filename in os.scandir(folder):
        if filename.is_file() and filename.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Open image to get dimensions
            with Image.open(filename.path) as img:
                # Calculate aspect ratio to maintain proportions
                width, height = img.size
                aspect_ratio = width / height
                # A4 size: 210x297 mm
                # Adjust dimensions to fit A4 page while maintaining aspect ratio
                if width > height:
                    new_width = 210
                    new_height = 210 / aspect_ratio
                else:
                    new_height = 297
                    new_width = 297 * aspect_ratio
                pdf.add_page()
                # Add image to PDF with calculated dimensions
                pdf.image(filename.path, x=0, y=0, w=new_width, h=new_height)
    pdf_output = os.path.join(folder, "output.pdf")
    pdf.output(pdf_output, "F")
    return pdf_output

def main():
    print("Escolha uma opção:")
    print("1 - Compactar Fotos")
    print("2 - Criar PDF")

    option = input("Escolha o número da Opção: ")

    folder = input('Por favor, cole o caminho da pasta contendo as imagens: ') 
    if not os.path.exists(folder):
        print('A pasta não existe. Por favor cole um caminho válido.') 
        sys.exit()

    if option == "1":
        for filename in os.scandir(folder):
            if filename.is_file() and filename.stat().st_size > 1000000 and filename.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = filename.path
                new_filename = resize_image(image_path, folder)
                # Code to resize the images
            elif filename.is_file() and filename.stat().st_size <= 1000000:
                print(f'{filename.path} is already below the size limit.')
            elif filename.is_file() and not filename.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(f'{filename.path} is not a valid image file.')

    elif option == "2":
        pdf_output = create_pdf(folder)
        print(f"PDF created successfully: {pdf_output}")

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()