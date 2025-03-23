
__all__ = [
    "UniqueViolation",
    "EmptyResult",
    "DriverError",
]


class UniqueViolation(Exception):
    pass


class EmptyResult(Exception):
    pass


class DriverError(Exception):
    pass
