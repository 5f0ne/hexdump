from setuptools import setup

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="hexdumper",            
    version="2.0.1",
    author="5f0",
    url="https://github.com/5f0ne/hexdump",
    description="Prints the hexdump of a selected file",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=["hexdumper"],
    install_requires=[
        "hash_calc",
        "hexlib==2.0.1"
    ],
    entry_points={
        "console_scripts": [
            "hexdumper = hexdumper.__main__:main"
        ]
    }
)