"""Registration viewing tool"""

import argparse
from nilearn.plotting import plot_anat
import matplotlib.pyplot as plt


def registration_report(fn, in_file, target=None, nslices=8,
                        title=None):
    """Creates a .pdf file showing registration alignment.
    
    Shows registration alignment along the transverse, sagittal, and frontal
    planes. fn is the output file path/name. in_file is the registed file. 
    target is the reference file used for alignment. If set to None, a default
    2mm MNI template is used. nlsices sets the number of slices to view for
    each plane. title sets the title for the figures.
    """

    fig, ax = plt.subplots(3, 1, figsize=(20, 25))
    ax[0].set_title(title, fontsize=30)

    for i, j in enumerate(['x', 'y', 'z']):
        plot_anat(
            in_file, draw_cross=False, cut_coords=nslices,
            display_mode=j, axes=ax[i]
        ).add_edges(target)

    # save off subplot figure into png
    fig.savefig(fn)


if __name__ == '__main__':

    parser = argparse.ArgumentParser('View subject registration')
    parser.add_argument('-o', help='Output file (must include .pdf extension)')
    parser.add_argument('-i', help='Input file (i.e. file aligned to target)')
    parser.add_argument('-r', help='Reference file used for alignment. If not '
                        'provided, a 2mm MNI template is used',
                        default=None)
    parser.add_argument('-n', help='Number of slices to display', default=8)
    parser.add_argument('-t', help='Title', default=None)
    args = parser.parse_args()
    registration_report(args.o, args.i, args.r, args.n, args.t)
