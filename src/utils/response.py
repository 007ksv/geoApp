def create_response(success, data):
    if success:
        res = {"success": success, "data": data}
    else:
        res = {"success": success, "data": {}}
    return res
