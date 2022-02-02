from rest_framework import routers
from .views import FileTrasnferView

router=routers.SimpleRouter()
router.register('', FileTrasnferView, basename="filesview")

