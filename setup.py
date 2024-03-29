from setuptools import setup
import os

VERSION = "2.0.0"


def collect_files(*dirs):
    "Walks file tree to return a list of all file paths under each dir in dirs."
    file_paths = []

    for dr in dirs:
        for d, _2, paths in os.walk(dr):
            for fname in paths:
                fpath = os.path.join(d, fname)
                file_paths.append(fpath)

    return file_paths


data_dirs = ["amf-checks"]

setup(
    name="amf-compliance-checks",
    author="Ag Stephens",
    author_email="ag.stephens@stfc.ac.uk",
    url="https://github.com/ncasuk/amf-compliance-checks",
    version=VERSION,
    description="AMF compliance checks",
    packages=data_dirs,
    data_files=[("", collect_files(*data_dirs))],
    include_package_data=True
)

