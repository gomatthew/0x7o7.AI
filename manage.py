from app import create_app
import uvicorn

app = create_app()
debug = True


def main():
    if debug:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
    else:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
