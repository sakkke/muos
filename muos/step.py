from .environment import Environment

class Step:
    name: str

    def main(self, environment: Environment) -> None:
        pass

    def at_exit(self, environment: Environment) -> None:
        pass
