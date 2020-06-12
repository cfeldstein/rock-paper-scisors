import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get_stats",
    version="0.0.1",
    author="Cary Feldstein",
    author_email="cary.feldstein@gmail.com",
    description="Statistical Analysis of Streaming Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
