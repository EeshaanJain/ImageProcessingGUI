from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import sys
from PIL import Image
from pathlib import Path
import os
import numpy as np
import random
import string
import re
from Scripts import basic_transforms, hist_eq, transforms, random_image
import matplotlib.pyplot as plt
from Scripts.image_conversion import to_grayscale, colorsys_getRGBA



import ctypes
app_id = 'EeshaanJain.EE610.ImProME.Assignment1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sample_img = Image.open("Images/sample.jpg").convert("RGBA")
        self.undoStack = [(np.array(self.sample_img), "Images/sample.jpg")] # I will implement stack using a list of tuples containing (Image, Image path)
        # Initially the undoStack has the sample Image which is the first image to be shown
        self.display_image("Images/sample.jpg")
        # <-------------------- Button Actions -------------------->
        # <-------------------------------------------------------->
        self.button_cat.clicked.connect(self.load_cat_image)
        self.button_load_image.clicked.connect(self.load_image)
        self.button_save_image.clicked.connect(self.save_image)
        self.button_undo_one.clicked.connect(self.undo_once)
        self.button_undo_all.clicked.connect(self.undo_all)
        self.button_shortcut_clockwise.clicked.connect(self.rotate_clockwise)
        self.button_shortcut_anticlockwise.clicked.connect(self.rotate_anticlockwise)
        self.button_shortcut_custom_rotate.clicked.connect(self.rotate_arbitrary)
        self.button_shortcut_invert_left_right.clicked.connect(self.horizontal_flip)
        self.button_shortcut_invert_up_down.clicked.connect(self.vertical_flip)
        self.button_shortcut_invert_diagonal.clicked.connect(self.diagonal_flip)
        self.button_equalize_histogram.clicked.connect(self.hist_eq)
        self.button_get_channel.clicked.connect(self.get_channel)
        self.button_grayscale.clicked.connect(self.to_grayscale)
        self.button_invert.clicked.connect(self.invert_image)
        self.button_gamma_correction.clicked.connect(self.gamma_correction)
        self.button_log_transform.clicked.connect(self.log_transform)
        self.button_random_image.clicked.connect(self.generate_random_image)

    def load_image(self):
        home_dir = str(Path.home()) # Get home directory
        load_image_filename = QtWidgets.QFileDialog.getOpenFileName(self, "OpenFile", home_dir,
                                    "Image files (*.jpg *.png *.jpeg)") # Open file
        if load_image_filename[0]:
            load_image_file = Image.open(load_image_filename[0]).convert("RGBA") # Load the image
            self.undoStack.append((np.array(load_image_file), load_image_filename[0])) # Add current image to undoStack
            self.display_image(load_image_filename[0]) # Display image

    def save_image(self):
        
        home_dir = str(Path.home())
        save_filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFile", home_dir, "Image Files (*.png)")
        if save_filename:
            curr_img, _ = self.undoStack[-1]
            im = Image.fromarray(curr_img.astype(np.uint8))
            im.save(save_filename)

    def _internal_save(self, img):
        img = img.convert("RGBA")
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=12))
        img.save(f"temp/{file_name}.png")
        return f"temp/{file_name}.png"

    

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

    def undo_once(self):
        if len(self.undoStack) > 1:
            removed_image = self.undoStack.pop()
            if removed_image[1].startswith('temp/'):
                os.remove(removed_image[1])
            self.display_image(self.undoStack[-1][1])


    def undo_all(self):
        if len(self.undoStack) > 1:
            self.undoStack = self.undoStack[:2]
            self.display_image(self.undoStack[-1][1])

    # <-------------------- Basic transforms --------------------->
    def rotate_clockwise(self):
        curr_img, _ = self.undoStack[-1]
        rotated_curr_img = basic_transforms.rotate_clockwise(curr_img)
        rotated_curr_img_filepath = self._internal_save(Image.fromarray(rotated_curr_img))
        self.undoStack.append((rotated_curr_img, rotated_curr_img_filepath))
        self.display_image(rotated_curr_img_filepath)

    def rotate_anticlockwise(self):
        curr_img, _ = self.undoStack[-1]
        rotated_curr_img = basic_transforms.rotate_anticlockwise(curr_img)
        rotated_curr_img_filepath = self._internal_save(Image.fromarray(rotated_curr_img))
        self.undoStack.append((rotated_curr_img, rotated_curr_img_filepath))
        self.display_image(rotated_curr_img_filepath)
    
    def rotate_arbitrary(self):
        name, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter the degrees:\nExamples:\n 40\n-30\n+56.33\nNote that the left out space is filled with black")
        if done and re.match("^[+-]?((\d+(\.\d*)?)|(\.\d+))$", name):
            curr_img, _ = self.undoStack[-1]
            rotated_curr_img = basic_transforms.rotate_arbitrary(curr_img, float(name))
            rotated_curr_img_filepath = self._internal_save(Image.fromarray(rotated_curr_img))
            self.undoStack.append((rotated_curr_img, rotated_curr_img_filepath))
            self.display_image(rotated_curr_img_filepath)
 
    def horizontal_flip(self):
        curr_img, _ = self.undoStack[-1]
        flipped_curr_img = basic_transforms.horizontal_flip(curr_img)
        flipped_curr_img_filepath = self._internal_save(Image.fromarray(flipped_curr_img))
        self.undoStack.append((flipped_curr_img, flipped_curr_img_filepath))
        self.display_image(flipped_curr_img_filepath)

    def vertical_flip(self):
        curr_img, _ = self.undoStack[-1]
        flipped_curr_img = basic_transforms.vertical_flip(curr_img)
        flipped_curr_img_filepath = self._internal_save(Image.fromarray(flipped_curr_img))
        self.undoStack.append((flipped_curr_img, flipped_curr_img_filepath))
        self.display_image(flipped_curr_img_filepath)

    def diagonal_flip(self):
        curr_img, _ = self.undoStack[-1]
        flipped_curr_img = basic_transforms.diagonal_flip(curr_img)
        flipped_curr_img_filepath = self._internal_save(Image.fromarray(flipped_curr_img))
        self.undoStack.append((flipped_curr_img, flipped_curr_img_filepath))
        self.display_image(flipped_curr_img_filepath)

    def hist_eq(self):
        curr_img, _ = self.undoStack[-1]

        new_img, hist_old, hist_new = hist_eq.hist_equalization(curr_img)
        new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)
        plt.bar(range(256), hist_old, label='old')
        plt.bar(range(256), hist_new, label='new')
        plt.title('Result of Histogram Equalization')
        plt.legend()
        plt.savefig('Results/histogram_equalization_result' + str(random.randint(10000000, 99999999)) + '.png')

    def gamma_correction(self):
        gamma, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter gamma:\nExamples:\n1.1\n3")
        if done and re.match("^[0-9]\d*(\.\d+)?$", gamma):
            curr_img, _ = self.undoStack[-1]
            new_img = transforms.power_law_transformation(curr_img, float(gamma))
            new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
            self.undoStack.append((new_img, new_img_filepath))
            self.display_image(new_img_filepath)

    def log_transform(self):
        curr_img, _ = self.undoStack[-1]
        new_img = transforms.log_transformation(curr_img)
        new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)
            

    def invert_image(self):
        curr_img, _ = self.undoStack[-1]
        r, g, b, a = colorsys_getRGBA(curr_img)
        r, g, b = 255 - r, 255 - g, 255 - b 
        new_img = np.dstack((r, g, b, a))
        new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)

    def get_channel(self):
        name, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter R, G or B\nExample:\nR")
        curr_img, _ = self.undoStack[-1]
        if done and re.match("R|G|B", name):
            r, g, b, a = colorsys_getRGBA(curr_img)
            if name == "R":
                red_img = np.dstack((r, r, r, a))
                red_img_path = self._internal_save(Image.fromarray(red_img.astype(np.uint8)))
                self.undoStack.append((red_img, red_img_path)) 
                self.display_image(red_img_path)
            elif name == "G":
                green_img = np.dstack((g, g, g, a))
                green_img_path = self._internal_save(Image.fromarray(green_img.astype(np.uint8)))
                self.undoStack.append((green_img, green_img_path)) 
                self.display_image(green_img_path)
            else:
                blue_img = np.dstack((b, b, b, a))
                blue_img_path  = self._internal_save(Image.fromarray(blue_img.astype(np.uint8)))
                self.undoStack.append((blue_img, blue_img_path)) 
                self.display_image(blue_img_path)
        
    def to_grayscale(self):
        curr_img, _ = self.undoStack[-1]
        new_img = to_grayscale(curr_img)
        new_img_path = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_path))
        self.display_image(new_img_path)

            
    def generate_random_image(self):
        random_image_filename = random_image.get_random_image()
        img_arr = np.array(Image.open(f"Images/random/{random_image_filename}.png").convert("RGBA"))
        self.undoStack.append((img_arr, random_image_filename))
        self.display_image(random_image_filename)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app_icon = QtGui.QIcon()
    app_icon.addFile('Images/logo_final.png', QtCore.QSize(32,32))
    win.setWindowIcon(app_icon)
    for f in os.scandir('temp/'):
        os.remove(f.path)
    for f in os.scandir('Results/'):
        os.remove(f.path)
    for f in os.scandir('Images/random/'):
        os.remove(f.path)
    sys.exit(app.exec_())
    
