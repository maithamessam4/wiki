from contextlib import _RedirectStream, redirect_stderr, redirect_stdout
from importlib.resources import contents
from multiprocessing import context
from random import random
from urllib import request
from django.shortcuts import render
from encyclopedia.forms import enterycreateform
import random
import markdown
from . import util
import encyclopedia


def index(request):
    q=request.GET.get('q')
    entries=util.list_entries()
    if q:
        entries=[e for e in entries if q.lower() in e.lower()]
    if q in entries:
        redirect_stdout('wiki:single_entry',entries[0])
            
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })
def single_entry(requesr,title:str):
    content=util.get_entry(title)
    return render(request,'encyclopedia/single_entry.html',context={'title':title,'content':content})
def create(request):
    if request.method=='post':
        form=enterycreateform(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            if title in util.list_entries():
                return render(request,'encyclopedia/error.html',context={
                    'title':f'the entry {title}already exist'})
            content=form.cleaned_data['content']
            util.save_entry(title,content)
            return redirect_stderr('wiki:index')
        return render(request,'encyclopedia/create.html',{'form':form,}) 
    
    
def edit(request, title: str):
    if request.method == 'GET' :
        entries = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', context={
            'title': title,
            'form': edit(initial={'content': entries}),
        })
    elif request.method == 'POST':
        form = edit(request.POST )
        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            entries = util.get_entry(title)
            return render(request, 'encyclopedia/edit.html', context={
                'title':title,
                'form': markdown.markdown(entries),
               })

    
