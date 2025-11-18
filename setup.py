import atexit
import os.path
import platform
from setuptools import setup
import shutil
import tempfile
import urllib.request

setupDir = os.path.dirname(__file__)
with open(os.path.join(setupDir, ".version.lftp")) as vH:
    lftp_version = vH.read().strip()

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

setup(
    name='binary-lftp',
    version=lftp_version,
    data_files=[
        ("bin", [the_lftp_path])
    ],
    license='MIT',
)
