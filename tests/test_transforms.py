"""Tests for the transform functions in ethanpolars."""

import numpy as np
import polars as pl

from ethanpolars import demean


def test_demean_numpy():
    """Test the demean function with NumPy arrays."""
    # Test with simple array
    arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
    result = np.zeros_like(arr)
    demean(arr, result)
    
    # Mean of [1,2,3,4,5] is 3, so result should be [-2,-1,0,1,2]
    expected = np.array([-2.0, -1.0, 0.0, 1.0, 2.0], dtype=np.float64)
    np.testing.assert_array_almost_equal(result, expected)
    
    # Test with NaN values
    arr_with_nan = np.array([1.0, 2.0, np.nan, 4.0, 5.0], dtype=np.float64)
    result = np.zeros_like(arr_with_nan)
    demean(arr_with_nan, result)
    
    # Mean of [1,2,4,5] is 3, so result should be [-2,-1,nan,1,2]
    expected = np.array([-2.0, -1.0, np.nan, 1.0, 2.0], dtype=np.float64)
    np.testing.assert_array_almost_equal(result[~np.isnan(result)], 
                                         expected[~np.isnan(expected)])
    assert np.isnan(result[2]) and np.isnan(expected[2])
    
    # Test with all NaN values
    all_nan = np.array([np.nan, np.nan, np.nan], dtype=np.float64)
    result = np.zeros_like(all_nan)
    demean(all_nan, result)
    
    # Should return all NaNs
    assert np.all(np.isnan(result))


def test_demean_polars():
    """Test the demean function with Polars Series."""
    # Create a simple Polars Series
    s = pl.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    
    # Apply demean using expression map_batches
    df = pl.DataFrame({"value": s})
    result = df.select(pl.col("value").map_batches(lambda x: pl.Series(demean(x.to_numpy())))).get_column("value")
    
    # Verify result
    expected = pl.Series([-2.0, -1.0, 0.0, 1.0, 2.0])
    assert result.equals(expected)
    
    # Test with nulls
    s_with_nulls = pl.Series([1.0, 2.0, None, 4.0, 5.0])
    
    # Apply demean using expression map_batches
    df = pl.DataFrame({"value": s_with_nulls})
    result = df.select(
        pl.col("value").cast(pl.Float64).map_batches(lambda x: pl.Series(demean(x.to_numpy())))
    ).get_column("value")
    
    # Verify result
    expected = pl.Series([-2.0, -1.0, None, 1.0, 2.0])
    assert result.to_list() == expected.to_list()