import pytest


@pytest.mark.asyncio
async def test_logout(client, user_data):
    response = client.post("/auth/logout")

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_register(client, user_data):
    payload = {
        "name": user_data.name,
        "email": user_data.email,
        "password": user_data.password,
    }

    response = client.post("/auth/register", json=payload)

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_login(client, user_data, cookies):
    payload = {
        "email": user_data.email,
        "password": user_data.password,
    }

    response = client.post("/auth/login", json=payload)
    cookies |= response.cookies

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_me(client, user_data, cookies):
    client.cookies = cookies
    response = client.get("/user/@me")
    user_data.id = response.json()["id"]

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_user_by_id(client, user_data, cookies):
    client.cookies = cookies
    response = client.get(f"/user/{user_data.id}")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_image(client, cookies):
    client.cookies = cookies
    files = {"file": ("image", b"image", "text/plain")}

    response = client.post("/image", files=files)

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_post_project(client, user_data, cookies):
    client.cookies = cookies
    payload = {
        "name": "Project",
        "description": "Project description",
    }

    response = client.post("/project", json=payload)
    user_data.project_id = response.json()["id"]

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_project(client, user_data, cookies):
    client.cookies = cookies

    response = client.get(f"/project/{user_data.project_id}")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_patch_project(client, user_data, cookies):
    client.cookies = cookies
    payload = {
        "name": "Project patched",
        "description": "Project patched description",
    }

    response = client.patch(f"/project/{user_data.project_id}", json=payload)

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_my_project(client, user_data, cookies):
    client.cookies = cookies

    response = client.get(f"/projects/@my")

    assert response.status_code == 200

