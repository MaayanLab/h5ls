import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="archs4py",
    version="0.0.1",
    author="Alexander Lachmann",
    author_email="alexander.lachmann@mssm.edu",
    description="ARCHS4 pipeline for sample submission and post processing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maayanlab/xalign",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "archs4py": ["data/*"]
    },
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'progress',
        'loess',
        'tqdm',
        'statsmodels',
        'mygene',
        'GEOparse',
        'feather-format',
        'sqlalchemy',
        'wget',
        'pymysql'
    ],
    python_requires='>=3.6',
)