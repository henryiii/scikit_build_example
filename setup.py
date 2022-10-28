import sys

from scikit_build_core.setuptools.extension import CMakeBuild, CMakeExtension
from setuptools import find_packages, setup

setup(
    name="cmake_example",
    version="0.0.1",
    ext_modules=[CMakeExtension("scikit_build_example")],
    zip_safe=False,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    extras_require={"test": ["pytest>=6.0"]},
    cmdclass={"build_ext": CMakeBuild},
    python_requires=">=3.7",
)
