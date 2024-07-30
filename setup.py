from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

README = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="python-lorem-ipsum",
    version="2.0.0",
    url="https://github.com/oVitorio/python-lorem-ipsum",
    license="MIT",
    author="Vitório Augusto Cavalheiro",
    description="A Python library for generating Lorem Ipsum text.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.9.0, <4",
)
