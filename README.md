# registration-viewer
Tool to view brain registration (i.e. coregistration and normalization) alignment



# Dependencies
Make sure you have the following libraries installed:

1. Nilearn
2. Matplotlib

# Use

Download the `viewreg.py` file or this project. Navigate to the directory and run the file in the command line:

`python viewreg.py -o /path/to/output_file.pdf -i /path/to/input_file.nii -r /path/to/reference_file.nii`

The output is a `.pdf` file showing slices along the saggital, frontal, and transverse planes. Note that the reference image (`-r`) is optional. If not provided, a standard 2mm MNI template will be used. As well, you can set the number of slices (`-n`) to view, and the title of the plots (`-t`); these arguments are optional and default to 8 and None, respectively.

You can also use `-h` to display the help:
```
-o O        Output file (must include .pdf extension)
-i I        Input file (i.e. file aligned to target)
-r R        Reference file used for alignment. If not provided, a 2mm MNI
            template is used
-n N        Number of slices to display
-t T        Title
```
