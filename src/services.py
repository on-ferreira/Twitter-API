from typing import Any, Dict, List

import requests
from src.mongoConnection import trends_collection
from src.constants import BRAZIL_WOE_ID, API_URL, headers


def _get_trends(woe_id: int) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    payload = {"woeid": woe_id}

    trends_response = requests.post(API_URL, data=payload, headers=headers)

    # Check if the request was successful
    if trends_response.status_code == 200:
        return trends_response.json()["trends"]

    else:
        trends = []

    return trends



def get_trends() -> List[Dict[str, Any]]:
    """Get treending topics persisted in MongoDB.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    """Get trends topics and save on MongoDB."""

    trends = _get_trends(woe_id=BRAZIL_WOE_ID)

    # Check if trends were retrieved successfully
    if trends:
        for trend in trends.values():
            trends_collection.insert_one(trend)
    else:
        print("No trends to save.")