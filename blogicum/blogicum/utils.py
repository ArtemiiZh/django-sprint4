from django.core.paginator import Paginator


def paginate_queryset(request, queryset, limit):

    paginator = Paginator(queryset, limit)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
