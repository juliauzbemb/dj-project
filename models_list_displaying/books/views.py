from django.shortcuts import render


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


# def books_view_date(request):
#     pass