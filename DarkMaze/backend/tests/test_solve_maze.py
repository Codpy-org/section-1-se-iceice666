import httpx
import pytest

USERNAME = "TestUser"
RESET_URL = f"http://127.0.0.1:8000/api/v1/reset?username={USERNAME}"
LOGIN_URL = f"http://127.0.0.1:8000/api/v1/login"
MOVE_URL = "http://127.0.0.1:8000/api/v1/move"
game_state = {}


async def login_request():
    """Simulates a frontend login."""
    payload = {"username": USERNAME}

    async with httpx.AsyncClient() as client:
        response = await client.post(LOGIN_URL, json=payload)

    assert response.status_code == 200  # Ensure the request was successful
    return response.json()


async def reset_request():
    """Reset Game state"""
    global game_state

    async with httpx.AsyncClient() as client:
        response = await client.get(RESET_URL)

    assert response.status_code == 200  # Ensure the request was successful
    game_state = response.json()
    return game_state


async def move_request(direction):
    """Simulates a frontend move request."""
    global game_state

    payload = {"username": USERNAME, "direction": direction}

    async with httpx.AsyncClient() as client:
        response = await client.post(MOVE_URL, json=payload)

    assert response.status_code == 200  # Ensure the request was successful
    game_state = response.json()
    return game_state


@pytest.mark.asyncio
async def test_integration():
    global game_state

    await login_request()
    game_state = await reset_request()
    assert game_state["current_position"] == [1, 0]

    for i in range(5):
        game_state = await move_request("down")

    assert game_state["current_position"] == [1, 5]


@pytest.mark.asyncio
async def test_solver():
    global game_state

    await login_request()
    game_state = await reset_request()
    assert game_state["current_position"] == [1, 0]

    game_state = await move_request("down")
    game_state = await move_request("down")
    game_state = await move_request("down")
    game_state = await move_request("down")
    game_state = await move_request("down")

    game_state = await move_request("right")
    game_state = await move_request("down")
    game_state = await move_request("right")
    game_state = await move_request("right")

    game_state = await move_request("up")
    game_state = await move_request("up")
    game_state = await move_request("up")
    game_state = await move_request("up")

    game_state = await move_request("right")
    game_state = await move_request("right")
    game_state = await move_request("down")
    game_state = await move_request("right")
    game_state = await move_request("right")
    game_state = await move_request("down")
    game_state = await move_request("right")
    game_state = await move_request("down")


    assert game_state["health"] == 666