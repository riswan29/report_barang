from django.shortcuts import render, get_object_or_404
from .models import Report

def search_progress(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '').strip()

        if search_query:  # Perform search only if search query is not empty
            reports = None  # Initialize reports as None

            if search_query.isdigit():
                reports = Report.objects.filter(id=search_query)
            elif search_query.startswith('KD') and search_query[2:].isdigit():
                reports = Report.objects.filter(id=int(search_query[2:]))
            else:
                reports = Report.objects.filter(n_barang__icontains=search_query)

            if not reports:  # If no reports found, set reports to an empty queryset
                reports = Report.objects.none()

        else:  # If search query is empty, set reports to an empty queryset
            reports = Report.objects.none()

        context = {
            'reports': reports,
            'search_query': search_query
        }
        return render(request, 'search_progress.html', context)

    return render(request, 'search_progress.html')
