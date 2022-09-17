from ..environment import Environment
from ..get_lines_as_list import get_lines_as_list
from ..get_static_dir import get_static_dir
from ..step import Step

class SelectTimeZone(Step):
    description: str = 'Selecting a time zone...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        timezones_txt = get_static_dir() / 'timezones.txt'
        choices = get_lines_as_list(timezones_txt)
        result = environment.fzf.prompt(choices, '--height=10 --layout=reverse')
        environment.time_zone = result[0]
