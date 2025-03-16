from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def serve_game_html():
    with open("src/templates/game.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/login", response_class=HTMLResponse)
async def serve_login_html():
    with open("src/templates/login.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn

    # Run the app
    uvicorn.run(app, host="0.0.0.0", port=8088)
