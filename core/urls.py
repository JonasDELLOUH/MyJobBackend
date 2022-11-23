from django.urls import path, include
from rest_framework import routers

from core.views import MemberViewSet, PostViewSet, PostCommentViewSet, PostLikeViewSet, JobViewSet, JobCategoryViewSet, \
    WorkerViewSet, MessageViewSet, AddressViewSet, WorkshopViewSet, DiscussionViewSet, PostWithCatViewSet, \
    PostOfWorkerViewSet

router = routers.DefaultRouter()
router.register('member', MemberViewSet, basename='Member')
router.register('post', PostViewSet, basename="Post")
router.register('post_with_cat', PostWithCatViewSet, basename="PostWithCat")
router.register('post_of_worker', PostOfWorkerViewSet, basename="PostOfWorker")
router.register('post_comment', PostCommentViewSet, basename="PostComment")
router.register('post_like', PostLikeViewSet, basename="PostLike")
router.register('job', JobViewSet, basename="Job")
router.register('job_category', JobCategoryViewSet, basename="JobCategory")
router.register('worker', WorkerViewSet, basename="Worker")
router.register('message', MessageViewSet, basename="Message")
router.register('address', AddressViewSet, basename="Address")
router.register('workshop', WorkshopViewSet, basename="Workshop")
router.register('discussion', DiscussionViewSet, basename="discussion")

urlpatterns = [
    path('', include(router.urls))
]
