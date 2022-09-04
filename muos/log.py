from typing import Any
from .color import Color

class Log:
    @staticmethod
    def message(value: Any) -> None:
        print('{}{}{}'.format(Color.GREEN, value, Color.DEFAULT))
