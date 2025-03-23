from typing import TypeVar
import pydantic

__all__ = ["BaseModel", "Model"]

Model = TypeVar("Model", bound="BaseModel")


class BaseModel(pydantic.BaseModel):
    pass
