"""villager"""
from typing import Literal, TypeVar

# pylint: disable=E0401
from db import RowType

# pylint: disable=E0401
from net import LinkType

ResourceTypeT = TypeVar(
    "ResourceTypeT",
    Literal["villager"],
    Literal["villager_special"],
)


# pylint: disable=R0903
class CommonType(RowType):
    """CommonType"""

    is_special: bool
    name: str
    resource: ResourceTypeT
    link: LinkType


# pylint: disable=R0903
class CommonDetailType(CommonType):
    """CommonDetailType"""

    birth_day: int
    birth_month: int
    is_special: False


# pylint: disable=R0903
class SpecialDetailType(CommonDetailType):
    """SpecialDetailType"""

    is_special: True
    resource: Literal["villager_special"]
