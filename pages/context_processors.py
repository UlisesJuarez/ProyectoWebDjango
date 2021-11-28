from pages.models import Page

def get_pages(request):
    pages=Page.objects.filter(visible=True).order_by('order').values_list('id','title','slug')
    #si solo se necesita un elemento 
    #pages=Page.objects.values_list('title',flat=True)

    return {
        'pages':pages
    }
