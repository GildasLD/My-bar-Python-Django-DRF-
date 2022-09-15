from django.urls import include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

API_TITLE = 'My bar'
API_DESCRIPTION = 'My bar\'s API'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    re_path(r'^api/', include('beers.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls',
            namespace='rest_framework')),
    re_path(r'^schema/$', schema_view),
    re_path(r'^docs/', include_docs_urls(title=API_TITLE,
            description=API_DESCRIPTION))
]