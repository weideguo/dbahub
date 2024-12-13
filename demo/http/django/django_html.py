# 前后端分离时，django集成前端

# 编译前端项目存放于项目根目录下的目录 frontend


# settings.py
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "frontend/dist/static"),
)

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'frontend/dist')],
    },
]


# urls.py
from django.urls import path
from django.views.generic import TemplateView
path(r'', TemplateView.as_view(template_name="index.html")),

