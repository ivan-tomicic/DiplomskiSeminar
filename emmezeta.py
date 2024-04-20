import requests
import json

from emmezeta_utils import payload


def call_emmezeta_api(filters):
    url = "https://www.emmezeta.hr/graphql"

    if "sortDir" in filters.keys() and "sortField" in filters.keys():
        if filters["sortField"] == "popular":
            payload["variables"]["sort"] = {}
        else:
            payload["variables"]["sort"] = {}
            payload["variables"]["sort"][filters["sortField"]] = filters["sortDir"]


    for key, value in filters.items():
        if key in ["sortField", "sortDir"]:
            continue
        if key == "fetchSize":
            payload["variables"]["pageSize"] = value
        elif key in ["height", "width", "price"]:
            payload["variables"]["filters"].append({
                "key": key,
                "value": value,
                "inputType": "FilterRangeTypeInput"
            })
            payload["variables"]["filter"][key] = {"from": value.split("-")[0], "to": value.split("-")[1]}
        elif key == "colors":
            for color in value:
                payload["variables"]["filters"].append({
                    "key": "boja",
                    "value": color,
                    "inputType": "FilterEqualTypeInput"
                })
            payload["variables"]["filter"]["boja"] = {"in": [color for color in value]}

    headers = {
        'Content-Type': 'application/json'
    }

    print("Payload: ", payload)

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    return response.json()


