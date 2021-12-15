from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.db import get_db
from app.models.models import Base, Category, Product, Supplier, User,PaymentMethod,ProductDiscount
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

    yield Session()


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
def payment_discount_factory(db_session,product_factory,payment_method_factory):
    class PaymentDiscountFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = ProductDiscount
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        mode = factory.Faker('name')
        value = factory.Faker('pyfloat')
        product =  factory.SubFactory(product_factory)
        payment_method =  factory.SubFactory(payment_method_factory)

    return PaymentDiscountFactory

@pytest.fixture()
def user_admin_token(user_factory):
    user_factory(role='admin')

    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjY1NDIwODc0fQ.o_syoOwrg8VOvl5nWYnA0waXxL0pFLdUgJY8HoqMVjM'


@pytest.fixture()
def admin_auth_header(user_admin_token):
    return {'Authorization': f'Bearer {user_admin_token}'}
