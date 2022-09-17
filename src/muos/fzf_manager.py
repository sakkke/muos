from os import path, remove
from pyfzf import FzfPrompt
from tarfile import open as open_tar
from tempfile import mkdtemp
from urllib import request

class FzfManager:
    EXECUTABLE_NAME = 'fzf'
    executable: str
    tarfile: str
    temp_d: str

    def __init__(self) -> None:
        self.temp_d = mkdtemp()

    def download(self) -> None:
        url = 'https://github.com/junegunn/fzf/releases/download/0.33.0/fzf-0.33.0-linux_amd64.tar.gz'
        url_filename = url.split('/')[-1]

        self.tarfile = path.join(self.temp_d, url_filename)

        request.urlretrieve(url, self.tarfile)

    def extract(self) -> None:
        with open_tar(self.tarfile) as f:
            f.extract(self.EXECUTABLE_NAME, self.temp_d)

    def get(self) -> None:
        self.download()
        self.extract()
        remove(self.tarfile)
        self.executable = path.join(self.temp_d, self.EXECUTABLE_NAME)

    def use(self) -> FzfPrompt:
        return FzfPrompt(self.executable)
