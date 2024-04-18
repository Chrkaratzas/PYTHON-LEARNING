import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace


class FaceRecognitionApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Load an image using OpenCV
        self.verification_image = 'img.png'

        # Open the video source
        self.vid = cv2.VideoCapture(0)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Button that lets the user verify face
        self.btn_verify = ttk.Button(window, text="Verify Face", width=15, command=self.verify_face)
        self.btn_verify.pack(anchor=tk.CENTER, expand=True)

        # Button to exit program
        self.btn_quit = ttk.Button(window, text="Quit", width=15, command=self.window.destroy)
        self.btn_quit.pack(anchor=tk.CENTER, expand=True)

        # Update & delay
        self.delay = 10
        self.update()

        self.window.mainloop()

    def verify_face(self):
        # Capture a frame for verification
        ret, frame = self.vid.read()
        cv2.imwrite('current_frame.jpg', frame)
        try:
            # Verify using DeepFace
            result = DeepFace.verify(self.verification_image, 'current_frame.jpg')
            if result['verified']:
                print("Face verified!")
                folder_path = r"C:\Users\User\Desktop\personal data"
                os.startfile(folder_path)


            else:
                print("Face not verified!")
        except Exception as e:
            print("Verification error:", e)

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()
        if ret:
            # Convert the image from BGR color (which OpenCV uses) to RGB color
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(self.delay, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


# Create a window and pass it to the FaceRecognitionApp object
FaceRecognitionApp(tk.Tk(), "Tkinter and OpenCV")


