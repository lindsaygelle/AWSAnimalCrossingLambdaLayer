"""net"""
from typing import Literal, TypedDict, TypeVar

MethodTypeT = TypeVar(
    "MethodTypeT", Literal["DELETE"], Literal["GET"], Literal["PATCH"], Literal["POST"]
)


class LinkType(TypedDict):
    """LinkType"""

    method: MethodTypeT
    href: str
