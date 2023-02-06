from django.core.exceptions import ValidationError
from django.db import models

from core.models import AuditableEntity
import datetime


# Create your models here.
class Library(AuditableEntity):
    label = models.CharField("label", max_length=32, null=False, blank=False)
    group = models.ForeignKey(
        "holders.HolderGroup", on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        db_table = "libraries"


class Reader(AuditableEntity):
    firstname = models.CharField("firstname", max_length=32, null=True, blank=True)
    lastname = models.CharField("lastname", max_length=52, null=True, blank=True)
    surname = models.CharField("surname", max_length=32, null=True, blank=True)
    user = models.OneToOneField(
        "users.User", null=True, blank=True, on_delete=models.CASCADE
    )

    def clean(self):
        if not (self.firstname and self.lastname) or self.surname:
            raise ValidationError("You must at least provide a surname.")

    class Meta:
        db_table = "readers"


class Loan(AuditableEntity):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    returned_date = models.DateField(null=True, blank=True)
    expected_return_date = models.DateField(
        default=datetime.date.today() + datetime.timedelta(weeks=3)
    )

    class Meta:
        ordering = ["-expected_return_date"]
        db_table = "loans"


class BookGenre(models.Model):
    label = models.CharField("label", max_length=42)
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "book_genres"


class Book(AuditableEntity):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    genre = models.ForeignKey(
        BookGenre, on_delete=models.CASCADE, null=True, blank=True
    )
    author = models.CharField("author", max_length=255)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField("isbn", max_length=14)
    page_count = models.SmallIntegerField(default=0)
    publication_date = models.DateField(null=True, blank=True)
    title = models.CharField("title", max_length=42)

    class Meta:
        db_table = "books"
