 """  19𝒟070022
  ______          _                              _       _       
 |  ____|        | |                            | |     (_)      
 | |__   ___  ___| |__   __ _  __ _ _ __        | | __ _ _ _ __  
 |  __| / _ \/ __| '_ \ / _` |/ _` | '_ \   _   | |/ _` | | '_ \ 
 | |___|  __/\__ \ | | | (_| | (_| | | | | | |__| | (_| | | | | |
 |______\___||___/_| |_|\__,_|\__,_|_| |_|  \____/ \__,_|_|_| |_|
                                                         
 """                                                              

"""
Main file containing the Image Editor
"""

# <-------------------- PyQt5 -------------------->
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

# <-------------------- File IO -------------------->
import sys
from pathlib import Path
import os

# <-------------------- Pillow library: Note that OpenCV wasn't used anywhere-------------------->
from PIL import Image

# <-------------------- Processing Libraries -------------------->
import numpy as np
import random
import string
import re

# <-------------------- Image Processing Scripts -------------------->
from Scripts import basic_transforms, hist_eq, transforms
import matplotlib.pyplot as plt
from Scripts.image_conversion import to_grayscale, colorsys_getRGBA
import Scripts.filters as F
import Scripts.convolution as Conv

# <-------------------- To set the logo -------------------->
import ctypes
app_id = 'EeshaanJain.EE610.ImProME.Assignment1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

