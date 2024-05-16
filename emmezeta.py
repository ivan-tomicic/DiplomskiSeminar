import copy

import requests
import json

from emmezeta_utils import payload


def call_emmezeta_api(filters):
    url = "https://www.emmezeta.hr/graphql"
    payload_copy = copy.deepcopy(payload)

    if "sortDir" in filters.keys() and "sortField" in filters.keys():
        if filters["sortField"] == "popular":
            payload_copy["variables"]["sort"] = {}
        else:
            payload_copy["variables"]["sort"] = {}
            payload_copy["variables"]["sort"][filters["sortField"]] = filters["sortDir"]


    for key, value in filters.items():
        if key in ["sortField", "sortDir"]:
            continue
        if key == "fetchSize":
            payload_copy["variables"]["pageSize"] = value
        elif key in ["height", "width", "price"]:
            payload_copy["variables"]["filters"].append({
                "key": key,
                "value": value,
                "inputType": "FilterRangeTypeInput"
            })
            payload_copy["variables"]["filter"][key] = {"from": value.split("-")[0], "to": value.split("-")[1]}
        elif key == "colors":
            for color in value:
                payload_copy["variables"]["filters"].append({
                    "key": "boja",
                    "value": color,
                    "inputType": "FilterEqualTypeInput"
                })
            payload_copy["variables"]["filter"]["boja"] = {"in": [color for color in value]}

    headers = {
        'Content-Type': 'application/json'
    }

    print("Payload: ", payload_copy)

    response = requests.post(url, data=json.dumps(payload_copy), headers=headers)

    return response.json()


