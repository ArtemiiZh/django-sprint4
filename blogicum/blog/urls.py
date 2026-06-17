from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    # Главная, посты категории и профиль
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),

    # Просмотр отдельного поста
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),

    # Редактирование профиля
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    # Работа с публикациями (Имена адаптированы под шаблоны и тесты Яндекса)
    path('posts/create/', views.post_create, name='create_post'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='edit_post'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='delete_post'),

    # Работа с комментариями
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
