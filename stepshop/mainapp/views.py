from django.shortcuts import render


def index(request):
    title = "Главная"
    links_menu = [
        {'link': 'index', 'name': 'Главная'},
        {'link': 'products:index', 'name': 'Продукты'},
        {'link': 'about', 'name': 'О нас'},
        {'link': 'contacts', 'name': 'Контакты'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def products(request):
    title = "Каталог продуктов"

    context = {'title': title}

    return render(request, 'products.html', context)


def product(request):
    return render(request, 'product.html')
