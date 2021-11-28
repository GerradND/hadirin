from django.shortcuts import render

def index(request):
    return render(request, 'perizinan/index.html')

def validasi_izin(request):
    context = {
        'daftar_izin': [
            {'id': 1,
            'staf': 'Agung',
            'tanggal': '22/06/2021',
            'keterangan': 'Capek kerja pak',
            'status': 'pending'},
            {'id': 2,
            'staf': 'Bejo',
            'tanggal': '22/06/2022',
            'keterangan': 'Sama pak',
            'status': 'pending'}
            ]
    }
    return render(request, 'perizinan/validasi_izin.html', context)

def detail_izin(request, id):
    context = {
        'izin': {
            'id': 1,
            'staf': 'Agung',
            'tanggal': '22/06/2021',
            'keterangan': 'Capek kerja pak',
            'status': 'pending'
            }
    }
    return render(request, 'perizinan/detail_izin.html', context)

def add_izin(request):
    return render(request, 'perizinan/add_izin.html')

def add(request):
    return render(request, 'perizinan/index.html')