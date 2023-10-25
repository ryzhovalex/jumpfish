from typing import Sequence
from jumpfish.builtin import BuiltinRepos
from jumpfish.models import Command, Func, JumpFishConfig
from jumpfish.repo import Repo


class JumpFish:
    def __init__(self, config: JumpFishConfig) -> None:
        self._repos: Sequence[Repo] = \
            config.repos if config.repos else BuiltinRepos

    def send(self, c: str) -> None:
        """
        Sends a new command to the interpreter.

        Commands are stateful - each new command is attached to the current
        context, some logic may depend on this context. So the order of the
        commands is important.
        """
        pass

    def get_funcs(self, search: FuncSearch) -> list[Func]:
        pass

    def get_commands(self, search: CommandSearch) -> list[Command]:
        pass
