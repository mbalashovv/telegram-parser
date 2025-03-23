from abc import ABC
from typing import TypeVar, List

from app.pkg.models.base import Model

__all__ = ["BaseRepository", "Repository"]

Repository = TypeVar("Repository", bound="BaseRepository")


class BaseRepository(ABC):
    async def create(self, cmd: Model) -> Model:
        raise NotImplementedError

    async def read(self, query: Model) -> Model:
        raise NotImplementedError

    async def read_all(self) -> List[Model]:
        raise NotImplementedError

    async def update(self, cmd: Model) -> Model:
        raise NotImplementedError

    async def delete(self, cmd: Model) -> Model:
        raise NotImplementedError
