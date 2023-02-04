from rest_framework import routers
from holders import views

router = routers.DefaultRouter()
router.register("groups", views.HolderGroupViewSet)
router.register("", views.HolderViewSet)
