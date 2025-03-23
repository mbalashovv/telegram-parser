from functools import partial

__all__ = [
    "factory",
    "inject",
]


def factory(cls, *args, **kwargs):
    return partial(__factory, cls, *args, **kwargs)


def __factory(cls, *args, **kwargs):
    return cls(*args, **kwargs)


def inject(cls):
    for key, value in cls.keywords.items():
        if isinstance(value, partial):
            cls.keywords[key] = inject(value)
    return cls()
