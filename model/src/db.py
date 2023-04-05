"""db"""
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, List, Optional, Tuple, TypedDict, Union


# pylint: disable=R0903
class CursorRowType(ABC):
    """CursorRowType"""


# pylint: disable=R0903
class CursorType(ABC):
    """CursorType"""

    @abstractmethod
    def execute(self, query: str, data: Optional[Tuple[Any]]):
        """execute"""

    @abstractmethod
    def fetchall(self) -> List[CursorRowType]:
        """fetchall"""

    @property
    @abstractmethod
    def lastrowid(self) -> int:
        """lastrowid"""


class RowType(TypedDict):
    """RowType"""

    id: Union[int, str]
    created_at: datetime
    updated_at: datetime
