from collections import abc
from numbers import Number
from pathlib import Path
from warnings import warn

from numpy import ndarray
from torch import is_tensor

IMG_SUFFIX = ['.PNG', '.JPG', '.JPEG', 'TIFF', 'BMP']

VIDEO_SUFFIX = ['.MOV', '.MP4', '.AVI']


def is_dict(x) -> bool:
    return isinstance(x, dict)


def is_tuple(x) -> bool:
    return isinstance(x, tuple)


def is_list(x) -> bool:
    return isinstance(x, list)


def is_iterable(x) -> bool:
    return isinstance(x, abc.Iterable)


def is_sequence(x) -> bool:
    return isinstance(x, abc.Sequence)


def is_int(x) -> bool:
    return isinstance(x, int)


def is_str(x) -> bool:
    return isinstance(x, str)


def is_float(x) -> bool:
    return isinstance(x, float)


def is_number(x) -> bool:
    return isinstance(x, Number)


def is_numpy(x) -> bool:
    return isinstance(x, ndarray)


def is_torch(x) -> bool:
    return is_tensor(x)


def is_numpy_img(x) -> bool:
    '''
    x == ndarray (H x W x C)
    '''
    return is_numpy(x) and (x.ndim == 2 or (x.ndim == 3 and x.shape[-1] in [1, 3]))


def is_numpy_imgs(xs) -> bool:
    '''
    x == ndarray (H x W x C)
    '''
    for x in xs:
        if not(is_numpy(x) and (x.ndim == 2 or (x.ndim == 3 and x.shape[-1] in [1, 3]))):
            return False
    return True


def is_torch_img(x) -> bool:
    '''
    x == tensor (H x W x C)
    '''
    return is_numpy_img(x.cpu().numpy())


def is_image(x) -> bool:
    return is_numpy_img(x) or is_torch_img(x)


def is_img_file(x) -> bool:
    x = Path(x)
    cond1 = x.exists()
    cond2 = x.suffix.upper() in IMG_SUFFIX
    return cond1 and cond2


def is_video_file(x) -> bool:
    x = Path(x)
    cond1 = x.exists()
    cond2 = x.suffix.upper() in VIDEO_SUFFIX
    return cond1 and cond2


def is_file(x: str) -> bool:
    x = Path(x)
    return x.is_file()


def is_folder(x: str) -> bool:
    x = Path(x)
    return x.is_dir()


def is_path_exist(x) -> bool:
    return Path(x).exists()
