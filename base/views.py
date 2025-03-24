from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumni
from .forms import AlumniForm

def alumni_list(request):
    alumni = Alumni.objects.all()
    
    # Filtering based on query parameters
    graduation_year = request.GET.get('graduation_year')
    department = request.GET.get('department')
    company_name = request.GET.get('company_name')

    if graduation_year:
        alumni = alumni.filter(graduation_year=graduation_year)
    if department:
        alumni = alumni.filter(department__icontains=department)
    if company_name:
        alumni = alumni.filter(company_name__icontains=company_name)

    # Unique values for filters
    years = Alumni.objects.values_list('graduation_year', flat=True).distinct()
    departments = Alumni.objects.values_list('department', flat=True).distinct()
    companies = Alumni.objects.values_list('company_name', flat=True).distinct()

    return render(request, 'base/alumni_list.html', {
        'alumni': alumni,
        'years': years,
        'departments': departments,
        'companies': companies
    })

def add_alumni(request):
    if request.method == "POST":
        form = AlumniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumni_list')
    else:
        form = AlumniForm()
    return render(request, 'base/add_alumni.html', {'form': form})

def edit_alumni(request, alumni_id):
    alumni = get_object_or_404(Alumni, id=alumni_id)
    if request.method == "POST":
        form = AlumniForm(request.POST, instance=alumni)
        if form.is_valid():
            form.save()
            return redirect('alumni_list')
    else:
        form = AlumniForm(instance=alumni)
    return render(request, 'base/edit_alumni.html', {'form': form})

def delete_alumni(request, alumni_id):
    alumni = get_object_or_404(Alumni, id=alumni_id)
    alumni.delete()
    return redirect('alumni_list')
