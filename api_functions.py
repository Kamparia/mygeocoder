from fastapi.responses import JSONResponse


# success response model
def ResponseModel(data, message):
    return JSONResponse(
        status_code=200, 
        content={"code": 200, "status": message, "data": data}
    )    


# errors response model
def ErrorResponseModel(code, message):
    return JSONResponse(
        status_code=code, 
        content={"code": code, "message": message}
    )