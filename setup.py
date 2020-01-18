import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='databricks_client',
    version='0.0.1',
    author="Alexandre Gattiker",
    author_email="algattik@microsoft.com",
    description="REST client for Databricks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/algattik/databricks_client",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    extras_require={
        'azurecli':  ["azure-core"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
