from ..step import Step

class Begin(Step):
    name: str = 'Begin'

    def main(self) -> None:
        print('begin')
