from rest_framework import serializers

from holders.models import HolderGroup
from users.models import User
from .models import Library, Reader, Loan, BookGenre, Book


class LibrarySerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=HolderGroup.objects.all())

    class Meta:
        model = Library
        fields = ["id", "label", "group"]


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ["id", "firstname", "lastname", "surname"]


class LoanSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    reader = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())

    class Meta:
        model = Loan
        fields = ["id", "book", "reader", "returned_date", "expected_return_date"]


class BookSerializer(serializers.ModelSerializer):
    library = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all())
    genre = serializers.PrimaryKeyRelatedField(
        queryset=BookGenre.objects.all(), required=False
    )
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Book
        fields = [
            "id",
            "library",
            "genre",
            "author",
            "description",
            "isbn",
            "pageCount",
            "publicationDate",
            "title",
            "owner",
        ]


class BookGenreSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = BookGenre
        fields = ["id", "label", "created_by"]
