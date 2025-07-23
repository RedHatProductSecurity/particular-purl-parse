from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="particular-purl-parse",
    version="1.0.0",
    author="Red Hat Product Security",
    author_email="product-security@redhat.com",
    description="A library for parsing PackageURL (PURL) strings and extracting component information",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/RedHatProductSecurity/particular-purl-parse",
    project_urls={
        "Bug Reports": "https://github.com/RedHatProductSecurity/particular-purl-parse/issues",
        "Source": "https://github.com/RedHatProductSecurity/particular-purl-parse",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    keywords="purl, packageurl, parsing, python",
    package_data={
        "": ["*.md", "*.txt"],
    },
    include_package_data=True,
    zip_safe=False,
) 