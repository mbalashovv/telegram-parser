from abc import abstractmethod
from contextlib import asynccontextmanager

__all__ = ["BaseConnector"]


class BaseConnector:

    @abstractmethod
    @asynccontextmanager
    async def get_connection(self):
        """Getting connection in asynchronous context."""

        raise NotImplementedError()
