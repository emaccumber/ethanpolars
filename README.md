# ethanpolars

[![PyPI](https://img.shields.io/pypi/v/ethanpolars.svg)](https://pypi.org/project/ethanpolars/)
[![Python Version](https://img.shields.io/pypi/pyversions/ethanpolars.svg)](https://pypi.org/project/ethanpolars/)
[![License](https://img.shields.io/pypi/l/ethanpolars.svg)](https://github.com/ethanmaccumber/ethanpolars/blob/main/LICENSE)

Utility functions for working with Polars dataframes.

## Installation

```bash
pip install ethanpolars
```

Or for development:

```bash
pip install -e ".[dev]"
```

## Features

### Demean

The `demean` function subtracts the mean from each non-NaN value in an array, preserving NaN values.

```python
import polars as pl
from ethanpolars import demean

# Sample data
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
```

Output:
```
shape: (5, 2)
┌───────┬──────────┐
│ value ┆ demeaned │
│ ---   ┆ ---      │
│ f64   ┆ f64      │
╞═══════╪══════════╡
│ 1.0   ┆ -1.75    │
│ 2.0   ┆ -0.75    │
│ 3.0   ┆ 0.25     │
│ null  ┆ null     │
│ 5.0   ┆ 2.25     │
└───────┴──────────┘
```

## Development

### Setup

Clone the repository and install development dependencies:

```bash
git clone https://github.com/ethanmaccumber/ethanpolars.git
cd ethanpolars
pip install -e ".[dev]"
```

### Testing

Run tests with pytest:

```bash
pytest
```

With coverage:

```bash
pytest --cov=ethanpolars
```

### Linting and Formatting

Format code:

```bash
black src tests
isort src tests
```

Run linters:

```bash
ruff src tests
mypy src
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
