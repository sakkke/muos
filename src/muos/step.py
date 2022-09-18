from .environment import Environment
from .log import Log

class Step:
    name: str

    def main(self, environment: Environment) -> None:
        Log.message(self.name)

    def at_exit(self, environment: Environment) -> None:
        pass
