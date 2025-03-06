import cv2
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("face_liveness_model.h5")

# Define class labels
class_labels = ['Spoof', 'Live']

def preprocess_frame(frame):
    """Preprocess frame for model prediction."""
    frame = cv2.resize(frame, (150, 150))  # Resize to model input size
    frame = frame.astype('float32') / 255.0  # Normalize
    frame = np.expand_dims(frame, axis=0)  # Add batch dimension
    return frame

def detect_liveness():
    """Capture webcam feed and perform real-time liveness detection."""
    cap = cv2.VideoCapture(0)  # Open webcam
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Camera not accessible")
            break
        
        processed_frame = preprocess_frame(frame)
        prediction = model.predict(processed_frame)[0][0]
        label = class_labels[int(prediction > 0.5)]  # Threshold at 0.5
        
        # Display result
        color = (0, 255, 0) if label == 'Live' else (0, 0, 255)
        cv2.putText(frame, f'Liveness: {label}', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow('Face Liveness Detection', frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Run the webcam detection
detect_liveness()
