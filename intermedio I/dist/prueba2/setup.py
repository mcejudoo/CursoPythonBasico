from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name="Empleado",
version="1.0",
description="Ejemplo patron DAO",
author="Antonio",
author_email="home@gmail.es",
url="http://prueba.com",
license="GPL",
scripts=["empleadoDAO.py"]
)
