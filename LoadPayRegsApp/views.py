from django.shortcuts import render, redirect 
#from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import TableAndUrlColumnsForm 
from .models import DocFile, TableAndUrlColumns
from .utils import total_result, read_doc
 
# Воображаемая функция для обработки загруженного файла:
###
 
# Create your views here:
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        doc = DocFile(docfile = uploaded_file)
        doc.save()
        read_doc(doc.docfile.path)
        return redirect(to='table')
    else:
        return render(request, 'upload_file.html')

def table(request):
    row = TableAndUrlColumns.objects.all()
    res1, res2 = total_result()
    context = {
        'row_list': row,
        'result_1': res1,
        'result_2': res2,
    }
    return render(request, 'table.html', context)
    
def redirect_result(request):
    return redirect('table.html')