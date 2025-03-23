import pydantic
from functools import wraps
from typing import Dict, List, Tuple, Union

from app.internal.repository.handlers.handle_exception import handle_exception
from app.pkg.models.base import Model
from app.pkg.models.exceptions import EmptyResult


__all__ = ["collect_response"]


def collect_response(fn):
    """
    Args:
            fn: Target function that contains a query in postgresql.
    Returns:
            The model that is specified in type hints of `fn`.
    Raises:
            EmptyResult: when query of `fn` returns None.
    """

    @wraps(fn)
    @handle_exception
    async def inner(
        *args: Tuple[str],
        **kwargs: Dict[str, str],
    ) -> Union[List[Model], Model]:
        response = await fn(*args, **kwargs)
        if not response:
            raise EmptyResult
        return pydantic.parse_obj_as(
            fn.__annotations__["return"],
            dict(response),
        )

    return inner
