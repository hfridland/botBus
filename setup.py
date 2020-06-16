import setuptools


setuptools.setup(
    name="bus_bot", # Replace with your own username
    version="0.0.1",
    author="Haim Fridland",
    author_email="hfridland@shaw.ca",
    description="Vancouver bus stop requester",
    long_description="Vancouver bus stop requester",
    long_description_content_type="text/markdown",
    url="https://github.com/hfridland/botBus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)