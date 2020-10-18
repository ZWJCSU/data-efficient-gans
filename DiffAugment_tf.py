# Differentiable Augmentation for Data-Efficient GAN Training
# Shengyu Zhao, Zhijian Liu, Ji Lin, Jun-Yan Zhu, and Song Han
# https://arxiv.org/pdf/2006.10738

import tensorflow as tf


def DiffAugment(x, policy='', channels_first=False):

    return x


def rand_brightness(x):

    return x


def rand_saturation(x):

    return x


def rand_contrast(x):

    return x


def rand_translation(x, ratio=0.125):
 #
    return x


def rand_cutout(x, ratio=0.5):

    return x


AUGMENT_FNS = {
    'color': [rand_brightness, rand_saturation, rand_contrast],
    'translation': [rand_translation],
    'cutout': [rand_cutout],
}
