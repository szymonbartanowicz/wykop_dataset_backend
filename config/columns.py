COLUMNS_METADATA = {
    'link_id': {'type': 'int', 'sortable': False, 'filterable': False},
    'title': {'type': 'string', 'sortable': True, 'filterable': True},
    'description': {'type': 'string', 'sortable': True, 'filterable': True},
    'source_url': {'type': 'string', 'sortable': False, 'filterable': False},
    'upvote_count': {'type': 'int', 'sortable': True, 'filterable': True},
    'downvote_count': {'type': 'int', 'sortable': True, 'filterable': True},
    'comments_count': {'type': 'int', 'sortable': True, 'filterable': True},
    'related_count': {'type': 'int', 'sortable': True, 'filterable': True},
    'creation_date': {'type': 'datetime', 'sortable': True, 'filterable': True},
    'author_user_id': {'type': 'int', 'sortable': False, 'filterable': False},
    'plus18': {'type': 'bool', 'sortable': True, 'filterable': True},
    'status': {'type': 'string', 'sortable': True, 'filterable': True},
    'can_vote': {'type': 'bool', 'sortable': True, 'filterable': True},
    'is_hot': {'type': 'bool', 'sortable': True, 'filterable': True},
    'archived': {'type': 'bool', 'sortable': True, 'filterable': True},
    'id': {'type': 'string', 'sortable': True, 'filterable': True},
    '_version_': {'type': 'int', 'sortable': False, 'filterable': False},
}

HIDDEN_COLUMNS = [
    'link_id', '_version_'
]