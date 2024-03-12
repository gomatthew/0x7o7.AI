from app import app
import uvicorn

debug=True

if debug:
    uvicorn.run(app, host='127.0.0.1', port=8081, reload=True)
# else:
#     uvicorn.run(app,host=host,port=8081,reload=False)