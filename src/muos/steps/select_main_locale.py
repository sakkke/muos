from ..environment import Environment
from ..step import Step

class SelectMainLocale(Step):
    name: str = 'Selecting a main locale...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        choices = environment.locales
        result = environment.fzf.prompt(choices, '--height=10 --layout=reverse')
        environment.main_locale = result[0]
