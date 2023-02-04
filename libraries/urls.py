from rest_framework import routers
from libraries import views

router = routers.DefaultRouter()
router.register("libraries", views.LibraryViewSet)
router.register("readers", views.ReaderViewSet)
router.register("loans", views.LoanViewSet)
router.register("books", views.BookViewSet)
router.register("genres", views.BookGenreViewSet)
