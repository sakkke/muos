from subprocess import run
from typing import Any

class Command:
    @staticmethod
    def run(command: Any) -> None:
        result = run(command)

        returncode = result.returncode

        if returncode != 0:
            raise Exception('Returned a non-zero code: {}'.format(returncode))

        return result
