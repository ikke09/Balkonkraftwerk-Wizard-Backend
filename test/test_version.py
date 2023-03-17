import pytest


@pytest.mark.usefixtures('client')
class TestVersion():

    def test_get_api_version(self, client):
        response = client.get('/api')
        assert response.status_code == 200
        data = response.json["data"]
        assert 'version' in data
        assert data['version'] == '0.0.1'
