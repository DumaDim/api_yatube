from django.urls import include, path
from rest_framework.routers import DefaultRouter


from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
]
