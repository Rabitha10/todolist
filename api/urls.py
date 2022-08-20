from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router=DefaultRouter()
router.register('mytodos',views.TodosViewset,basename='mytodos')
router.register('modeltodos',views.TodosModelViewset,basename='modelview')
router.register('signin',views.LoginView,basename='signin')


urlpatterns=[
    path('todos/',views.TodosView.as_view()),
    # api/v1/todos/{id}
    path('todos/<int:id>',views.TodoDetails.as_view()),
    path('mixin/todos/',views.TodosMixinView.as_view()),
    path('mixin/todos/<int:id>',views.TodoDetailMixin.as_view()),
    path('accounts/signup/',views.UsercreationView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+router.urls