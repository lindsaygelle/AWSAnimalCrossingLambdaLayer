"""hha"""
from typing import Literal, TypeVar

# pylint: disable=E0401
from db import RowType

# pylint: disable=E0401
from net import LinkType

ResourceTypeT = TypeVar(
    "ResourceTypeT",
    Literal["category"],
    Literal["collection"],
    Literal["concept"],
    Literal["series"],
)


# pylint: disable=R0903
class CommonType(RowType):
    """CommonType"""

    name: str
    resource: ResourceTypeT
    link: LinkType


# pylint: disable=R0903
class CommonDetailType(CommonType):
    """CommonDetailType"""
