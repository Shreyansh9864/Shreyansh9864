import cv2
import mediapipe as mp

# Initialize VideoCapture
cap = cv2.VideoCapture(0)

# Initialize MediaPipe FaceMesh and Drawing utilities
mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils
mp_draw_style=mp.solutions.drawing_styles


# Create FaceMesh instance
face_mesh = mp_face.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# Drawing specifications
draw_spec = mp_draw.DrawingSpec(thickness=1, color=(0, 255, 25), circle_radius=1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to access the camera.")
        break

    # Convert the frame to RGB (MediaPipe requires RGB format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for face landmarks
    results = mp_face.FaceMesh(refine_landmarks=True).process(rgb_frame)

    # If landmarks are detected, draw them
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_draw.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style(),

            )


            mp_draw.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_draw_style.get_default_face_mesh_tesselation_style()
            )

    # Display the frame
    cv2.imshow("Face Landmark Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
