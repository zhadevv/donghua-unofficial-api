from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="donghua-api",
    version="1.0.0",
    author="zhadev",
    author_email="cp.zhadev@gmail.com",
    description="Unofficial API for Donghub.vip - Chinese Animation Streaming Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhadevv/donghua-unofficial-api",
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
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Video",
    ],
    install_requires=[
      "fastapi>=0.119.1",
      "uvicorn>=0.38.0", 
      "httpx>=0.28.1",
      "beautifulsoup4>=4.14.2",
      "python-multipart>=0.0.20"
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "donghua-api=start:main",
        ],
    },
    include_package_data=True,
    keywords="donghua, api, scraper, streaming, chinese-animation, anime",
    project_urls={
        "Bug Reports": "https://github.com/zhadevv/donghua-unofficial-api/issues",
        "Source": "https://github.com/zhadevv/donghua-unofficial-api",
        "Documentation": "https://github.com/zhadevv/donghua-unofficial-api#readme",
    },
)
