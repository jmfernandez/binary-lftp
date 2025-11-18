import atexit
import os.path
import platform
import setuptools
import shutil
import tempfile
import urllib.request
import sys

# In this way, we are sure we are getting
# the installer's version of the library
# not the system's one
setupDir = os.path.dirname(__file__)
sys.path.insert(0, setupDir)

from binary_lftp import __version__ as binary_lftp_version
from binary_lftp import __author__ as binary_lftp_author
from binary_lftp import __license__ as binary_lftp_license

# The statically linked binary version to fetch
lftp_version = '4.9.3'

machine = platform.machine()
if machine == "x86_64":
    lftp_machine = "amd64"
elif machine == "aarch64":
    lftp_machine = "arm64v8"
else:
    lftp_machine = machine
system = platform.system().lower()
lftp_download_link = f"https://github.com/userdocs/lftp-static/releases/download/{lftp_version}/lftp-{lftp_machine}"

edir = tempfile.mkdtemp()
atexit.register(shutil.rmtree, edir)
the_lftp_path = os.path.join(edir, "lftp")
local_lftp_binary, headers = urllib.request.urlretrieve(lftp_download_link, filename=the_lftp_path)
# Assuring the right permissions
os.chmod(the_lftp_path, 0o555)

setuptools.setup(
    name='binary-lftp',
    version=binary_lftp_version,
    author=binary_lftp_author,
    url="https://github.com/jmfernandez/binary_lftp",
    project_urls={"Bug Tracker": "https://github.com/jmfernandez/binary_lftp/issues"},
    packages=setuptools.find_packages(),
    package_data={"binary_lftp": ["py.typed"]},
    data_files=[
        ("bin", [the_lftp_path])
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    license=binary_lftp_license,
)
