This Ecommerce API, built with Django and Django Rest Framework (DRF), manages products, brands, and categories. It emphasizes comprehensive testing, including unit, end-to-end, and factory testing.

<hr/><strong>Models</strong><br/>
<strong>Product:</strong> Contains fields like id, name, description, price, brand, and category.<br/>
<strong>Brand: </strong> Contains fields like id and name.<br/>
<strong>Category: </strong> Contains fields like id and name.<br/>
<hr/><strong>Serializers</strong><br/><br/>
<strong>ProductSerializer:</strong> Serializes Product model fields.<br/>
<strong>BrandSerializer:</strong> Serializes Brand model fields.<br/>
<strong>CategorySerializer:</strong> Serializes Category model fields.<br/>
<hr/><strong>Views</strong><br/><br/>
<strong>ProductViewSet:</strong> CRUD operations for Product.<br/>
<strong>BrandViewSet:</strong> CRUD operations for Brand.<br />
<strong>CategoryViewSet:</strong> CRUD operations for Category.<br />
<hr/><strong>Testing</strong><br/><br/>
<strong>Unit Testing:</strong> Tests individual components like models and serializers.<br/>
<strong>End-to-End Testing:</strong> Tests complete workflows and user scenarios.<br/>
<strong>Factory Testing:</strong> Uses factory libraries to create test data.<br/>
