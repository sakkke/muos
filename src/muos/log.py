from datetime import datetime
from typing import Any
from .color import Color

class Log:
    @staticmethod
    def message(value: Any) -> None:
        print('[{}] {}{}{}'.format(
            datetime.now().strftime('%H:%M:%S.%f'),
            Color.CYAN,
            value,
            Color.DEFAULT
        ))
