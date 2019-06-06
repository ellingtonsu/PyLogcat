import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylogcat",
    version="0.0.1",
    author="Wei-Tsung Su",
    author_email="ellington.su@gmail.com",
    description="An application log system similar to Android Logcat for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ellington.su/PyLogcat",
    packages=setuptools.find_packages(),
    install_requires=[
          'enum',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
)