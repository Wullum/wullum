from django import forms

from animals.models import Animals, Comments

class AddAnimal(forms.ModelForm):
    animal_name = forms.CharField(max_length=200, help_text="Navn")
    animal_name.widget.attrs.update({'class': 'u-full-width', 'id':'name'})
    species = forms.CharField(max_length=100, help_text='Art')
    species.widget.attrs.update({'class': 'u-full-width', 'id':'species'})
    born = forms.DateField(help_text='Født')
    born.widget.attrs.update({'class': 'u-full-width', 'id':'born'})
    arrived = forms.DateField(help_text='Ankommet')
    arrived.widget.attrs.update({'class': 'u-full-width', 'id':'arrived'})
    dead = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    animal_characteristics = forms.CharField(widget=forms.Textarea, max_length=400, help_text='Kendetegn')
    animal_characteristics.widget.attrs.update({'class': 'u-full-width', 'id':'animal_characteristics'})
    fur_colour = forms.CharField(max_length=100, help_text='Pelsfarve')
    fur_colour.widget.attrs.update({'class': 'u-full-width', 'id':'fur_colour'})
    fur_type = forms.CharField(max_length=100, help_text='Pelstype')
    fur_type.widget.attrs.update({'class': 'u-full-width', 'id':'fur_type'})
    white_marks = forms.CharField(max_length=100, help_text='Hvide tegninger')
    white_marks.widget.attrs.update({'class': 'u-full-width', 'id':'white_marks'})
    eye_colour = forms.CharField(max_length=100, help_text='Øjenfarve')
    eye_colour.widget.attrs.update({'class': 'u-full-width', 'id':'eye_colour'})
    blue_eyed_white = forms.CharField(max_length=50, help_text='Blue eyed white')
    blue_eyed_white.widget.attrs.update({'class': 'u-full-width', 'id':'blue_eyed_white'})
    genotype = forms.CharField(max_length=50, help_text='Genotype')
    genotype.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})

    class Meta:
        model = Animals
        fields = ('animal_name', 'species', 'born', 'arrived', 'animal_characteristics', 'fur_colour', 'fur_type', 'white_marks', 'eye_colour', 'blue_eyed_white', 'genotype',)

class AddComment(forms.ModelForm):
    animals = forms.ModelChoiceField(queryset=Animals.objects.all(), help_text='Vælg dyr')
    comments_date = forms.DateField(initial='01/01/01', help_text='Vælg dato')
    comment = forms.CharField(widget=forms.Textarea, max_length=400, help_text='Skriv kommentaren her')
    comment.widget.attrs.update({'class': 'u-full-width', 'id':'comment'})

    class Meta:
        model = Comments
        fields = ('animals', 'comment_date','comment',)
        exclude = ['animals', 'comment_date']