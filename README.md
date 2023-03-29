<h2>Image Resizing Script README</h2>

<p>This script allows you to resize all images in a specified folder to a maximum width of 1000 pixels, while
    maintaining the aspect ratio. If an image is larger than 1MB, it will be resized and saved with the prefix
    "redimensionada_" in the same folder. The original image will be deleted to save space.</p>

<h3>Prerequisites</h3>

<ul>
    <li>Python 3.5 or later</li>
    <li>PIL (Python Imaging Library) module</li>
</ul>

<h3>Installation</h3>

<ol>
    <li>Install Python 3.5 or later from the official website: https://www.python.org/downloads/</li>
    <li>Install the PIL module by running the command pip install pillow in the terminal.</li>
</ol>

<h3>Usage<h3>
        <ol>
            <li>Save the script in a desired location.</li>
            <li>Open a terminal window and navigate to the folder containing the script.</li>
            <li>Run the script by entering the command python image_resizing_script.py in the terminal.</li>
            <li>Enter the path to the folder containing the images you want to resize when prompted.</li>
            <li>The script will resize all eligible images in the folder and save them with the prefix "redimensionada_"
                in the same folder.</li>
            <li>The original images will be deleted.</li>
        </ol>

<h3>Notes</h3>

<ul>
    <li>The script only resizes images with the extensions ".jpg", ".jpeg", or ".png".</li>
    <li>If an image is already smaller than or equal to 1MB, it will not be resized.</li>
    <li>If a file with the same name as the resized image already exists, it will be overwritten.</li>
    <li>If the PIL module is not installed, the script will exit and prompt you to install it.</li>
</ul>
