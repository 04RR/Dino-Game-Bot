# Dino-Game-Bot
Google chrome Dino game bot powered by Computer Vision and Deep Learning. 


# MakeTrainingData.py
This program uses win32api and win32ui to grab the screen and log the key presses. The images that are got from screen grabbing are then processed (Grayscale) using OpenCV. The images and key logs are then used to make the training set for the model. 

# GrabScreen.py
This program has the get_screen function that uses win32api to grab the screen.
