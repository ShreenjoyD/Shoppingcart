from django.shortcuts import redirect, render
from django.db.models import Q
from .models import details
from django.shortcuts import get_object_or_404
import csv
import random
from random import *
import pandas as pd
from pandas import DataFrame
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from django.http import StreamingHttpResponse

# Create your views here.

class Echo:
    def write(self, value):
        return value

def streamcsv(request):
    rows = (["Row {}".format(idx), str(idx)] for idx in range(1000))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv",
        headers={'Content-Disposition': 'attachment; filename="dataf.csv"'},
    )

def index(request):
    return render(request, 'index.html')


def presults(request):
    query=None
    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=details.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(genres__icontains=query) )
    return  render(request,'postresults.html',{'query': query,
                                          'results': results})
          

def purchase(request, id):
    obj=get_object_or_404(details, pk=id)
    return render(request,'booktocart.html', {'obj':obj})
    
def addtocart(request):
	b = pd.read_csv('C:\\Users\\User\\cart\\cart\\maincart\\dataf.csv', sep=',', error_bad_lines=False, encoding ='latin-1')
	b.columns = ['ID','Genre']
	tf = TfidfVectorizer(analyzer='word', ngram_range=(1,2), min_df=0, stop_words='english')
	tfidf_matrix = tf.fit_transform(b['Genre'])
	mnb= MultinomialNB(tfidf_matrix, tfidf_matrix)
	results={}
	for i, row in b.iterrows():
		similar_indices = mnb[i].argsort()[:-100:-1]
		similar_items = [(b['ID'][j]) for j in similar_indices]
		row_id = row['ID']
		results[row_id] = similar_items
		results[row_id].pop(results[row_id].index((row_id)))
    return render(request,'index.html', {'results':results})    
   
