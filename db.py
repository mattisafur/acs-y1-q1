from models import State


def initialize_database() -> None:
    raise NotImplementedError


def is_database_initialized() -> bool:
    raise NotImplementedError


def load_state(name: str) -> State | None:
    raise NotImplementedError


def delete_state(name: str) -> None:
    raise NotImplementedError
