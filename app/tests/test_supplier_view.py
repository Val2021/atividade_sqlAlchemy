from fastapi.testclient import TestClient





def test_supplier_create(client: TestClient):
    response = client.post('/supplier/', json={
        'name': 'Supplier 1'
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1

def test_supplier_update(client: TestClient):
    response = client.post('/supplier/', json={
        'name': 'Supplier 1'
    })
    assert response.status_code == 201

    response = client.put(
        '/supplier/1', json={'name': 'Supplier alterado'})

    assert response.status_code == 200
    assert response.json()['name'] == 'Supplier alterado'

def test_supplier_show(client: TestClient):
    response = client.post('/supplier/', json={
        'name': 'Supplier 1'
    })

    assert response.status_code == 201
    response = client.get('/supplier/')
    assert response.status_code == 200
    assert response.json()
        

   