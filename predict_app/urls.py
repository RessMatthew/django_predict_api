from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from predict_app import views

router = routers.DefaultRouter()
router.register(r'trainingresult', views.TrainingResultViewSet)  # 路由到TrainingResultViewSet视图

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # GET，获得所有训练结果
    path('get-all-result/', views.get_all_result),

    # POST，随机森林测试并评价模型
    path('rf/training/', views.rf_training),

    # POST，随机森林预测数据集缺陷
    path('rf/predict/', views.rf_predict),

    # POST，knn训练测试并评价模型
    path('knn/training/', views.knn_training),

    # POST，knn已训练模型预测数据集
    path('knn/predict/', views.knn_predict),

]