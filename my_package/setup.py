import setuptools

with open("README.md") as buffer:
    long_description = buffer.read()

setuptools.setup(
    name="my_package",
    version="0.0.1",
    author="Jan Son Ha",
    author_email="s26092@pjwstk.edu.pl",
    description="just a package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sonek2706/my_package",
    python_requires=">=3.6",
)
