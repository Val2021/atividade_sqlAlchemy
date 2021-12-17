from fastapi.testclient import TestClient


def test_product_discount_create(client: TestClient, payment_method_factory,product_factory, admin_auth_header):
    payment_method = payment_method_factory(enabled = True)
    product = product_factory(price = 10,visible=True)

    response = client.post('/product_discount/', headers=admin_auth_header,
                           json={
                               'mode': 'value',
                               'value': 10,
                               'product_id': product.id,
                               'payment_method_id': payment_method.id
                           })
    print("response",response.json())
    assert response.status_code == 201
    assert response.json()['mode'] == 'value'
    assert response.json()['product_id'] == product.id
    assert response.json()['payment_method_id'] == payment_method.id


def test_product_discount_update(client: TestClient,product_discount_factory, admin_auth_header): ###
    payment_discount = product_discount_factory(mode = 'value')
    response = client.put(f'/product_discount/{payment_discount.id}', headers=admin_auth_header,
                           json={
                               'mode': 'percentage',
                                'value': payment_discount.value,
                                'product_id': payment_discount.product.id,
                                'payment_method_id': payment_discount.payment_method.id
                           })
    print("response",response.json())
    assert response.status_code == 200
    assert response.json()['mode'] == 'percentage'


def test_product_discount_get(client: TestClient,product_discount_factory, admin_auth_header): ###
  
    discounts = [product_discount_factory(mode='value'), product_discount_factory(mode='percentage')]
    response = client.get('/product_discount/', headers=admin_auth_header)
    assert response.status_code == 200
   

    result = [
        {
            'mode': 'value',
            'value': discounts[0].value,
            'product_id': discounts[0].product.id,
            'payment_method_id': discounts[0].payment_method.id,
            'id': discounts[0].id,
            'product': {
                'id': discounts[0].product.id,
                'description': discounts[0].product.description,
                'price':discounts[0].product.price,
                'technical_details': discounts[0].product.technical_details,
                'image':discounts[0].product.image,
                'visible':discounts[0].product.visible,
                'category_id': discounts[0].product.category.id,
                'supplier_id': discounts[0].product.supplier.id,
            },
            'payment_method': {
                'id': discounts[0].payment_method.id,
                'name': discounts[0].payment_method.name
            }
        },
        {
            'mode': 'percentage',
            'value': discounts[1].value,
            'product_id': discounts[1].product.id,
            'payment_method_id': discounts[1].payment_method.id,
            'id': discounts[1].id,
            'product': {
                'id': discounts[1].product.id,
                'description': discounts[1].product.description,
                'price':discounts[1].product.price,
                'technical_details': discounts[1].product.technical_details,
                'image':discounts[1].product.image,
                'visible':discounts[1].product.visible,
                'category_id': discounts[1].product.category.id,
                'supplier_id': discounts[1].product.supplier.id,
            },
            'payment_method': {
                'id': discounts[1].payment_method.id,
                'name': discounts[1].payment_method.name
            }
        },
    ]
    assert len(response.json()) == 2
    assert response.json()[0]['id']==discounts[0].id
    assert response.json() == result


def test_product_discount_validation_enabled(client: TestClient, payment_method_factory,product_discount_factory, admin_auth_header):
    payment_method = payment_method_factory(enabled = False)
    product =  product_discount_factory()

    response = client.post('/product_discount/', headers=admin_auth_header,
                           json={
                               'mode': 'value',
                               'value': 10,
                               'product_id': product.id,
                               'payment_method_id': payment_method.id
                           })
    print("response",response.json())
    assert response.status_code == 400
    assert response.json()["detail"] == "Não poderá ser criado o desconto para essa forma de pagamento"
    


def test_product_discount_validation_has_discount(client: TestClient, payment_method_factory,product_discount_factory, admin_auth_header):
    payment_method = payment_method_factory(enabled = True)
    product =  product_discount_factory()

    response = client.post('/product_discount/', headers=admin_auth_header,
                           json={
                               'mode': 'value',
                               'value': 10,
                               'product_id': product.id,
                               'payment_method_id': payment_method.id
                           })
   
    assert response.status_code == 201
    response = client.post('/product_discount/', headers=admin_auth_header,
                           json={
                               'mode': 'value',
                               'value': 20,
                               'product_id': product.id,
                               'payment_method_id': payment_method.id
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Ja existe um desconto para essa forma de pagamento"