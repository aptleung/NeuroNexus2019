from sklearn.feature_extraction import image
from Common import show_images, retrieve_scan, show_slice
import numpy as np
import matplotlib.pyplot as plt
import math
from keras.utils import np_utils
import keras


def patchify_slice(my_slice, width, height):
    '''
    :param slice: Slice you would like to extract patches from
    :param width: Width of each patch
    :param height: Height of each patch
    :return:
    '''
    return image.extract_patches_2d(my_slice, (width, height))


def retrieve_slice(slice_location):
    '''
    :param slice_location: Location of the slice
    :return: Slice as a numpy array
    '''
    scan = plt.imread(slice_location)

    # Pre-process the scan after reading it
    scan = norm_slice(scan)

    return scan


def norm_slice(my_slice):
    '''
    INPUT:  (1) a single slice of any given modality (excluding gt)
    OUTPUT: normalized slice
    '''
    b, t = np.percentile(my_slice, (0.5,99.5))
    my_slice = np.clip(my_slice, b, t)
    if np.std(my_slice) == 0:
        return my_slice
    else:
        return (my_slice - np.mean(my_slice)) / np.std(my_slice)


def label_patches(patches):
    '''
    Always pass in square patches with an odd width and height
    This is needed for use to calculate the center pixel

    :param patches: Patches you would like to label
    :return:
    '''
    labels_list = []
    dim = math.ceil(len(patches[0, 1, :]) / 2)

    for patch in patches:
        if patch[dim, dim] != 0:
            labels_list.append("1")
        else:
            labels_list.append("0")

    print(labels_list[30080:30120])
    return keras.utils.to_categorical(labels_list, num_classes=2)