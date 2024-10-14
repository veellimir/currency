import time
from datetime import datetime
from typing import Union, List, Dict

from django.core.cache import cache
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages

from currency_project.env_config import CONFIG__API_CURRENCY
from api.currency import get_usd_to_rub


def get_current_usd(request) -> JsonResponse:
    last_request_time: Union[float, None] = cache.get("last_request_time")

    if last_request_time and time.time() - last_request_time < 10:
        messages.error(request, "Пожалуйста, подождите 10 секунд между запросами")
        return render(request, "mainapp/current_usd.html")

    try:
        usd_to_rub: float = get_usd_to_rub(CONFIG__API_CURRENCY)
        messages.success(request, "Ответ получен")
    except request.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

    current_time = datetime.now()

    history: List[Dict[str, Union[float, int]]] = cache.get("usd_history", [])
    history.insert(0, {"rate": usd_to_rub, "timestamp": current_time})

    if len(history) > 10:
        history = history[:10]
    cache.set("usd_history", history, timeout=None)
    cache.set("last_request_time", time.time())

    context: Dict = {
        "title": "Курс USD к RUB",
        "current_rate": usd_to_rub,
        "history": history,
        "current_time": current_time,
    }
    return render(request, "mainapp/current_usd.html", context)
