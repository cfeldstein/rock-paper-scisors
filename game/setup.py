import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rps",
    version="0.0.1",
    author="Cary Feldstein",
    author_email="cary.feldstein@gmail.com",
    description="A Rock Paper Scissors Game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
