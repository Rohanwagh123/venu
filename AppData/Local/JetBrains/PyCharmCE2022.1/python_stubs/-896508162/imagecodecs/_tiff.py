# encoding: utf-8
# module imagecodecs._tiff
# from F:\Aanaconda\lib\site-packages\imagecodecs\_tiff.cp39-win_amd64.pyd
# by generator 1.147
""" TIFF codec for the imagecodecs package. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as numpy # F:\Aanaconda\lib\site-packages\numpy\__init__.py
from imagecodecs._shared import _log_warning, _set_attributes


# Variables with simple values

__version__ = '2021.6.8'

# functions

def tiff_check(*args, **kwargs): # real signature unknown
    """ Return True if data likely contains a TIFF image. """
    pass

def tiff_decode(*args, **kwargs): # real signature unknown
    """
    Return numpy array from TIFF image.
    
        By default the image from the first directory/page is returned.
        If index is None, all images in the file with matching shape and
        dtype are returned in one array.
    
        If asrgb is True, return decoded image as RGBA32.
        Return JPEG compressed images as 8-bit Grayscale or RGB24.
        Return images stored in CMYK colorspace as RGB24.
    
        The libtiff library does not correctly handle truncated ImageJ hyperstacks,
        SGI depth, STK, LSM, and many other bio-TIFF files.
    """
    pass

def tiff_encode(*args, **kwargs): # real signature unknown
    """ Return TIFF image from numpy array. """
    pass

def tiff_version(*args, **kwargs): # real signature unknown
    """ Return libtiff library version string. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class _TIFF(object):
    """ TIFF Constants. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BIGENDIAN = 19789
    COMPRESSION_ADOBE_DEFLATE = 8
    COMPRESSION_DEFLATE = 32946
    COMPRESSION_JPEG = 7
    COMPRESSION_LZMA = 34925
    COMPRESSION_LZW = 5
    COMPRESSION_NONE = 1
    COMPRESSION_PACKBITS = 32773
    COMPRESSION_WEBP = 50001
    COMPRESSION_ZSTD = 50000
    LITTLEENDIAN = 18761
    PHOTOMETRIC_MASK = 4
    PHOTOMETRIC_MINISBLACK = 1
    PHOTOMETRIC_MINISWHITE = 0
    PHOTOMETRIC_PALETTE = 3
    PHOTOMETRIC_RGB = 2
    PHOTOMETRIC_SEPARATED = 5
    PHOTOMETRIC_YCBCR = 6
    PLANARCONFIG_CONTIG = 1
    PLANARCONFIG_SEPARATE = 2
    PREDICTOR_FLOATINGPOINT = 3
    PREDICTOR_HORIZONTAL = 2
    PREDICTOR_NONE = 1
    VERSION_BIG = 43
    VERSION_CLASSIC = 42
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'imagecodecs._tiff', '__doc__': 'TIFF Constants.', 'VERSION_CLASSIC': 42, 'VERSION_BIG': 43, 'BIGENDIAN': 19789, 'LITTLEENDIAN': 18761, '__dict__': <attribute '__dict__' of '_TIFF' objects>, '__weakref__': <attribute '__weakref__' of '_TIFF' objects>, 'COMPRESSION_NONE': 1, 'COMPRESSION_LZW': 5, 'COMPRESSION_JPEG': 7, 'COMPRESSION_PACKBITS': 32773, 'COMPRESSION_DEFLATE': 32946, 'COMPRESSION_ADOBE_DEFLATE': 8, 'COMPRESSION_LZMA': 34925, 'COMPRESSION_ZSTD': 50000, 'COMPRESSION_WEBP': 50001, 'PHOTOMETRIC_MINISWHITE': 0, 'PHOTOMETRIC_MINISBLACK': 1, 'PHOTOMETRIC_RGB': 2, 'PHOTOMETRIC_PALETTE': 3, 'PHOTOMETRIC_MASK': 4, 'PHOTOMETRIC_SEPARATED': 5, 'PHOTOMETRIC_YCBCR': 6, 'PLANARCONFIG_CONTIG': 1, 'PLANARCONFIG_SEPARATE': 2, 'PREDICTOR_NONE': 1, 'PREDICTOR_HORIZONTAL': 2, 'PREDICTOR_FLOATINGPOINT': 3})"


TIFF = _TIFF


class TiffError(RuntimeError):
    """ TIFF Exceptions. """
    def __init__(self, *args, **kwargs): # real signature unknown
        """ Initialize Exception from string or memtif capsule. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021FFDD0B850>'

__spec__ = None # (!) real value is "ModuleSpec(name='imagecodecs._tiff', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021FFDD0B850>, origin='F:\\\\Aanaconda\\\\lib\\\\site-packages\\\\imagecodecs\\\\_tiff.cp39-win_amd64.pyd')"

__test__ = {}

