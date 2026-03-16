import numpy as np

def kingMoves(board_size, position):
    rows, cols = board_size
    r0, c0 = position

    r = np.arange(rows)[:, None]   # kolumna indeksów wierszy
    c = np.arange(cols)[None, :]   # wiersz indeksów kolumn

    return np.maximum(np.abs(r - r0), np.abs(c - c0))
