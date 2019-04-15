from distutils.core import setup
import setuptools

setuptools.setup(
     name='keyvaluestoreprovider',  
     version='0.1',
     author="Shubham Sureka",
     author_email="sureka.shubham1@gmail.com",
     description="KeyValueStore package",
     url="https://bitbucket.org/dev/keyvaluestore/src/integration/",
     packages=setuptools.find_packages(exclude=['KeyValueStore_Services']),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )