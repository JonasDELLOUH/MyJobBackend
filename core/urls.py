from django.urls import path, include
from rest_framework import routers

from core.models.job_category import JobCategory
from core.views import MemberViewSet, PostViewSet, PostCommentViewSet, PostLikeViewSet, JobViewSet, JobCategoryViewSet

router = routers.DefaultRouter()
router.register('member', MemberViewSet, basename='Member')
router.register('post', PostViewSet, basename="Post")
router.register('post_comment', PostCommentViewSet, basename="PostComment")
router.register('post_like', PostLikeViewSet, basename="PostLike")
router.register('job', JobViewSet, basename="Job")
router.register('job_category', JobCategoryViewSet, basename="JobCategory")

urlpatterns = [
    path('', include(router.urls))
]
