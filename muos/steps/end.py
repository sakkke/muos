from ..step import Step

class End(Step):
    name: str = 'End'

    def main(self) -> None:
        print('end')
