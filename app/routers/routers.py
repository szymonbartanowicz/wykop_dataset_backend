from fastapi import APIRouter
import httpx
from app.models.models import SearchParameters, SearchResults
from app.services.query_builder import QueryBuilder
from app.services.helpers import prepare_response

router = APIRouter()


@router.post("/")
def search(search_parameters: SearchParameters) -> SearchResults:
    try:
        qb = QueryBuilder(search_parameters)
        url = qb.get_full_url()
        response = httpx.get(url)
        return prepare_response(response.json())
    except Exception as e:
        return {"Error": {str(e)}}
