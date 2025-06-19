# Dominant Color Extractor

A Python CLI tool that extracts dominant colors from an image using K-means clustering. The extracted color hex codes are optionally visualized and automatically copied to your clipboard.

## 📁 Features

* Detects top **K** dominant colors in an image
* Outputs HEX color codes
* Optional color bar visualization using `matplotlib`
* Automatically copies color codes to clipboard
* Supports `.jpg`, `.png`, and other OpenCV-supported image formats

## 🚀 Requirements

Install the dependencies:

```bash
pip install opencv-python matplotlib scikit-learn pyperclip
```

## 📅 Usage

### Run the script

```bash
python dominant_color_extractor.py path/to/image.jpg -k 5 --show
```

### Arguments:

* `image_path` (str): Path to the image file
* `-k` (int): Number of dominant colors to extract (default: 5)
* `--show`: Optional flag to display a color bar of the extracted colors

### Example

```bash
python dominant_color_extractor.py image.jpg -k 3 --show
```

**Output:**

```
Processing image: image.jpg
Extracting dominant colors...
Dominant color codes:
#d3a875
#8e5e3b
#372a1c
Copied 3 color codes to clipboard!
```

## 🔧 Functions

### `load_image(image_path)`

Loads an image and converts it to RGB format.

### `resize_image(image, width=250)`

Resizes the image to a manageable size for faster processing.

### `get_dominant_colors(image, k=5)`

Uses K-means clustering to identify the dominant colors.

### `rgb_to_hex(rgb)`

Converts RGB to hexadecimal string.

### `display_colors(colors)`

Displays the dominant colors visually.

### `save_to_clipboard(color_codes)`

Copies the HEX color codes to the clipboard using `pyperclip`.

## ⚠️ Notes

* `KMeans` clustering results may vary slightly between runs
* If clipboard functionality fails, ensure `pyperclip` is installed and supports your OS

