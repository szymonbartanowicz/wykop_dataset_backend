from fastapi import APIRouter
from app.models.models import SearchParameters
from app.services.query_builder import QueryBuilder
import requests
from app.services.helpers import prepare_response

router = APIRouter()


@router.post("/")
def search(search_parameters: SearchParameters):
    try:
        qb = QueryBuilder(search_parameters)
        url = qb.get_full_url()
        response = requests.get(url)
        return prepare_response(response.json())
    except Exception as e:
        return {"Error": str(e)}

