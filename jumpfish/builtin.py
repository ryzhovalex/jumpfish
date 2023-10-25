from typing import Sequence
from jumpfish.repo import Repo


class BuiltinRepo(Repo):
    pass


BuiltinRepos: Sequence[Repo] = [BuiltinRepo]  # type: ignore
