"""hha"""
from typing import Literal, TypeVar
from db import RowType
from net import LinkType

ResourceTypeT = TypeVar(
    "ResourceTypeT",
    Literal["category"],
    Literal["collection"],
    Literal["concept"],
    Literal["series"],
)


class CommonType(RowType):
    """CommonType"""

    name: str
    resource: ResourceTypeT
    link: LinkType


class CommonDetailType(CommonType):
    """CommonDetailType"""
