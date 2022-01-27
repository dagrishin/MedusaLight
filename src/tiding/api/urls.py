from rest_framework.routers import SimpleRouter

from .views import PublicationView


router = SimpleRouter()
router.register(r"", PublicationView, "publication")
urlpatterns = router.urls

