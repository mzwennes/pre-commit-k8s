import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pre-commit-k8s",
    version="0.0.2",
    author="Martijn Zwennes",
    author_email="martijnzwennes@pm.me",
    description="pre-commit rules for Kubernetes related files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zwennesm/pre-commit-k8s",
    packages=setuptools.find_packages(include=["hooks", "hooks.*"]),
    entry_points={"console_scripts": ["pre-commit-k8s=hooks.validate:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
