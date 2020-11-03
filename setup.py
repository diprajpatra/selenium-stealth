import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selenium-stealth",
    version="1.0.0",
    author="Dipraj Patra",
    author_email="diprajpatra@gmail.com",
    description="Trying to make python selenium more stealthy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diprajpatra/selenium-stealth",
    packages=setuptools.find_packages(),
    package_data={"selenium-stealth": ["js/*.js"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
