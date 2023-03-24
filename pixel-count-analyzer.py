import datetime
import os
import sys
import openpyxl
from openpyxl.styles import Font
from PIL import Image

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet['A1'] = 'Filename'
worksheet['B1'] = 'Total Pixel Count'
worksheet['C1'] = 'White Pixel Count'
worksheet['D1'] = 'Percentage Of White Pixels'

row = worksheet[1]
for cell in row:
    cell.font = Font(size=12, bold=True)

counter = 2

try:
    # Create the output folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # Set the folder path to the "images" folder in the same directory as the script
    folder_path = os.path.join(os.path.dirname(sys.argv[0]), 'images')

    # Loop over all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is an image file with a supported extension
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')):
            print(f'Processing file: {file_name}')
            # Open the image file using PIL
            img_path = os.path.join(folder_path, file_name)
            img = Image.open(img_path)

            # Check if the image is a TIFF file and set the pixel value to look for accordingly
            if img.format == 'TIFF':
                pixel_value = 255
            else:
                pixel_value = (255, 255, 255)

            # Count the number of pixels with the specified value
            pixel_count = 0
            for pixel in img.getdata():
                if pixel == pixel_value:
                    pixel_count += 1

            # Print the total number of pixels and the number of matching pixels
            total_pixel_count = img.width * img.height
            percentage_matching_pixels = (pixel_count / total_pixel_count) * 100

            print(f'Total pixels: {total_pixel_count}')
            print(f'White pixels: {pixel_count}')
            print(f'Percentage of white pixels: {percentage_matching_pixels:.2f}%')

            namecell = "A"+str(counter)
            totalcell = "B"+str(counter)
            whitecell = "C"+str(counter)
            percentcell = "D"+str(counter)

            worksheet[namecell] = f'{os.path.splitext(file_name)[0]}'
            worksheet[totalcell] = total_pixel_count
            worksheet[whitecell] = pixel_count
            worksheet[percentcell] = f'{percentage_matching_pixels:.2f}%'

            counter += 1

    workbook.save(os.path.join("output", datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S.xlsx")))


except Exception as e:
    # Handle any exceptions that occur during processing
    print(f'An error occurred: {e}')
    with open('error.log', 'w') as f:
        f.write(str(e))
