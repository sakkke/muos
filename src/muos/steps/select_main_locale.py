from ..environment import Environment
from ..select_step import SelectStep

class SelectMainLocale(SelectStep):
    name: str = 'Select a main locale'

    def main(self, environment: Environment) -> None:
        super().main(environment, environment.locales)
        environment.main_locale = self.choices[0]
