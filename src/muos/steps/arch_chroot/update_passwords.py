from subprocess import PIPE, Popen, run
from ...environment import Environment
from ...step import Step

class UpdatePasswords(Step):
    name: str = 'Update user passwords'

    def main(self, environment: Environment) -> None:
        super().main(environment)

        for password in environment.passwords:
            stdin = Popen(['printf', '%s', ':'.join(password)], stdout=PIPE)
            run(['arch-chroot', environment.mnt, 'chpasswd'], stdin=stdin.stdout)
