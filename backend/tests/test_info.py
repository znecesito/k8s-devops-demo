import json
from app import app

def test_info_endpoint():
    with app.test_client() as client:
        response = client.get('/info')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "container_id" in data
