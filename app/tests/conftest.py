from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.db import get_db
from app.models.models import Address, Base, Category, Coupon, Product, Supplier, User,PaymentMethod,ProductDiscount,Order,Customer
from app.app import app
import pytest
import factory

@pytest.fixture()
def db_session():
    engine = create_engine('sqlite:///./test.db',
                           connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    db = Session ()
    yield db
    db.close()
    

   


@pytest.fixture()
def override_get_db(db_session):
    def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    return client


@pytest.fixture()
def user_factory(db_session):
    class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = User
            sqlalchemy_session = db_session

        id = None
        display_name = factory.Faker('name')
        email = factory.Faker('email')
        role = None
        password = '$2b$12$2F.MmED.HUKwVq74djSzguVYu4HBYEkKYNqxRnc/.gVG24QyYcC9m'

    return UserFactory


@pytest.fixture()
def category_factory(db_session):
    class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Category
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return CategoryFactory


@pytest.fixture()
def supplier_factory(db_session):
    class SupplierFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Supplier
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return SupplierFactory

@pytest.fixture()
def payment_method_factory(db_session):
    class PaymentMethodFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = PaymentMethod
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')
        enabled = factory.Faker('pybool')

    return PaymentMethodFactory



@pytest.fixture()
def product_factory(db_session,category_factory,supplier_factory):
    class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Product
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        description =  factory.Faker('name')
        price = factory.Faker('pyfloat')
        technical_details = factory.Faker('name')
        image  = factory.Faker('name')
        visible = factory.Faker('pybool')
        category =  factory.SubFactory(category_factory)
        supplier = factory.SubFactory(supplier_factory)


    return ProductFactory


@pytest.fixture()
def product_discount_factory(db_session,product_factory,payment_method_factory):
    class ProductDiscountFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = ProductDiscount
            sqlalchemy_session = db_session

        id = factory.Sequence(int)
        mode = factory.Faker('name')
        value = factory.Faker('pyfloat')
        product =  factory.SubFactory(product_factory)
        payment_method =  factory.SubFactory(payment_method_factory)

    return ProductDiscountFactory


@pytest.fixture()
def coupon_factory(db_session):
    class CouponFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Coupon
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        code = factory.Faker('name')
        type = 'value'
        expire_at = factory.Faker('date_time')
        limit =  factory.Faker('pyint')
        value = factory.Faker('pyfloat')

    return CouponFactory



@pytest.fixture()
def address_factory(db_session,customer_factory):
    class AddressFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Address
            sqlalchemy_session = db_session

        id =  factory.Sequence(int)
        address =  factory.Faker('name')
        city = factory.Faker('city')
        state = factory.Faker('country_code')
        number = factory.Faker('pyint')
        zipcode = factory.Faker('postcode')
        neighbourhood = factory.Faker('street_address')
        primary = True
        customer = factory.SubFactory(customer_factory)


    return AddressFactory



@pytest.fixture()
def customer_factory(db_session, user_factory):
    class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Customer
            sqlalchemy_session = db_session

        id =  factory.Sequence(int)
        first_name = factory.Faker('first_name')
        last_name = factory.Faker('last_name')
        phone_number = factory.Faker('phone_number')
        genre = factory.Faker('name')
        document_id = factory.Faker('pyint')
        birth_date = factory.Faker('date_time')
        user = factory.SubFactory(user_factory)

    return CustomerFactory



@pytest.fixture()
def order_factory(db_session,customer_factory,address_factory,payment_method_factory):
    class OrderFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Order
            sqlalchemy_session = db_session

        id = factory.Sequence(int)
        number =factory.Faker('pyint')
        status = 'ORDER SHIPPED'
        customer = factory.SubFactory(customer_factory)
        created_at = factory.Faker('date_time')
        address = factory.SubFactory(address_factory)
        total_value = factory.Faker('pyfloat')
        payment_method = factory.SubFactory(payment_method_factory)
        total_discount = factory.Faker('pyfloat')

    return OrderFactory







@pytest.fixture()
def user_admin_token(user_factory):
    user_factory(role='admin')

    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjY1NDIwODc0fQ.o_syoOwrg8VOvl5nWYnA0waXxL0pFLdUgJY8HoqMVjM'


@pytest.fixture()
def admin_auth_header(user_admin_token):
    return {'Authorization': f'Bearer {user_admin_token}'}

@pytest.fixture()
def usercustomer_token(user_factory):
    user_factory(role='customer',password = '$2b$12$ISnz0oHoDZybfE1ddpAIMuJNsIrXBfIRBi5Nts3ulo2n8UVL3d7qS')

    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjM5ODgxOTQ0fQ.rwF4RUiESn9PbXB8YIa2NkHK04Pb66Btbl1m3YPPFr8'


@pytest.fixture()
def customer_auth_header(usercustomer_token):
    return {'Authorization': f'Bearer {usercustomer_token}'}
