# from fastapi.testclient import TestClient
from starlette.testclient import TestClient



def test_order_create(client: TestClient,address_factory,payment_method_factory,product_factory,coupon_factory, customer_auth_header):
    address = address_factory()
    coupon = coupon_factory()
    payment_method = payment_method_factory()
    product = product_factory()
    response = client.post('/orders/', headers= customer_auth_header,
                        json={

                        'address_id': address.id,
                        'payment_method_id': payment_method.id,
                        'coupon_code': coupon.code,
                        'products': [{
                                       "quantity": 2,
                                       "id": product.id
                                   }
                                   ]
    })
    print("response",response.json())
    assert response.status_code == 201



def test_order_update(client: TestClient,order_factory,admin_auth_header,):
    order = order_factory()
    response = client.put(f'/orders/{order.id}', headers= admin_auth_header,
                        json={
                                     
                        'status' :'ORDER RECEIVED',
                                   
    })
    assert response.status_code == 200
    print("response",response.json())
    # response = client.get('/orders/1',headers= admin_auth_header,)
    # assert response.status_code == 200
    print("response",response.json())
    assert response.json()['status'] == 'ORDER RECEIVED'
    
    

    

def test_order_get(client: TestClient,admin_auth_header):
    response = client.get('/orders/', headers=admin_auth_header)
    assert response.status_code == 200
    
    

