from django import  forms
class enterycreateform(forms.Form):
    title=forms.CharField(widget=forms.Textarea(attrs={'cols':"60",'rows':"20",'style':'height:100px'}))
    content=forms.Textarea()
    