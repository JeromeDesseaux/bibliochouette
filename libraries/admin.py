from django.contrib import admin
from .models import Loan, Book, BookGenre, Reader, Library

# Register your models here.
admin.site.register(Loan)
admin.site.register(Book)
admin.site.register(BookGenre)
admin.site.register(Reader)
admin.site.register(Library)
