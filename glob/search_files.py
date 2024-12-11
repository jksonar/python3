
import glob

# Find Python Files
python_files = glob.glob("*.py")
print(python_files)

# Find Images
image_files = glob.glob("images/*.jpg") + glob.glob("images/*.png")
print(image_files)
