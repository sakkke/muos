'''Step that is a part of Runner

* Step class
'''

from .environment import Environment
from .log import Log

class Step:
    '''Step for Runner

    This class is used in Runner instance.
    Runner runs each step of the array.
    '''

    name: str
    '''Name of step

    Example: ``'Do something'``
    '''

    def main(self, environment: Environment) -> None:
        '''Function called by Runner

        This function prints the step name.

        Args:
            environment (Environment): Aceessable environment variable.

        Returns:
            None: This function have not return value.
        '''
        Log.message(self.name)

    def at_exit(self, environment: Environment) -> None:
        '''Function called at exit

        Args:
            environment (Environment): Aceessable environment variable.

        Returns:
            None: This function have not return value.
        '''
        pass
