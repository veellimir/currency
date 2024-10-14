### DOCS https://www.cbr-xml-daily.ru/

from typing import Union
import requests


def get_usd_to_rub(api_currency: str) -> float:
    try:
        response = requests.get(api_currency)
        response.raise_for_status()

        data = response.json()
        usd_to_rub: Union[float, None] = data["Valute"]["USD"]["Value"]
        return round(usd_to_rub, 2)
    except requests.RequestException as e:
        raise RuntimeError(f"Ошибка при получении курса валют: {e}")
