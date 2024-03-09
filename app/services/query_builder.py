from dotenv import load_dotenv
import os
from app.config.config import *
from app.models.models import *
from fastapi import HTTPException
from app.services.helpers import *


load_dotenv()

TYPES_OPERATIONS = {
    "string": {OperationEnum.contains.value},
    "text": {OperationEnum.contains.value},
    "int": {
        OperationEnum.equals.value,
        OperationEnum.greater_than.value,
        OperationEnum.less_than.value,
    },
    "bool": {OperationEnum.equals.value},
    "enum": {OperationEnum.equals.value},
    "datetime": {
        OperationEnum.equals.value,
        OperationEnum.greater_than.value,
        OperationEnum.less_than.value,
    }
}


class QueryBuilder:
    def __init__(self, search_parameters):
        self.base_url = ""
        self.search_parameters = search_parameters
        self.set_base_url()
        self.query = ""

    def set_base_url(self):
        self.base_url = (
            os.getenv("SOLR_HOST")
            + ":"
            + os.getenv("SOLR_PORT")
            + "/solr/"
            + os.getenv("SOLR_COLLECTION")
            + "/select?q="
        )

    def set_query(self):
        self.apply_search()
        if self.search_parameters.filters:
            self.apply_filters()
        if self.search_parameters.order_by is not None:
            self.apply_sorting()
        self.apply_pagination()
        self.set_visible_columns()

    def get_full_url(self) -> str:
        self.set_query()
        return self.base_url + self.query

    def apply_search(self):
        if self.search_parameters.search is None:
            self.query += "*"
        else:
            self.query += (
                self.search_parameters.search
                + "~"
                + str(CONFIG["maximum_edit_distance"])
                + "&qf="
                + get_serialized_search_columns_with_boosts()
                + "&defType="
                + CONFIG["query_parser"]
            )
            self.apply_faceting()
            self.apply_highlighting()

    def apply_filters(self):
        filters = self.search_parameters.filters
        for filter in filters:
            self.apply_filter(filter)

    def apply_filter(self, filter: Filter):
        self.validate_filters(filter)
        filter_query = filter.name + ":"
        if filter.operation == OperationEnum.equals.value:
            filter_query += '"' + filter.value + '"'
        elif filter.operation == OperationEnum.greater_than.value:
            filter_query += "[" + filter.value + " TO *]"
        elif filter.operation == OperationEnum.less_than.value:
            filter_query += "[* TO " + filter.value + "]"
        self.query += "&fq=" + filter_query

    def validate_filters(self, filter: Filter):
        if filter.name not in COLUMNS_METADATA.keys():
            raise HTTPException(detail="Wrong column name.", status_code=400)
        if (
            filter.operation
            not in TYPES_OPERATIONS[COLUMNS_METADATA[filter.name]["type"]]
        ):
            raise HTTPException(
                detail=f"Operation '{filter.operation.value}' is not valid for column '{filter.name}'",
                status_code=400,
            )
        if not COLUMNS_METADATA[filter.name]["filterable"]:
            raise HTTPException(
                detail=f"Column '{filter.name}' is not filterable.", status_code=400
            )

    def apply_sorting(self):
        order_by = self.search_parameters.order_by
        self.validate_sorting(order_by)
        order_by = get_actual_column(order_by)
        order_direction = self.search_parameters.order_direction
        if order_direction is None:
            order_direction = "asc"
        self.query += "&sort=" + order_by + "%20" + order_direction

    def validate_sorting(self, column: str):
        if column not in COLUMNS_METADATA.keys():
            raise HTTPException(detail="Wrong column name.", status_code=400)
        if not COLUMNS_METADATA[column]["sortable"]:
            raise HTTPException(
                detail=f"Column '{column}' is not sortable.", status_code=400
            )

    def apply_pagination(self):
        page = self.search_parameters.page
        if page is None:
            page = 0
        items_per_page = self.search_parameters.items_per_page
        if items_per_page is None:
            items_per_page = CONFIG["default_items_per_page"]
        else:
            items_per_page = items_per_page.value
        offset = page * items_per_page
        self.query += "&start=" + str(offset) + "&rows=" + str(items_per_page)

    def apply_faceting(self):
        self.query += "&facet=true&facet.field=" + CONFIG["facet_column"]

    def apply_highlighting(self):
        self.query += "&hl=true&hl.fl=title,description"

    def set_visible_columns(self):
        self.query += "&fl=" + get_serialized_visible_columns()
