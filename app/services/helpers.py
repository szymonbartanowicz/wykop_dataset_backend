from app.config.columns import *


def prepare_response(response):
    total = response['response']["numFound"]
    data = response['response']["docs"]
    facets = response.get('facet_counts', {}).get('facet_fields', {})
    highlighting = response.get('highlighting', {})

    return {
        "total": total,
        "data": data,
        "facets": facets,
        "highlighting": highlighting
    }


def get_serialized_search_columns_with_boosts() -> str:
    serialized = []
    for field, details in SEARCH_COLUMNS.items():
        serialized.append(f"{field}^{details['boost']}")
    return "%20".join(serialized)


def get_serialized_visible_columns() -> str:
    visible_columns = [key for key in COLUMNS_METADATA if key not in HIDDEN_COLUMNS]
    return ",".join(visible_columns)


def get_actual_column(column) -> str:
    if COLUMNS_METADATA[column]["has_alias"]:
        column += "_str"
    return column
