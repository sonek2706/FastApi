import setuptools

with open("README.md") as buffer:
    long_description = buffer.read()

setuptools.setup(
    name="my_package",
    version="0.0.1",
    author="Jan Son Ha",
    author_email="s26092@pjwstk.edu.pl",
    description="Ecommerce website package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sonek2706/Ecommerce-Website",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Typing :: Typed",
    ],
    python_requires=">=3.6",
)
