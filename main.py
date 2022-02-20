import cv2 #pip install opencv-python
import os
import platform

# SETTINGS #
SHOW_REAL_VIDEO = True   # Set this to True to get real camera video from cv2


def convert_row_to_ascii(row):
    # 17-long
    ORDER = (' ',' ',' ',' ', '.', "'", ',', ':', ';', 'c', 'l',
             'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N','M','W','8','B','@','$')
    return tuple(ORDER[int(x / (255 / len(ORDER)))] for x in row)[::-1]


def convert_to_ascii(input_grays):
    return tuple(convert_row_to_ascii(row+row+row) for row in input_grays)


def print_array(input_ascii_array):
    
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")
    print('\n'.join((''.join(row) for row in input_ascii_array)), end='')


cap = cv2.VideoCapture(0)

while(cv2.waitKey(1) & 0xFF != ord('q')):
  
    '''
    you can set the screen_height and screen_width according to your wish but The bigger the numbers the more your camera will lag
    '''
    screen_height = 70 
    screen_width = 140 
    # Get screensize for reduction
    if(platform.system()=="Darwin"): # For getting a better screen size and works only for MAC
        screen_height, screen_width = os.popen('stty size', 'r').read().split()

    # Get image data
    ret, frame = cap.read()

    # Convert data to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reduce grayscale array to proper resolution
    reduced = cv2.resize(gray, (int(screen_width), int(screen_height)))

    # Plug in reduced resolution numpy array for ascii converter function
    converted = convert_to_ascii(reduced)
    print_array(converted)

    # Display the resulting frame
    if SHOW_REAL_VIDEO:
        cv2.imshow('frame',gray)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
