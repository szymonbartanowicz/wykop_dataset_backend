from pydantic import BaseModel, Extra
from enum import Enum, IntEnum


class OrderDirectionEnum(str, Enum):
    asc = 'asc'
    desc = 'desc'


class OperationEnum(str, Enum):
    equals = 'equals'
    contains = 'contains'
    greater_than = 'greater_than'
    less_than = 'less_than'


class ItemsPerPageEnum(IntEnum):
    option1 = 5
    option2 = 10
    option3 = 20
    option4 = 50
    option5 = 100


class Filter(BaseModel):
    name: str
    operation: OperationEnum
    value: str


class SearchParameters(BaseModel):
    page: int | None = None
    items_per_page: ItemsPerPageEnum | None = None
    order_by: str | None = None
    order_direction: OrderDirectionEnum | None = None
    filters: list[Filter] | None = None
    search: str | None = None

    class Config:
        extra = Extra.forbid
