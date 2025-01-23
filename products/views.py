from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# ViewSet for Category
class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Category.
    """
    queryset = Category.objects.all()  # Retrieves all Category objects
    serializer_class = CategorySerializer  # Uses CategorySerializer for data representation


# ViewSet for Product
class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Product,
    along with search and ordering functionality.
    """
    queryset = Product.objects.all()  # Retrieves all Product objects
    serializer_class = ProductSerializer  # Uses ProductSerializer for data representation
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Enables search and ordering
    search_fields = ['name', 'description']  # Fields to search in
    ordering_fields = ['price', 'stock']  # Fields to order by
