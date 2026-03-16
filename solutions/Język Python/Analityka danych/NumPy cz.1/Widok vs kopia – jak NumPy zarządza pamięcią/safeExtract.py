import numpy as np

def safe_extract(original, extracted):
    if extracted.base is original:
        return 'view'
    else:
        return 'copy'
