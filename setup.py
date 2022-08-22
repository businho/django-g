from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django",
    ],
    setup_requires=[
        "pytest-runner",
        "flake8",
        "black",
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-mock",
    ],
)
