# 🍅 Tomato Quality Classifier

A desktop application that uses computer vision (OpenCV) to classify tomatoes into quality categories — **Good**, **Edible**, or **InEdible** — based on their color. The application features a graphical interface built with Tkinter.

## 🔍 Features

- Automatically classifies tomatoes based on HSV color ranges.
- Displays classification results with an overlay on the image.
- Calculates the total price based on tomato quality.
- Presents a summary report with categorized tomatoes and respective prices.
- Simple and intuitive GUI for smooth interaction.

## 🧠 Classification Logic

The classification is based on color segmentation using HSV:
- **Good**: Dominantly red tomatoes.
- **Edible**: Dominantly yellow tomatoes.
- **InEdible**: Dominantly green or other non-ideal colors.

## 💸 Price Table

| Quality    | Price per Tomato (₹) |
|------------|----------------------|
| Good       | 100                  |
| Edible     | 80                   |
| InEdible   | 30                   |

## 🖼️ Image Input

Place your images in the `./images` directory before launching the app. The app processes all images in that folder.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/prajwal023/tomato_classifier.git
   cd tomato_classifier

2. Install dependencies (if not already):
   pip install opencv-python numpy

3. Make sure you have an images/ folder in the same directory with some tomato images inside.

4. Run the application:
   python app.py

## 🖥️ GUI Preview
Press Start Sorting to begin classification.

Press spacebar to move to the next image after classification.

A detailed report window will open after all images are processed.



## 🧑‍💻 Author
Developed by [Prajwal](https://github.com/prajwal023)





   

