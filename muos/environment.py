from pyfzf import FzfPrompt
from .fzf_manager import FzfManager

class Environment:
    fzf: FzfPrompt

    def __init__(self) -> None:
        self.setup_fzf()

    def setup_fzf(self) -> None:
        fzf_manager = FzfManager()
        fzf_manager.get()
        self.fzf = fzf_manager.use()
