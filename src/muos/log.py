from datetime import datetime
from typing import Any
from .color import Color

class Log:
    @staticmethod
    def message(value: Any) -> None:
        print('{}[{}] {}{}{}{}'.format(
            Color.CYAN,
            datetime.now().strftime('%H:%M:%S.%f'),
            Color.DEFAULT,
            Color.GREEN,
            value,
            Color.DEFAULT
        ))
