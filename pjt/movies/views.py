from django.shortcuts import render
import requests

# Create your views here.
def main(request):
    API = '68172b7a51f513b96b7217ac3079c5df'
    resDatas = []
    
    for n in range(1, 6):
        num = str(n)
        LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={API}&language=ko-KR&page={num}"
        listData = requests.get(LIST_URL)
        resDatas.append(listData.json().get('results'))
    context = {
        'resDatas': resDatas
    }
    return render(request, 'movies/main.html', context)