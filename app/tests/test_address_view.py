# from fastapi.testclient import TestClient
from starlette.testclient import TestClient



def test_address_create(client: TestClient,address_factory, customer_auth_header):
    
    response = client.post('/address/', headers= customer_auth_header,
                        json={

                             'address': str,
                             'city':str,
                             'state':str,
                             'number':str,
                             'zipcode':str,
                             'neighbourhood':str,
                             'primary':bool,
                             'customer_id':int
                        
    })
    print("response",response.json())
    assert response.status_code == 201

   