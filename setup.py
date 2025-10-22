from setuptools import setup, find_packages

setup(
    name="donghua-api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
      "fastapi>=0.119.1",
      "uvicorn>=0.38.0", 
      "httpx>=0.28.1",
      "beautifulsoup4>=4.14.2",
      "python-multipart>=0.0.20"
    ],
    python_requires=">=3.8",
)
