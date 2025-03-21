# Contributing to ethanpolars

First off, thanks for taking the time to contribute!

## Development Environment Setup

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/ethanpolars.git
   cd ethanpolars
   ```

3. Install the package in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

1. Create a branch for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes.

3. Run the tests to ensure your changes don't break anything:
   ```bash
   pytest
   ```

4. Format and lint your code:
   ```bash
   make format
   make lint
   ```

5. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add feature X"
   ```

6. Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request on GitHub.

## Coding Style

We use:
- Black for code formatting
- isort for import sorting
- ruff for linting
- mypy for type checking

All of these can be run at once with:
```bash
make format
make lint
```

## Adding a New Feature

If you're adding a new function, please:

1. Add proper type hints
2. Add comprehensive docstrings
3. Add tests for the new function
4. Update documentation if necessary
5. Add examples if applicable

## Releasing (for maintainers)

1. Update the version number in `pyproject.toml`
2. Create a new tag:
   ```bash
   git tag v0.x.x
   ```
3. Push the tag:
   ```bash
   git push origin v0.x.x
   ```

The CI/CD will automatically build and publish the package to PyPI.

## Questions?

If you have any questions, please open an issue on GitHub.
