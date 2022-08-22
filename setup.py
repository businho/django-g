from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django",
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "flake8<5",
        "flake8-bugbear",
        "pytest",
        "pytest-black",
        "pytest-cov",
        "pytest-flake8",
        "pytest-mock",
    ],
)
