import requests
from app.config.dependency import get_url_api


def get_cytokines_by_classification(classification: str):
    url = get_url_api() + '/analises/search-cytokines-by-classification?classification=' + classification
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return "Não foi possível obter os dados."

