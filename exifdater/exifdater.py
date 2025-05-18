#!python3
# program set date of image from EXIt origin date
print("testExifDater 0.01")
# plan
# read parameters
# readfile
# read exif
# extract date from EXIF
# set date of file form EXIT
# batch procesing
# display information onscreen
import importlib.util





def is_library_installed(library_name):
    return importlib.util.find_spec(library_name) is not None

# Example usage
library_name = 'Pillow'
if is_library_installed(library_name):
   print(f"{library_name} is installed.")
else:
   print(f"{library_name} is not installed.")


