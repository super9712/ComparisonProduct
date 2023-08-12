from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/aspectapp/', include('aspectapp.urls')),  # 'yourapp'은 앱의 이름으로 변경해주세요.
    # 다른 URL 패턴들을 여기에 추가할 수 있습니다.
]
