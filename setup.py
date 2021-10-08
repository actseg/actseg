from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


# IDEA from: https://github.com/psf/requests/blob/main/setup.py
about = {}
with open(here / "src" / "actseg" / "__about__.py", "r") as f:
    exec(f.read(), about)

setup(
    name="actseg",
    version=about["__version__"],
    description="A utility for action segmentation research: evaluation and others",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/actseg/actseg/",
    author="Yasser Souri",
    author_email="yassersouri@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="action segmentation, video understanding",
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    install_requires=["numpy"],
    extras_require={
        "dev": ["pytest", "check-manifest"],
    },
    project_urls={
        "Bug Reports": "https://github.com/actseg/actseg/issues",
        "Source": "https://github.com/actseg/actseg/",
    },
)
