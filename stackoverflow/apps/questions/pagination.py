from rest_framework import pagination


class QuestionsPagination(pagination.PageNumberPagination):
    page_size = 1  # number of items in the page
    max_page_size = 100  # max number of items in a page
