import cv2 as cv
import sys

# Keycode definitions
ESC_KEY = 27
Q_KEY = 113

def main():
    # Define variables
    filename = sys.argv[1] if len(sys.argv) > 1 else 'autoroute2.avi'

    # Reading the image (and forcing it to grayscale)
    cap = cv.VideoCapture(filename)

    # Making sure the capture has opened successfully
    if not cap.isOpened():
        # Capture opening has failed we cannot do anything :'(
        print("Capture opening has failed we cannot do anything :'(")
        sys.exit()

    # Creating a window to display some images
    cv.namedWindow("Original video")
    cv.namedWindow("Gray video")
    
    # A key that we use to store the user keyboard input
    key = None
    # Waiting for the user to press ESCAPE before exiting the application
    
    while key != ESC_KEY and key != Q_KEY:
        ret, im = cap.read()
        # Verify if the frame read was successful
        if not ret:
            print("Fin de la vidéo ou erreur de lecture.")
            break

        # Verify that the frame is not empty before displaying it
        if im is None or im.size == 0:
            print("Frame vide ou invalide.")
            continue

        # Turning im into grayscale and storing it in imGray
        imGray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        
        # Displaying the images
        cv.imshow("Original video", im)
        cv.imshow("Gray video", imGray)
        
        # Look for pollKey documentation
        key = cv.pollKey()
    
    # Release cap
    cap.release()
    # Destroying all OpenCV windows
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    
    
    


