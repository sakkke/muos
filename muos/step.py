from .environment import Environment
from .log import Log

class Step:
    description: str

    def main(self, environment: Environment) -> None:
        Log.message(self.description)

    def at_exit(self, environment: Environment) -> None:
        pass
