from typing import Any, Sequence
from pydantic import BaseModel as Model

from jumpfish.repo import Repo


class Command(Model):
    raw: str
    """
    Raw string used to generate the command.
    """

    func: "Func"
    context: "Context"

    arrival_timestamp: float
    """
    When the command was received by the interpreter.
    """

    args: list["CommandArg"]


class Func(Model):
    name: str
    description: str
    arg_spec: "FuncArgSpec"


class FuncArgSpec(Model):
    positionals: list["PositionalArgSpec"]
    short_flags: list["ShortFlagArgSpec"]
    long_flags: list["LongFlagArgSpec"]


class PositionalArgSpec(Model):
    name: str
    type: str
    default: Any | None = None
    """
    Default value for the argument.
    """
    is_optional: bool = False
    """
    Whether can be omitted.

    Note that for positionals earlier ones cannot be optional if the latter
    ones are not.
    """


class ShortFlagArgSpec(Model):
    """
    Short boolean flag.

    Short flags can always be omitted which is interpreted as a False (i.e.
    they are always optional).
    """
    char: str

    default: bool = False
    """
    Default value for the flag.
    """

    is_countable: bool = False
    """
    Whether the flag can be specified several times in order to achieve
    different logic.

    For example, verbosity level 3: "-vvv".
    """


class LongFlagArgSpec(Model):
    """
    AKA named argument, like "--something somevalue".
    """
    name: str
    type: str
    default: Any | None = None
    """
    Default value for the flag.
    """
    is_optional: bool = True
    """
    Whether the flag can be omitted.
    """


class Context(Model):
    namespace: str
    timestamp: float


# no type for command args since the commands are linked with functions where
# arg specs can be inspected by name
class CommandArg(Model):
    name: str
    value: Any


class State(Model):
    """
    Whole or partial state of JumpFish database.
    """
    commands: list[Command]
    funcs: list[Func]
    currentContext: Context


class JumpFishConfig(Model):
    """
    Configuration of JumpFish interpreter.
    """
    repos: Sequence[Repo] | None = None
    """
    Which repositories to use for data operations.

    First passed repository is always the one used for data read. Data write is
    made to all repositories.

    By default there is a single built-in repo.
    """
