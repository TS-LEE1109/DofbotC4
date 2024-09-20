import cv2
import time
from ultralytics import YOLO

# Load YOLOv8 model (juicy1.pt file)
model = YOLO('/home/juicy/Juicy_code/best.pt')

# Camera setup (depth camera index, default is 0)
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Camera could not be opened.")
    exit()

time.sleep(2)  # Allow time for the camera to warm up

# Function to pour water (function to control the juicy robot arm)
def pour_water():
    # Robot arm control code (controlling motor movements)
    print("Robot arm is pouring water.")
    # Add code to set the angles or control the movements of the robot arm
    # motor.move_to_position(...)
    # motor.pour_water(...)

# Object detection function (detect objects using YOLOv8)
def detect_object(frame):
    results = model(frame)  # Process the frame using the YOLO model
    boxes = results[0].boxes.xyxy  # Bounding box coordinates
    labels = results[0].boxes.cls  # Class labels (as numbers)
    return labels, boxes

# Initialize object state (0: cup is upside down, 1: cup is upright)
object_state = 0

while True:
    # Read real-time frames from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to retrieve frame from the camera.")
        break

    # Detect objects using the YOLO model
    labels, boxes = detect_object(frame)

    # Check if the cup is placed in the correct position
    for label in labels:
        if label == 1:  # If class ID is 1, the cup is placed correctly
            object_state = 1  # Change object state to 1

    # If object state becomes 1, execute the pouring action
    if object_state == 1:
        print("The cup is correctly positioned. Starting water pouring action.")
        pour_water()  # Call the function to pour water
        break  # Exit the loop after pouring once

    # Display the result
    cv2.imshow('Detection', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()


