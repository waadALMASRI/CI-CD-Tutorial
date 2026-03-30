# CI/CD Toy Project (Python)

A minimal Python project to learn how **pip** (package manager), **pytest** (test suite), and **GitHub Actions** (CI pipeline) work together.

## Project Structure

```
ci-cd-python-project/
├── .github/
│   └── workflows/
│       └── ci.yml              ← The CI pipeline (GitHub Actions reads this)
├── src/
│   ├── __init__.py             ← Makes src/ a Python package
│   └── calculator.py           ← Your application code
├── tests/
│   ├── __init__.py             ← Makes tests/ a Python package
│   └── test_calculator.py      ← The test suite (pytest runs this)
├── main.py                     ← Entry point (run the app)
├── requirements.txt            ← The package manager manifest
├── .gitignore
└── README.md
```

## How to Use This Locally

```bash
# 1. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 2. Install dependencies (package manager in action)
pip install -r requirements.txt

# 3. Run the app
python main.py

# 4. Run the test suite
pytest -v

# 5. Run tests with coverage report
pytest --cov=src --cov-report=term-missing
```

## How to Push to GitHub

```bash
# 1. Create a new repo on github.com (do NOT add a README)
# 2. Then run:
git init
git add .
git commit -m "Initial commit: Python toy project with CI pipeline"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ci-cd-python-project.git
git push -u origin main
```

Once pushed, go to the **Actions** tab in your repo — you'll see the pipeline running!

## What Happens When You Push

1. GitHub detects `.github/workflows/ci.yml`
2. It spins up a fresh Ubuntu VM
3. It installs Python 3.12 and your dependencies (`pip install -r requirements.txt`)
4. It runs your test suite (`pytest -v`)
5. It checks code coverage (`pytest --cov=src --cov-fail-under=80`)
6. If all 22 tests pass and coverage ≥ 80% → green checkmark ✓
7. If anything fails → red X, you get notified

## Mapping to the CI/CD Guide

| Guide Concept        | Python Equivalent                  |
|----------------------|------------------------------------|
| Package manager      | **pip** + `requirements.txt`       |
| Test framework       | **pytest**                         |
| Test suite           | `tests/test_calculator.py`         |
| `npm install`        | `pip install -r requirements.txt`  |
| `npm test`           | `pytest -v`                        |
| `package.json`       | `requirements.txt`                 |
