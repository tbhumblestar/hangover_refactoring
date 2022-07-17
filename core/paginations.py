from rest_framework.pagination import (
                                    PageNumberPagination,
                                    LimitOffsetPagination,
                                    CursorPagination
)

class PagePagination(PageNumberPagination):
    page_size = 25
    
class LimitandOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    offset_query_param ='start'
    max_limit = 20

class CursoringPagination(CursorPagination):
    page_size = 10
    ordering = 'created_at'
    cursor_query_param = 'record'