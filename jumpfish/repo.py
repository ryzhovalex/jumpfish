from jumpfish.models import Command, State


class Repo:
    def save(self, command: Command) -> None:
        raise NotImplementedError

    def get_state(self) -> State:
        # TODO(ryzhovalex): only whole state retrieval is supported for now
        raise NotImplementedError
