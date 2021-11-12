import pandas as pd
import numpy as np
import h5py as h5

def maxlength(filename):
    ll = []
    def _get_length(name, item):
        ll.append(len(name))
    with h5.File(filename) as f:
        f.visititems(_get_length)
    return(np.max(ll))

def log_hdf_file(hdf_file, maxlen):
    def _print_item(name, item):
        if hasattr(item, 'shape'):
            if str(item.dtype) == "object":
                print(("   {:{}}".format(name, maxlen))+(" | {}".format(str(item.shape)))+(" | string"))
            else:
                print(("   {:{}}".format(name, maxlen))+(" | {}".format(str(item.shape)))+(" | {}".format(item.dtype)))
        else:
            print(name)

    hdf_file.visititems(_print_item)

def h5ls(filename):
    maxlen = maxlength(filename)
    print(maxlen)
    with h5.File(filename) as f:
        log_hdf_file(f, maxlen)