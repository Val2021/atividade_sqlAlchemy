
# from fastapi.testclient import TestClient
from starlette.testclient import TestClient

def test_coupon_create(client: TestClient,admin_auth_header):
    response = client.post('/coupon/', headers=admin_auth_header,
                        json={

                        'code':'123',
                        'type':'value',
                        'expire_at': '2021-12-19T00:00:00.000+00:00',
                        'limit': 5,
                        'value':10.0 
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1


def test_coupon_get(client: TestClient, coupon_factory,admin_auth_header):
    coupon =  coupon_factory(code = '123', type = 'value', limit = 5,value = 10.0 )
    response = client.get('/coupon/', headers=admin_auth_header)
    assert response.status_code == 200
    assert len(response.json()) == 1
    