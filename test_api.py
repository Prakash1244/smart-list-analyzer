
from types import SimpleNamespace

from bson import ObjectId
from fastapi.testclient import TestClient

import api

client = TestClient(api.app)


def test_send_list(monkeypatch):
    async def fake_insert_one(document):
        return SimpleNamespace(inserted_id=ObjectId())

    monkeypatch.setattr(
        api.analyses_collection,
        "insert_one",
        fake_insert_one,
    )
    monkeypatch.setattr(
        api,
        "prepare_analyse",
        lambda numbers: {"Numbers": numbers},
    )

    response = client.post(
        "/send-list",
        json={"Numbers": [1, 2, 2]},
    )

    assert response.status_code == 200
    assert response.json()["document"] == "Successfully stored"
    assert "_id" in response.json()


def test_get_list(monkeypatch):
    async def fake_retrive_all():
        return [{"_id": "123", "Numbers": [1, 2, 2]}]

    monkeypatch.setattr(api, "retrive_all", fake_retrive_all)

    response = client.get("/get-list")

    assert response.status_code == 200
    assert response.json()["document"][0]["_id"] == "123"


def test_update_docs(monkeypatch):
    async def fake_update_list(analyse_id, numbers):
        return 1

    monkeypatch.setattr(api, "update_list", fake_update_list)

    response = client.put(
        "/update-docs",
        params={"analyse_id": "507f1f77bcf86cd799439011"},
        json={"Numbers": [3, 4, 4]},
    )

    assert response.status_code == 200
    assert response.json()["document"] == "Successfully updated"


def test_delete_docs(monkeypatch):
    async def fake_delete_list(analyse_id):
        return 1

    monkeypatch.setattr(api, "delete_list", fake_delete_list)

    response = client.delete(
        "/delete-docs",
        params={"analyse_id": "507f1f77bcf86cd799439011"},
    )

    assert response.status_code == 200
    assert response.json()["document"] == "deleted successfully"


def test_send_list_invalid_numbers():
    response = client.post(
        "/send-list",
        json={"Numbers": [1, "hello", 3]},
    )

    assert response.status_code == 422
