from setuptools import setup
from Cython.Build import cythonize

setup(
    name="toon_plus",
    version="1.0.0",
    description="Toon Plus format",
    author="Joel",
    packages=["toon_plus"],
    ext_modules=cythonize("toon_plus/toon_plus.pyx", compiler_directives={'language_level' : "3"}),
    zip_safe=False,
)
