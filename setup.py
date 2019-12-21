import os

try:
    os.system("pip3 install Flask")
    os.system("pip install Keras==2.2.4")
    os.system("pip install Keras==2.2.4")
    os.system("pip install numpy==1.15.4")
    os.system("pip install Pillow")
    os.system("pip install tensorflow")
    os.system("pip install matplotlib")
    print("All dependencies have been installed!")

except:
    print("An error occurred, please make sure you have Python 3.6 installed")
