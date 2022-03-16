from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, AddBlogView, AddCommentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('add-blog/', AddBlogView.as_view(), name='add_blog'),
    path('add-comment/', AddCommentView.as_view(), name='add_comment'),

]
