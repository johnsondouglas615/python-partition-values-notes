

def solve(value):
    return {"low": [x for x in value["items"] if x < value["threshold"]], "high": [x for x in value["items"] if x >= value["threshold"]]}
