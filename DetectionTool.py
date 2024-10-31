import cv2
import sys
from ultralytics import YOLO

def main(image_path):
    pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python DetectionTool.py <image_path>")
    else:
        main(sys.argv[1])