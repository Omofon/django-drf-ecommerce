This Ecommerce API, built with Django and Django Rest Framework (DRF), manages products, brands, and categories. It emphasizes comprehensive testing, including unit, end-to-end, and factory testing.

<strong>Models</strong>
<em>Product:</em> Contains fields like id, name, description, price, brand, and category.
Brand: Contains fields like id and name.
Category: Contains fields like id and name.
Serializers
ProductSerializer: Serializes Product model fields.
BrandSerializer: Serializes Brand model fields.
CategorySerializer: Serializes Category model fields.
Views
ProductViewSet: CRUD operations for Product.
BrandViewSet: CRUD operations for Brand.
CategoryViewSet: CRUD operations for Category.
Testing
Unit Testing: Tests individual components like models and serializers.
End-to-End Testing: Tests complete workflows and user scenarios.
Factory Testing: Uses factory libraries to create test data.
