"""villager"""
from typing import Literal, TypeVar
from db import RowType
from net import LinkType

ResourceTypeT = TypeVar(
    "ResourceTypeT",
    Literal["villager"],
    Literal["villager_special"],
)


class CommonType(RowType):
    """CommonType"""

    is_special: bool
    name: str
    resource: ResourceTypeT
    link: LinkType


class CommonDetailType(CommonType):
    """CommonDetailType"""

    birth_day: int
    birth_month: int
    is_special: False


class SpecialDetailType(CommonDetailType):
    """SpecialDetailType"""

    is_special: True
