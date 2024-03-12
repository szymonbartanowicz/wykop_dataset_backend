from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_connection():
    response = client.post("/", json={})
    assert response.status_code == 200


def test_pagination():
    items_per_page = 5
    response = client.post("/", json={
        "page": 0,
        "items_per_page": items_per_page,
    })
    assert response.status_code == 200
    assert len(response.json()["data"]) == items_per_page


def test_search():
    search_phrase = "komputer".lower()
    response = client.post("/", json={
        "search": search_phrase,
    })
    assert response.status_code == 200
    for doc in response.json()["data"]:
        assert search_phrase in doc["title"][0].lower() or search_phrase in doc["description"][0].lower()


def test_filters():
    greater_than_column = "comments_count"
    less_than_column = "downvote_count"
    equals_than_column = "can_vote"
    greater_than_value = 10
    less_than_value = 15
    equals_than_value = True
    response = client.post("/", json={
        "filters": [
            {
                "name": greater_than_column,
                "operation": "greater_than",
                "value": greater_than_value
            },
            {
                "name": less_than_column,
                "operation": "less_than",
                "value": less_than_value
            },
            {
                "name": equals_than_column,
                "operation": "equals",
                "value": equals_than_value
            }
        ],
    })
    assert response.status_code == 200
    for doc in response.json()["data"]:
        assert doc[greater_than_column][0] >= greater_than_value
        assert doc[less_than_column][0] <= less_than_value
        assert doc[equals_than_column][0] == equals_than_value


def test_sorting():
    order_by = "comments_count"
    order_direction = "desc"
    response = client.post("/", json={
        "order_by": order_by,
        "order_direction": order_direction
    })
    assert response.status_code == 200
    data = response.json()["data"]
    prev_value = data[0][order_by]
    for doc in data[1:]:
        assert prev_value >= doc[order_by]