# <-------------------- Main Window - inherits from gui.py -------------------->
class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sample_img = Image.open("Images/sample.jpg").convert("RGBA") # Sample image loaded everytime the Image editor is loaded
        self.undoStack = [(np.array(self.sample_img, dtype=np.uint8), "Images/sample.jpg")] # I will implement stack using a list of tuples containing (Image array, Image path)
        # Initially the undoStack has the sample Image which is the first image to be shown
        self.display_image("Images/sample.jpg") # Function to display the image on the GUI
        # <-------------------- Button Actions -------------------->
        self.button_cat.clicked.connect(self.load_cat_image) # Button to load random cat image
        self.button_load_image.clicked.connect(self.load_image) # Button to load image
        self.button_save_image.clicked.connect(self.save_image) # Button to save image
        self.button_undo_one.clicked.connect(self.undo_once) # Button to undo
        self.button_undo_all.clicked.connect(self.undo_all) # Button to revert
        self.button_shortcut_clockwise.clicked.connect(self.rotate_clockwise) # Button to rotate image clockwise
        self.button_shortcut_anticlockwise.clicked.connect(self.rotate_anticlockwise) # Button to rotate image anticlockwise
        self.button_shortcut_custom_rotate.clicked.connect(self.rotate_arbitrary) # Button to rotate image arbitrarily
        self.button_shortcut_invert_left_right.clicked.connect(self.horizontal_flip) # Button to flip image horizontally
        self.button_shortcut_invert_up_down.clicked.connect(self.vertical_flip) # Button to flip image vertically
        self.button_shortcut_invert_diagonal.clicked.connect(self.diagonal_flip) # Button to flip image diagonally
        self.button_equalize_histogram.clicked.connect(self.hist_eq) # Button to perform histogram equalization
        self.button_get_channel.clicked.connect(self.get_channel) # Button to perform channel separation
        self.button_grayscale.clicked.connect(self.to_grayscale) # Button to perform grayscale conversion
        self.button_invert.clicked.connect(self.invert_image) # Button to perform image inversion
        self.button_gamma_correction.clicked.connect(self.gamma_correction) # Button to perform gamma correction
        self.button_log_transform.clicked.connect(self.log_transform) # Button to perform log transformation
        self.button_random_image.clicked.connect(self.generate_random_image) # Button to load random image
        self.button_blur.clicked.connect(self.blur_image) # Button to perform blurring
        self.button_sharpen.clicked.connect(self.sharpen_image)
        self.action_load_image.triggered.connect(self.load_image) # Menu Item to load image
        self.action_save_image.triggered.connect(self.save_image) # Menu Item to save image
        self.action_quit.triggered.connect(self.close) # Menu Item to close editor

    def load_image(self):
        """
        Function to load image into the GUI
        """
        home_dir = str(Path.home()) # Get home directory
        load_image_filename = QtWidgets.QFileDialog.getOpenFileName(self, "OpenFile", home_dir,"Image files (*.jpg *.png *.jpeg)") # Open file
        if load_image_filename[0]: # The first index contains the directory
            load_image_file = Image.open(load_image_filename[0]).convert("RGBA") # Load the image
            self.undoStack.append((np.array(load_image_file, dtype=np.uint8), load_image_filename[0])) # Add current image to undoStack
            self.display_image(load_image_filename[0]) # Display image
            print("="*90)
            print("Image loaded from directory:", load_image_filename[0])
            print("="*90)

    def save_image(self):
        """
        Function to save image
        """
        home_dir = str(Path.home())
        save_filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFile", home_dir, "Image Files (*.png)")
        if save_filename:
            curr_img, _ = self.undoStack[-1] # Get current image
            im = Image.fromarray(curr_img.astype(np.uint8)) # Convert to PIL Image
            im.save(save_filename) # Save in the required directory

            print("="*90)
            print("Image saved to directory:", save_filename)
            print("="*90)

    def _internal_save(self, img):
        """
        Internal function - to save intermediate images
        """
        img = img.convert("RGBA") # Safety convert to RGBA
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=12)) # Generate random filename
        img.save(f"temp/{file_name}.png") # Save file
        return f"temp/{file_name}.png" # Return file directory

    

    def display_image(self, img_path):
        self.image_view_scene = QtWidgets.QGraphicsScene(self.centralwidget) # Load GraphicScene
        self.image_view_scene.addPixmap(QtGui.QPixmap(img_path)) # Add image to scene
        self.image_view_graphics.setScene(self.image_view_scene) # Add scene to view

    def load_cat_image(self):
        cat_path = "Images/cats/" # Cat Images 
        cat_image_list = os.listdir('Images/cats/') # Get list of images 
        cat_image_path = random.choice(cat_image_list) # Choose random image    
        cat_image = Image.open(cat_path + cat_image_path).convert("RGBA") # Load image
        self.undoStack.append((np.array(cat_image, dtype=np.uint8), cat_path + cat_image_path)) # Add image to undoStack
        self.display_image(cat_path + cat_image_path) # Display image
        print("="*90)
        print("Loaded random cat image from:", cat_image_path)
        print("="*90)
        

    def undo_once(self):
        """
        Function to perform the undo operation till only the sample image is left
        """
        if len(self.undoStack) > 1: # Only undo till there is the sample image left
            removed_image = self.undoStack.pop()
            if removed_image[1].startswith('temp/'): # Remove the image from temp/ directory
                os.remove(removed_image[1])
            self.display_image(self.undoStack[-1][1]) # Display the previous image
            print("="*90)
            print("1 undo move successfully completed")
            print("="*90)


    def undo_all(self):
        """ 
        Function to perform the revert (undo all) operation, till the second image in the stack, i.e the one after the sample image. In case we need to get back the sample image, a manual undo needs to be done after this.
        """
        if len(self.undoStack) > 1: # Only revert till there is the image after sample image left. If working with sample image, a manual undo needs to be done.
            self.undoStack = self.undoStack[:2]
            self.display_image(self.undoStack[-1][1])
            print("="*90)
            print("Revert move successfully completed. The second image will be displayed.")
            print("="*90)

    # <-------------------- Basic transforms --------------------->
    def rotate_clockwise(self):
        """
        Function to rotate image clockwise by 90 degrees
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        rotated_curr_img = basic_transforms.rotate_clockwise(curr_img).astype(np.uint8) # Rotate image
        rotated_curr_img_filepath = self._internal_save(Image.fromarray(rotated_curr_img))
        self.undoStack.append((rotated_curr_img, rotated_curr_img_filepath))
        self.display_image(rotated_curr_img_filepath)
        print("="*90)
        print("Image rotated clockwise by 90 degrees")
        print("="*90)

    def rotate_anticlockwise(self):
        """
        Function to rotate image anticlockwise by 90 degrees
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        rotated_curr_img = basic_transforms.rotate_anticlockwise(curr_img).astype(np.uint8) # Rotate image
        rotated_curr_img_filepath = self._internal_save(Image.fromarray(rotated_curr_img))
        self.undoStack.append((rotated_curr_img, rotated_curr_img_filepath))
        self.display_image(rotated_curr_img_filepath)
        print("="*90)
        print("Image rotated counterclockwise by 90 degrees")
        print("="*90)
    
    def rotate_arbitrary(self):
        """
        Function to rotate image clockwise by arbitrary degrees
        """
        name, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter the degrees:\nExamples:\n 40\n-30\n+56.33\nNote that the left out space is filled with black")
        if done and re.match("^[+-]?((\d+(\.\d*)?)|(\.\d+))$", name): # Regex to check format
            curr_img, _ = self.undoStack[-1] # Get current image
            rotated_curr_img = basic_transforms.rotate_arbitrary(curr_img, float(name)).astype(np.uint8) # Rotate image using SciPy
            rotated_curr_img_filepath = self._internal_save(Image.fromarray(rotated_curr_img))
            self.undoStack.append((rotated_curr_img, rotated_curr_img_filepath))
            self.display_image(rotated_curr_img_filepath)
            print("="*90)
            print(f"Image rotated by {name} degrees")
            print("="*90)
 
    def horizontal_flip(self):
        """
        Function to flip image horizontally
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        flipped_curr_img = basic_transforms.horizontal_flip(curr_img).astype(np.uint8) # Horizontal Flip image
        flipped_curr_img_filepath = self._internal_save(Image.fromarray(flipped_curr_img))
        self.undoStack.append((flipped_curr_img, flipped_curr_img_filepath))
        self.display_image(flipped_curr_img_filepath)
        print("="*90)
        print("Image flipped horizontally")
        print("="*90)

    def vertical_flip(self):
        """
        Function to flip image vertically
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        flipped_curr_img = basic_transforms.vertical_flip(curr_img).astype(np.uint8) # Vertical Flip image
        flipped_curr_img_filepath = self._internal_save(Image.fromarray(flipped_curr_img))
        self.undoStack.append((flipped_curr_img, flipped_curr_img_filepath))
        self.display_image(flipped_curr_img_filepath)
        print("="*90)
        print("Image flipped vertically")
        print("="*90)

    def diagonal_flip(self):
        """
        Function to flip image diagonally
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        flipped_curr_img = basic_transforms.diagonal_flip(curr_img).astype(np.uint8) # Diagonal flip the image
        flipped_curr_img_filepath = self._internal_save(Image.fromarray(flipped_curr_img))
        self.undoStack.append((flipped_curr_img, flipped_curr_img_filepath))
        self.display_image(flipped_curr_img_filepath)
        print("="*90)
        print("Image flipped diagonally")
        print("="*90)

    def hist_eq(self):
        """
        Function to perform histogram equalization and display intensity plot
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        new_img, hist_old, hist_new = hist_eq.hist_equalization(curr_img) # Perform histogram equalization
        new_img = new_img.astype(np.uint8)
        new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)
        # Plot histograms and save in Results directory
        plt.bar(range(256), hist_old, label='old')
        plt.bar(range(256), hist_new, label='new')
        plt.title('Result of Histogram Equalization')
        plt.legend()
        plt.savefig('Results/histogram_equalization_result' + str(random.randint(10000000, 99999999)) + '.png')
        print("="*90)
        print("Performed Histogram Equalization. Result saved in the Results/ directory")
        print("="*90)

    def gamma_correction(self):
        """
        Function to perform gamma correction 
        """
        gamma, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter gamma:\nExamples:\n1.1\n3") # Regex to match all decimals and integers
        if done and re.match("^[0-9]\d*(\.\d+)?$", gamma):
            curr_img, _ = self.undoStack[-1] # Get current image
            new_img = transforms.power_law_transformation(curr_img, float(gamma)).astype(np.uint8) # Gamma correction
            new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
            self.undoStack.append((new_img, new_img_filepath))
            self.display_image(new_img_filepath)
            print("="*90)
            print(f"Performed gamma correction for gamma = {gamma}")
            print("="*90)

    def log_transform(self):
        """
        Function to perform log transform 
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        new_img = transforms.log_transformation(curr_img).astype(np.uint8) # Log transformation
        new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)
        print("="*90)
        print("Performed log transform")
        print("="*90)
            

    def invert_image(self):
        """
        Function to perform image inversion
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        new_img = transforms.invert(curr_img).astype(np.uint8) # Invert image
        new_img_filepath = self._internal_save(Image.fromarray(new_img))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)
        print("="*90)
        print("Inverted the image in the colorspace")
        print("="*90)

    def get_channel(self):
        """
        Function to perform channel separation
        """
        name, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter R, G or B\nExample:\nR") # Regex to match the text R or G or B
        curr_img, _ = self.undoStack[-1]
        if done and re.match("R|G|B", name):
            r, g, b, a = colorsys_getRGBA(curr_img) # Separate image into R G B A channels
            if name == "R":
                red_img = np.dstack((r, r, r, a)).astype(np.uint8) # Stack same channel to get RGBA of that channel
                red_img_path = self._internal_save(Image.fromarray(red_img))
                self.undoStack.append((red_img, red_img_path)) 
                self.display_image(red_img_path)
                print("="*90)
                print("Displaying red channel")
                print("="*90)
            elif name == "G":
                green_img = np.dstack((g, g, g, a)).astype(np.uint8)# Stack same channel to get RGBA of that channel
                green_img_path = self._internal_save(Image.fromarray(green_img))
                self.undoStack.append((green_img, green_img_path)) 
                self.display_image(green_img_path)
                print("="*90)
                print("Displaying green channel")
                print("="*90)
            else:
                blue_img = np.dstack((b, b, b, a)).astype(np.uint8)# Stack same channel to get RGBA of that channel
                blue_img_path  = self._internal_save(Image.fromarray(blue_img))
                self.undoStack.append((blue_img, blue_img_path)) 
                self.display_image(blue_img_path)
                print("="*90)
                print("Displaying blue channel")
                print("="*90)
        
    def to_grayscale(self):
        """
        Function to perform grayscale conversion
        """
        curr_img, _ = self.undoStack[-1] # Get current image
        new_img = to_grayscale(curr_img).astype(np.uint8) # Convert to grayscale
        new_img_path = self._internal_save(Image.fromarray(new_img))
        self.undoStack.append((new_img, new_img_path))
        self.display_image(new_img_path)
        print("="*90)
        print("Converted image to grayscale")
        print("="*90)

            
    def generate_random_image(self):
        """
        Function to fetch random image
        """
        random_image_filename = 'Images/random/' + random.choice(os.listdir('Images/random')) # Load random image from Images/random directory
        img_arr = np.array(Image.open(random_image_filename).convert("RGBA")).astype(np.uint8)
        self.undoStack.append((img_arr, random_image_filename))
        self.display_image(random_image_filename)
        print("="*90)
        print("Displaying random image from Images/random/ directory")
        print("="*90)

    def blur_image(self):
        """
        Function to perform Box or Gaussian Blur
        """
        name, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter G for Gaussian Blur and B for box(mean) blur.\nOptionally mention size (odd) for box blur <B size>, and size (odd), sigma for Gaussian blur <G size sigma>. Default values are size = 3 and sigma = sqrt(size)\nExample:\nG 5 1\nB 3\nG 3\nB\nG\nNote:Use single spaces to separate values") # Regex to match the following formats: G <size?> <sigma?> and B <size?> where "?" means the parameter is optional
        if done:
            # Gaussian Filter
            name = name.strip()
            if name.startswith('G'):
                # No size or sigma case
                if len(name) == 1:
                    gauss = F.gaussian_filter(3) # Get gaussian filter
                    curr_img, _ = self.undoStack[-1]
                    new_img = Conv.convolution_hsv(curr_img, gauss).astype(np.uint8) # Perform convolution 
                    new_img_path = self._internal_save(Image.fromarray(new_img))
                    self.undoStack.append((new_img, new_img_path))
                    self.display_image(new_img_path)
                    print("="*90)
                    print("Performed Gaussian Blur for kernel size = 3x3 and sigma = sqrt(3)")
                    print("="*90)

                # Size case
                elif len(name.split(' ')) == 2 and re.match('^\d*[13579]$', name.split(' ')[-1]):
                    size = int(name.split(' ')[-1])
                    gauss = F.gaussian_filter(size)
                    curr_img, _ = self.undoStack[-1]
                    new_img = Conv.convolution_hsv(curr_img, gauss).astype(np.uint8)
                    new_img_path = self._internal_save(Image.fromarray(new_img))
                    self.undoStack.append((new_img, new_img_path))
                    self.display_image(new_img_path)
                    print("="*90)
                    print(f"Performed Gaussian Blur for kernel size = {size}x{size} and sigma = sqrt({size})")
                    print("="*90)

                # Size and sigma case
                elif len(name.split(' ')) == 3 and re.match('^\d*[13579]$', name.split(' ')[-2]) and re.match('^\d*\.?\d*$', name.split(' ')[-1]):
                    size = int(name.split(' ')[-2])
                    sigma = float(name.split(' ')[-1])
                    gauss = F.gaussian_filter(size, sigma)
                    curr_img, _ = self.undoStack[-1]
                    new_img = Conv.convolution_hsv(curr_img, gauss).astype(np.uint8)
                    new_img_path = self._internal_save(Image.fromarray(new_img))
                    self.undoStack.append((new_img, new_img_path))
                    self.display_image(new_img_path)
                    print("="*90)
                    print(f"Performed Gaussian Blur for kernel size = {size}x{size} and sigma={sigma}")
                    print("="*90)

            elif name.startswith('B'):
                # No size case
                if len(name) == 1:
                    avg = F.average_filter(3) # Get box filter
                    curr_img, _ = self.undoStack[-1]
                    new_img = Conv.convolution_hsv(curr_img, avg).astype(np.uint8) # Perform convolution
                    new_img_path = self._internal_save(Image.fromarray(new_img))
                    self.undoStack.append((new_img, new_img_path))
                    self.display_image(new_img_path)
                    print("="*90)
                    print("Performed Box/Mean Blur for kernel size = 3x3")
                    print("="*90)

                # Size case
                elif len(name.split(' ')) == 2 and re.match('^\d*[13579]$', name.split(' ')[-1]):
                    size = int(name.split(' ')[-1])
                    avg = F.average_filter(size)
                    curr_img, _ = self.undoStack[-1]
                    new_img = Conv.convolution_hsv(curr_img, avg).astype(np.uint8)
                    new_img_path = self._internal_save(Image.fromarray(new_img))
                    self.undoStack.append((new_img, new_img_path))
                    self.display_image(new_img_path)
                    print("="*90)
                    print(f"Performed Box/Mean Blur for kernel size = {size}x{size}")
                    print("="*90)

    def sharpen_image(self):
        """
        Function to perform sharpening by unmask sharping
        """
        name, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter the extent (recommended between 0.2 and 0.7) for sharpening the image\nExample\n0.4")
        if done and re.match('^\d*\.?\d*$', name): # Regex to match decimals
            extent = float(name)
            curr_img, _ = self.undoStack[-1]
            new_img = Conv.convolution_sharpen(curr_img, alpha=extent).astype(np.uint8) 
            # Perform sharpening
            new_img_path = self._internal_save(Image.fromarray(new_img))
            self.undoStack.append((new_img, new_img_path))
            self.display_image(new_img_path)
            print("="*90)
            print(f"Performed Sharpening for extent = {extent}")
            print("="*90)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app_icon = QtGui.QIcon()
    app_icon.addFile('Images/logo_final.png', QtCore.QSize(32,32))
    win.setWindowIcon(app_icon)
    # At each run, clear results of previous runs
    for f in os.scandir('temp/'):
        os.remove(f.path)
    for f in os.scandir('Results/'):
        os.remove(f.path)
    sys.exit(app.exec_())
    
