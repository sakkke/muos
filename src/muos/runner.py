from atexit import register as atexit_register
from typing import List
from .environment import Environment
from .log import Log
from .step import Step

class Runner:
    '''A class to run steps'''

    environment: Environment
    '''Environment of Runner

    Example: ``Environment()``
    '''

    def __init__(self, environment: Environment, steps: List[Step]) -> None:
        '''Initialize Runner

        Args:
            environment (Environment): A value of ``Environment`` type.
            steps (List[Step]): ``List`` of ``Step`` type.
        '''

        self.environment = environment
        self.steps = steps

    def run(self) -> None:
        '''A function to run steps'''

        Log.message(self.environment.name)

        for step in self.steps:
            step.main(self.environment)
            atexit_register(step.at_exit, self.environment)
