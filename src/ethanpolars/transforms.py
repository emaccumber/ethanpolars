"""
Transform functions for Polars dataframes.

This module contains implementations of various transformation functions that can
be used with Polars dataframes for common data transformation tasks.
"""

import numpy as np
from numba import float64, guvectorize  # type: ignore


@guvectorize([(float64[:], float64[:])], "(n)->(n)")  # type: ignore[misc]
def demean(arr: np.ndarray, result: np.ndarray) -> None:
    """
    Subtract the mean from each non-NaN value in an array.
    
    This function computes the mean of all non-NaN values in the input array
    and subtracts it from each non-NaN value. NaN values in the input remain
    NaN in the output.
    
    Parameters
    ----------
    arr : np.ndarray
        Input array with values to demean
    result : np.ndarray
        Output array to store demeaned values
        
    Notes
    -----
    The function is optimized using Numba's guvectorize, making it efficient
    for large arrays.
    
    Examples
    --------
    >>> import polars as pl
    >>> import numpy as np
    >>> from ethanpolars import demean
    >>> 
    >>> # With a Polars Series
    >>> s = pl.Series([1.0, 2.0, 3.0, None, 5.0])
    >>> s.cast(pl.Float64).to_numpy()
    array([ 1.,  2.,  3., nan,  5.])
    >>> 
    >>> # With a Polars DataFrame
    >>> df = pl.DataFrame({"values": s})
    >>> # Apply demean with map_batches on expression
    >>> result = df.select(
    ...     pl.col("values").cast(pl.Float64).map_batches(lambda x: pl.Series(demean(x.to_numpy())))
    ... ).get_column("values")
    >>> result
    shape: (5,)
    Series: '' [f64]
    [
        -1.75
        -0.75
        0.25
        null
        2.25
    ]
    """
    total = 0.0
    count = 0

    for value in arr:
        if not np.isnan(value):
            total += value
            count += 1

    if count > 0:
        mean = total / count
    else:
        mean = np.nan

    for i, value in enumerate(arr):
        if not np.isnan(value):
            result[i] = value - mean
        else:
            result[i] = np.nan