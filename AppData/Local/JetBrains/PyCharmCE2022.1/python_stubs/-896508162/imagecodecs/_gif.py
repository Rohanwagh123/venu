# encoding: utf-8
# module imagecodecs._gif
# from F:\Aanaconda\lib\site-packages\imagecodecs\_gif.cp39-win_amd64.pyd
# by generator 1.147
""" GIF codec for the imagecodecs package. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as numpy # F:\Aanaconda\lib\site-packages\numpy\__init__.py
from imagecodecs._shared import _log_warning, _set_attributes


# Variables with simple values

__version__ = '2021.7.30'

# functions

def gif_check(*args, **kwargs): # real signature unknown
    """ Return True if data likely contains a GIF image. """
    pass

def gif_decode(*args, **kwargs): # real signature unknown
    """
    Decode GIF image to numpy array.
    
        By default all images in the file are returned in one array.
        If an image index is specified, ignore the disposal mode and return the
        image data on black background.
    """
    pass

def gif_encode(*args, **kwargs): # real signature unknown
    """ Return GIF image from numpy array. """
    pass

def gif_version(*args, **kwargs): # real signature unknown
    """ Return giflib library version string. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class GIF(object):
    """ Gif Constants. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'imagecodecs._gif', '__doc__': 'Gif Constants.', '__dict__': <attribute '__dict__' of 'GIF' objects>, '__weakref__': <attribute '__weakref__' of 'GIF' objects>})"


class GifError(RuntimeError):
    """ GIF Exceptions. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000222F3E0B850>'

__spec__ = None # (!) real value is "ModuleSpec(name='imagecodecs._gif', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000222F3E0B850>, origin='F:\\\\Aanaconda\\\\lib\\\\site-packages\\\\imagecodecs\\\\_gif.cp39-win_amd64.pyd')"

__test__ = {}

