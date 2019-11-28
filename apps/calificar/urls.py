from rest_framework import routers
from .views import ProfessorViewset, StudentViewset, ScoreViewset

router = routers.DefaultRouter()
router.register(r'professors', ProfessorViewset)
router.register(r'students', StudentViewset)
router.register(r'scores', ScoreViewset)
