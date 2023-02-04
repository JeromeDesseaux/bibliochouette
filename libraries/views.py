from rest_framework import viewsets
from rest_framework import permissions

from libraries.models import Library, Reader, Loan, Book, BookGenre
from libraries.serializers import (
    LibrarySerializer,
    ReaderSerializer,
    LoanSerializer,
    BookSerializer,
    BookGenreSerializer,
)


# Create your views here.
class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by("-created_at")
    serializer_class = LibrarySerializer
    permission_classes = [permissions.IsAuthenticated]


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all().order_by("-created_at")
    serializer_class = ReaderSerializer
    permission_classes = [permissions.IsAuthenticated]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by("-created_at")
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookGenreViewSet(viewsets.ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    permission_classes = [permissions.IsAuthenticated]
