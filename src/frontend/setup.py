import setuptools


long_description = "My long description"
# with open("README.md") as buffer:
#     long_description = buffer.read()

with open("requirements.txt") as r:
    lines = r.readlines()

install_requires = list(filter(lambda x: len(x) > 0, map(str.strip, lines)))

setuptools.setup(
    name="frontend",
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
    install_requires=install_requires,
)
