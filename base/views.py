from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@csrf_exempt 
def display_table(request):
    if request.method == 'POST' and request.FILES.get('json_file'):
        try:
            # Read the uploaded JSON file
            uploaded_file = request.FILES['json_file']
            json_data = json.load(uploaded_file)

            # Check if JSON data is a list of dictionaries
            if isinstance(json_data, list) and all(isinstance(row, dict) for row in json_data):
                columns = list(json_data[0].keys())
                data = json_data
            else:
                columns = []
                data = []

            return render(request, 'base/table.html', {
                'columns': columns,
                'data': data
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON file'}, status=400)
    return render(request, 'base/input.html')









# from django.shortcuts import render
# import pandas as pd
# import os

# def display_table(request):
#     # Path to the uploaded Excel file
#     excel_file_path = "C:/Users/sawai/OneDrive - National Institute of Technology, Rourkela/Desktop/Data Table Test.xlsx"
    
#     # Read Excel file into a DataFrame
#     df = pd.read_excel(excel_file_path)
    
#     # Convert DataFrame to a list of dictionaries
#     data = df.to_dict('records')
#     columns = df.columns
    
#     return render(request, 'base/table.html', {
#         'data': data,
#         'columns': columns
#     })
