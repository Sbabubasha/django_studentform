from django import forms

g=[('MALE','male'),('FEMALE','female'),('OTHER','other')]
c=[('python','PYTHON'),('JAVA','java'),('MERN','mern'),('django','django')]

class Studentform(forms.Form):
    name=forms.CharField(max_length=20)
    aadhaar=forms.IntegerField()
    age=forms.IntegerField()
    mobno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=8,widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.ChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    address=forms.CharField(max_length=50,widget=forms.Textarea)