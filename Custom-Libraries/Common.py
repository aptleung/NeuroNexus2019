"""
This is the Common library for all functions related to Brain scans i/o
"""

import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib


def retrieve_scan(location):
    """
    Retrieves the specified Brain Scan from storage

    :param location: Location of Brain scan along with file name
           Ex)  /Users/jamesperalta/Dev/Test.nii

    :return scan: Brain scan as a numpy array
    """
    scan = nib.load(location)
    scan = np.array(scan.dataobj)
    return scan


def show_slice(image):
    """
    Displays the image passed

    :param image: The image as a numpy array
    """
    plt.imshow(image)


def show_images(images, cols=1, titles=None):
    """
    Display a list of images in a single figure with matplotlib.

    Parameters
    ---------
    images: List of np.arrays compatible with plt.imshow.

    cols (Default = 1): Number of columns in figure (number of rows is set to np.ceil(n_images/float(cols))).

    titles: List of titles corresponding to each image. Must have the same length as titles.
    """
    assert ((titles is None) or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1, n_images + 1)]
    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles)):
        a = fig.add_subplot(cols, np.ceil(n_images / float(cols)), n + 1)
        if image.ndim == 2:
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    plt.show()