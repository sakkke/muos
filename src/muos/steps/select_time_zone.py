from ..environment import Environment
from ..get_lines_as_list import get_lines_as_list
from ..get_static_dir import get_static_dir
from ..select_step import SelectStep

class SelectTimeZone(SelectStep):
    name: str = 'Select a time zone'

    def main(self, environment: Environment) -> None:
        super().main(environment, get_lines_as_list(get_static_dir() / 'timezones.txt'))
        environment.time_zone = self.choices[0]
