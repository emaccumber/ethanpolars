"""
Example demonstrating the use of the demean transform function.
"""

import polars as pl
import numpy as np

from ethanpolars import demean

def main():
    """Run the demean example."""
    print("Example 1: Using demean with a Polars DataFrame")
    
    # Create a DataFrame with a sample column
    df = pl.DataFrame({
        "value": [1.0, 2.0, 3.0, None, 5.0],
    })
    
    # Apply demean to the column
    df = df.with_columns(
        demeaned=pl.col("value").map_batches(
            lambda x: pl.Series(demean(x.to_numpy()))
        )
    )
    
    print(df)
    print("\n")
    
    print("Example 2: Using demean with a NumPy array")
    
    # Create a NumPy array
    arr = np.array([10.0, 20.0, np.nan, 40.0, 50.0], dtype=np.float64)
    result = np.zeros_like(arr)
    
    # Apply demean
    demean(arr, result)
    
    # Create a formatted display
    print("Original array:")
    print(arr)
    print("\nDemeaned array:")
    print(result)

if __name__ == "__main__":
    main()
