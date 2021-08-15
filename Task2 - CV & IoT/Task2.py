#
#
#
# The Sparks Foundation - Computer Vision and Internet of Things
# 			              (Task from different Domain)
# GRIP August 21
# Task - 2
  
# Submitted By - Sanket Mathur
#
#
#

# importing required values
import numpy as np
import cv2

# constants and global values
WINDOW_NAME = 'Color Detection'
FONT = cv2.FONT_HERSHEY_SIMPLEX

height = weight = 0
scale = 1
posx = posy = -1

def track_mouse(event, x, y, flags, params):
    """Function to track the mouse and change the global parameters posx and posy"""
    
    global posx, posy

    # updating the pointer values on position change
    if event == cv2.EVENT_MOUSEMOVE:
        posx, posy = x, y

def place_color():
    """Function used to draw information about the color over the image"""

    # extracting the color of the pixel at which the cursor is hovering
    color = tuple(map(int, img[posy][posx]))
    # inverting the color of the pixel to display the information better
    inv_color = tuple(map(lambda x : 255 - x, color))

    # formatting color value in RGB and Hex strings
    rgb_value = '({}, {}, {})'.format(*color)
    hex_value = '#{:02X}{:02X}{:02X}'.format(*color)

    # placing background layer to display the text
    cv2.rectangle(img, (10, height - 60), (width - 10, height - 10), color, -1)

    # placing the RGB and Hex values of the color over the placed layer
    cv2.putText(img, rgb_value, (30, height - 25), FONT, 1, inv_color, 2, cv2.LINE_AA)
    cv2.putText(img, hex_value, (width - 170, height - 25), FONT, 1, inv_color, 2, cv2.LINE_AA)

# reading the image and resizing it to be a maximum of 800 pixels in both axis
img = cv2.imread('./Pictures/Mountain.jpg')
height, width = img.shape[0], img.shape[1]

# scaling the image
scale = 800 / (height if height > width else width)
height = int(height * scale)
width = int(width * scale)

img = cv2.resize(img, (width, height))

# connecting the mouse callback to the event function we defiend
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, track_mouse)

# main loop of the program to display the image and update the values
while True:
    # place the color information over the image
    if posx >= 0 and posy >= 0:
        place_color()

    # display the image and apply the exit conditions
    cv2.imshow(WINDOW_NAME, img)
    if cv2.waitKey(40) & 0xFF == ord('q') or cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        break