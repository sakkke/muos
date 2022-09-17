from subprocess import CompletedProcess, run
from typing import Any

class Command:
    @staticmethod
    def capture(command: Any) -> CompletedProcess[str]:
        result = run(command, capture_output=True, text=True)

        returncode = result.returncode

        if returncode != 0:
            raise Exception('Returned a non-zero code: {}'.format(returncode))

        return result

    @staticmethod
    def run(command: Any) -> None:
        result = run(command)

        returncode = result.returncode

        if returncode != 0:
            raise Exception('Returned a non-zero code: {}'.format(returncode))

        return result
