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
from Scripts import basic_transforms, hist_eq, transforms
import matplotlib.pyplot as plt
from Scripts.image_conversion import RGBtoHSL, HSLtoRGB, to_grayscale



import ctypes
app_id = 'EeshaanJain.EE610.ImProME.Assignment1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sample_img = Image.open("Images/sample.jpg").convert("RGB")
        self.undoStack = [(np.array(self.sample_img), "Images/sample.jpg")] # I will implement stack using a list of tuples containing (Image, Image path)
        # Initially the undoStack has the sample Image which is the first image to be shown
        self.display_image("Images/sample.jpg")
        # <-------------------- Button Actions -------------------->
        # <-------------------------------------------------------->
        self.button_cat.clicked.connect(self.load_cat_image)
        self.button_load_image.clicked.connect(self.load_image)
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

    def load_image(self):
        home_dir = str(Path.home()) # Get home directory
        load_image_filename = QtWidgets.QFileDialog.getOpenFileName(self, "OpenFile", home_dir,
                                    "Image files (*.jpg *.png *.jpeg)") # Open file
        if load_image_filename[0]:
            load_image_file = Image.open(load_image_filename[0]).convert("RGB") # Load the image
            self.undoStack.append((np.array(load_image_file), load_image_filename[0])) # Add current image to undoStack
            self.display_image(load_image_filename[0]) # Display image

    # def save_image(self):
    #     home_dir = str(Path.home())
    #     save_filename = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFile", home_dir, "Image Files (*.jpg *.png *.jpeg)")
    #     if save_filename:
    #         Image.

    def _internal_save(self, img):
        img = img.convert("RGB")
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=12))
        img.save(f"temp/{file_name}.jpg")
        return f"temp/{file_name}.jpg"

    def _get_HSL(self, img, get_max_intensity=False):
        new_img = np.zeros(img.shape, dtype='int')
        if get_max_intensity:
            max_int = 0
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    new_img[i][j] = RGBtoHSL(*img[i][j])
                    max_int = max(max_int, new_img[i][j][2])

            return (new_img, max_int)
        else:
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    new_img[i][j] = RGBtoHSL(*img[i][j])

            return new_img

    def _get_RGB(self, img):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                img[i][j] = HSLtoRGB(*img[i][j])

        return img.astype('int')
    

    def display_image(self, img_path):
        self.image_view_scene = QtWidgets.QGraphicsScene(self.centralwidget) # Load GraphicScene
        self.image_view_scene.addPixmap(QtGui.QPixmap(img_path)) # Add image to scene
        self.image_view_graphics.setScene(self.image_view_scene) # Add scene to view

    def load_cat_image(self):
        cat_path = "Images/cats/" # Cat Images 
        cat_image_list = os.listdir('Images/cats/') # Get list of images 
        cat_image_path = random.choice(cat_image_list) # Choose random image    
        cat_image = Image.open(cat_path + cat_image_path) # Load image
        self.undoStack.append((np.array(cat_image), cat_path + cat_image_path)) # Add image to undoStack
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
        new_img = self._get_HSL(curr_img, False)
        hist_img, hist_old, hist_new = hist_eq.hist_equalization(new_img, new_img.shape[0], new_img.shape[1])
        new_img = self._get_RGB(hist_img)
        new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)
        plt.bar(range(100), hist_old, label='old')
        plt.bar(range(100), hist_new, label='new')
        plt.title('Result of Histogram Equalization')
        plt.legend()
        plt.savefig('Results/histogram_equalization_result' + str(random.randint(10000000, 99999999)) + '.png')

    def gamma_correction(self):
        gamma, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter gamma:\nExamples:\n1.1\n3")
        if done and re.match("^[0-9]\d*(\.\d+)?$", gamma):
            curr_img, _ = self.undoStack[-1]
            new_img = self._get_HSL(curr_img, False)
            new_img = transforms.power_law_transformation(new_img, float(gamma))
            new_img = self._get_RGB(new_img)
            new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
            self.undoStack.append((new_img, new_img_filepath))
            self.display_image(new_img_filepath)

    def log_transform(self):
        curr_img, _ = self.undoStack[-1]
        new_img, max_intensity = self._get_HSL(curr_img, True)
        new_img = transforms.log_transformation(new_img, max_intensity)
        new_img = self._get_RGB(new_img)
        new_img_filepath = self._internal_save(Image.fromarray(new_img.astype(np.uint8)))
        self.undoStack.append((new_img, new_img_filepath))
        self.display_image(new_img_filepath)
            

    def invert_image(self):
        curr_img, _ = self.undoStack[-1]
        for i in range(curr_img.shape[0]):
            for j in range(curr_img.shape[1]):
                curr_img[i][j] = 255 - curr_img[i][j]
        new_img_filepath = self._internal_save(Image.fromarray(curr_img.astype(np.uint8)))
        self.undoStack.append((curr_img, new_img_filepath))
        self.display_image(new_img_filepath)



    def get_channel(self):
        name, done = QtWidgets.QInputDialog.getText(self, "Input Dialog", "Enter R, G or B\nExample:\nR")
        curr_img, _ = self.undoStack[-1]
        if done and re.match("R|G|B", name):
            if name == "R":
                red_img = curr_img[:, :, 0]
                red_img_path = self._internal_save(Image.fromarray(red_img.astype(np.uint8)))
                self.undoStack.append((red_img, red_img_path)) 
                self.display_image(red_img_path)
            elif name == "G":
                green_img = curr_img[:, :, 1]
                green_img_path = self._internal_save(Image.fromarray(green_img))
                self.undoStack.append((green_img, green_img_path)) 
                self.display_image(green_img_path)
            else:
                blue_img = np.array(curr_img)[:, :, 2]
                blue_img_path  = self._internal_save(Image.fromarray(blue_img))
                self.undoStack.append((blue_img, blue_img_path)) 
                self.display_image(blue_img_path)
        
    def to_grayscale(self):
        curr_img, _ = self.undoStack[-1]
        new_img = to_grayscale(curr_img)
        new_img_path = self._internal_save(Image.fromarray(new_img.astype('uint8')))
        self.undoStack.append((new_img, new_img_path))
        self.display_image(new_img_path)

            




            




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
    sys.exit(app.exec_())
    
