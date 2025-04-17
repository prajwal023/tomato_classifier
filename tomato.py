import cv2
import numpy as np
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

sys.stdout.reconfigure(encoding='utf-8')

prices = {
    "Good": 100,
    "Edible": 80,
    "InEdible": 30
}

qualities = {
    "Good": [],
    "Edible": [],
    "InEdible": []
}

def classify_quality(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not open or find the image: {image_path}")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    red_lower1 = np.array([0, 100, 100])
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([160, 100, 100])
    red_upper2 = np.array([180, 255, 255])

    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])

    green_lower = np.array([35, 100, 100])
    green_upper = np.array([85, 255, 255])

    red_mask = cv2.bitwise_or(cv2.inRange(hsv, red_lower1, red_upper1),
                              cv2.inRange(hsv, red_lower2, red_upper2))
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)

    red_count = cv2.countNonZero(red_mask)
    yellow_count = cv2.countNonZero(yellow_mask)
    green_count = cv2.countNonZero(green_mask)

    if red_count > yellow_count and red_count > green_count:
        quality = "Good"
    elif yellow_count > red_count and yellow_count > green_count:
        quality = "Edible"
    else:
        quality = "InEdible"

    qualities[quality].append(image_path)

    # Resize to fixed dimensions
    image = cv2.resize(image, (500, 400))  # Width x Height

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, quality, (10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Tomato Classification", image)
    while True:
        key = cv2.waitKey(0)
        if key == ord(' '):
            break
    cv2.destroyAllWindows()



def classify_all_images():
    folder = './images'
    if not os.path.exists(folder):
        messagebox.showerror("Error", "Image folder not found!")
        return

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    if not files:
        messagebox.showinfo("No Images", "No images found in the directory.")
        return

    for f in files:
        classify_quality(os.path.join(folder, f))

    display_results()


def display_results():
    result_window = tk.Toplevel()
    result_window.title("Sorting Results")
    result_window.configure(bg="#f0f4f7")
    result_window.geometry("700x600")

    title = tk.Label(result_window, text="Tomato Sorting Report", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#2c3e50")
    title.pack(pady=20)

    for quality, items in qualities.items():
        frame = tk.LabelFrame(result_window, text=quality + f" Tomatoes (₹{prices[quality]} each)",
                              font=('Arial', 12, 'bold'), padx=10, pady=10, bg="#ecf0f1", fg="#2c3e50")
        frame.pack(fill="x", padx=20, pady=10)

        listbox = tk.Listbox(frame, width=80, height=min(5, len(items)))
        for item in items:
            listbox.insert(tk.END, item)
        listbox.pack()

        summary_text = f"Total: {len(items)} × ₹{prices[quality]} = ₹{len(items) * prices[quality]}"
        summary_label = tk.Label(frame, text=summary_text, font=('Arial', 11), bg="#ecf0f1", fg="#16a085")
        summary_label.pack(pady=(5, 0))


def launch_app():
    root = tk.Tk()
    root.title("Tomato Sorting System")
    root.geometry("500x400")
    root.configure(bg="#f0f4f7")

    # Style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Helvetica", 12), padding=10, background="#3498db", foreground="white")
    style.map("TButton", background=[("active", "#2980b9")])

    style.configure("TLabel", background="#f0f4f7", font=("Helvetica", 12))

    heading = tk.Label(root, text="🍅 Tomato Quality Classifier 🍅", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#2c3e50")
    heading.pack(pady=40)

    start_button = ttk.Button(root, text="Start Sorting", command=classify_all_images)
    start_button.pack(pady=10)

    about = tk.Label(root, text="Press spacebar to skip each image after classification",
                     font=("Arial", 10, "italic"), fg="#7f8c8d", bg="#f0f4f7")
    about.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    launch_app()
