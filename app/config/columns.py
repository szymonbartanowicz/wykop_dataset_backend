COLUMNS_METADATA = {
    "link_id": {
        "type": "int",
        "sortable": False,
        "filterable": False,
        "has_alias": False,
    },
    "title": {
        "type": "text",
        "sortable": True,
        "filterable": False,
        "has_alias": True,
    },
    "description": {
        "type": "text",
        "sortable": True,
        "filterable": False,
        "has_alias": True,
    },
    "source_url": {
        "type": "string",
        "sortable": False,
        "filterable": False,
        "has_alias": False,
    },
    "upvote_count": {
        "type": "int",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "downvote_count": {
        "type": "int",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "comments_count": {
        "type": "int",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "related_count": {
        "type": "int",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "creation_date": {
        "type": "datetime",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "author_user_id": {
        "type": "int",
        "sortable": False,
        "filterable": False,
        "has_alias": False,
    },
    "plus18": {
        "type": "bool",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "status": {
        "type": "enum",
        "sortable": True,
        "filterable": True,
        "has_alias": True,
    },
    "can_vote": {
        "type": "bool",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "is_hot": {
        "type": "bool",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "archived": {
        "type": "bool",
        "sortable": True,
        "filterable": True,
        "has_alias": False,
    },
    "id": {
        "type": "string",
        "sortable": False,
        "filterable": False,
        "has_alias": False,
    },
    "_version_": {
        "type": "int",
        "sortable": False,
        "filterable": False,
        "has_alias": False,
    },
}

HIDDEN_COLUMNS = ["link_id", "_version_", "author_user_id"]

SEARCH_COLUMNS = {
    "title": {
        "boost": 2.0
    },
    "description": {
        "boost": 1.0
    }
}
