from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in prachi_interview_solution/__init__.py
from prachi_interview_solution import __version__ as version

setup(
	name="prachi_interview_solution",
	version=version,
	description="prachi_interview_solution",
	author="prachi_interview_solution",
	author_email="prachibobade09@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
