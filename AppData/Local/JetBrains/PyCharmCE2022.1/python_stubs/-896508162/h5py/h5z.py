# encoding: utf-8
# module h5py.h5z
# from F:\Aanaconda\lib\site-packages\h5py\h5z.cp39-win_amd64.pyd
# by generator 1.147
""" Filter API and constants. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from h5py._objects import with_phil


# Variables with simple values

DISABLE_EDC = 0

ENABLE_EDC = 1

ERROR_EDC = -1

FILTER_ALL = 0

FILTER_CONFIG_DECODE_ENABLED = 2

FILTER_CONFIG_ENCODE_ENABLED = 1

FILTER_DEFLATE = 1
FILTER_ERROR = -1
FILTER_FLETCHER32 = 3
FILTER_LZF = 32000
FILTER_MAX = 65535
FILTER_NBIT = 5
FILTER_NONE = 0
FILTER_RESERVED = 256
FILTER_SCALEOFFSET = 6
FILTER_SHUFFLE = 2
FILTER_SZIP = 4

FLAG_DEFMASK = 255
FLAG_INVMASK = 65280
FLAG_MANDATORY = 0
FLAG_OPTIONAL = 1
FLAG_REVERSE = 256

FLAG_SKIP_EDC = 512

NO_EDC = 2

SO_FLOAT_DSCALE = 0
SO_FLOAT_ESCALE = 1

SO_INT = 2

SO_INT_MINBITS_DEFAULT = 0

SZIP_ALLOW_K13_OPTION_MASK = 1

SZIP_CHIP_OPTION_MASK = 2

SZIP_EC_OPTION_MASK = 4

SZIP_MAX_PIXELS_PER_BLOCK = 32

SZIP_NN_OPTION_MASK = 32

# functions

def filter_avail(*args, **kwargs): # real signature unknown
    """
    (INT filter_code) => BOOL
    
        Determine if the given filter is available to the library. The
        filter code should be one of:
    
        - FILTER_DEFLATE
        - FILTER_SHUFFLE
        - FILTER_FLETCHER32
        - FILTER_SZIP
    """
    pass

def get_filter_info(*args, **kwargs): # real signature unknown
    """
    (INT filter_code) => INT filter_flags
    
        Retrieve a bitfield with information about the given filter. The
        filter code should be one of:
    
        - FILTER_DEFLATE
        - FILTER_SHUFFLE
        - FILTER_FLETCHER32
        - FILTER_SZIP
    
        Valid bitmasks for use with the returned bitfield are:
    
        - FILTER_CONFIG_ENCODE_ENABLED
        - FILTER_CONFIG_DECODE_ENABLED
    """
    pass

def unregister_filter(*args, **kwargs): # real signature unknown
    """
    (INT filter_code) => BOOL
    
        Unregister a filter
    """
    pass

def _register_lzf(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

phil = None # (!) real value is '<h5py._objects.FastRLock object at 0x00000269039FD990>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026903AE04F0>'

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5z', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026903AE04F0>, origin='F:\\\\Aanaconda\\\\lib\\\\site-packages\\\\h5py\\\\h5z.cp39-win_amd64.pyd')"

__test__ = {}

