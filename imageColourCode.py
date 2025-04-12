import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pyperclip
import argparse
import os
from collections import Counter

def load_image(image_path):
    """Load image from path and convert to RGB"""
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def resize_image(image, width=250):
    """Resize image while maintaining aspect ratio"""
    height = int((image.shape[0] / image.shape[1]) * width)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

def get_dominant_colors(image, k=5):
    """Extract dominant colors using K-means clustering"""
    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    
    # Get the cluster centers (dominant colors)
    colors = kmeans.cluster_centers_
    
    # Count how many pixels belong to each cluster
    counts = Counter(kmeans.labels_)
    
    # Sort colors by frequency
    sorted_colors = sorted([(count, color) for color, count in zip(colors, counts.values())], 
                          key=lambda x: x[0], reverse=True)
    
    return [color for (count, color) in sorted_colors]

def rgb_to_hex(rgb):
    """Convert RGB values to hex color code"""
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def display_colors(colors):
    """Display the dominant colors in a plot"""
    plt.figure(figsize=(8, 2))
    for i, color in enumerate(colors):
        plt.subplot(1, len(colors), i+1)
        plt.imshow([[color]])
        plt.axis('off')
        plt.title(rgb_to_hex(color))
    plt.show()

def save_to_clipboard(color_codes):
    """Copy color codes to clipboard"""
    text = "\n".join(color_codes)
    pyperclip.copy(text)
    print(f"Copied {len(color_codes)} color codes to clipboard!")

def process_image(image_path, k=5, show_colors=False):
    """Main function to process the image"""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    print(f"Processing image: {image_path}")
    image = load_image(image_path)
    resized = resize_image(image)
    
    print("Extracting dominant colors...")
    colors = get_dominant_colors(resized, k)
    color_codes = [rgb_to_hex(color) for color in colors]
    
    print("Dominant color codes:")
    for code in color_codes:
        print(code)
    
    if show_colors:
        display_colors(colors)
    
    save_to_clipboard(color_codes)
    return color_codes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract dominant colors from an image')
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('-k', type=int, default=5, 
                       help='Number of dominant colors to extract (default: 5)')
    parser.add_argument('--show', action='store_true',
                       help='Show color visualization')
    
    args = parser.parse_args()
    
    try:
        # Install required packages if not available
        try:
            import cv2
            import pyperclip
        except ImportError:
            print("Installing required packages...")
            import subprocess
            subprocess.run(['pip', 'install', 'opencv-python', 'pyperclip', 'scikit-learn', 'matplotlib'])
        
        color_codes = process_image(args.image_path, args.k, args.show)
    except Exception as e:
        print(f"Error: {str(e)}")