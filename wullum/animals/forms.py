# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone

from animals.models import Animals, Comments, Weights

ANIMAL_CHOICES = (
    ('Høne', 'Høne'),
    ('Hane', 'Hane'),
    ('Kanin','Kanin'),
    ('Ged', 'Ged'),
    ('Får', 'Får'),
    ('Kat', 'Kat'),
    ('Hund', 'Hund'),
)

EYE_COLOUR_CHOICES = (
    ('0', '---'),
    ('Brun', 'Brun'),
    ('Blå', 'Blå'),
    ('Andet', 'Andet'),
)

FUR_CHOICES = (
    ('0', '---'),
    ('Normal', 'Normal'),
    ('Rex', 'Rex'),
    ('Satin', 'Satin'),
)

A_CHOICES = (
    ('A', 'A'),
    ('A_chi', 'A(chi)'),
    ('A_m', 'A(m)'),
    ('a', 'a'),
)

B_CHOICES = (
    ('B', 'B'),
    ('B_e', 'B(e)'),
    ('B_e_B_e', 'B(e)B(e)'),
    ('b_j', 'b(j)'),
    ('b', 'b'),
)

C_CHOICES = (
    ('C', 'C'),
    ('c', 'c'),
)

D_CHOICES = (
    ('D', 'D'),
    ('d', 'd'),
)

G_CHOICES = (
    ('G', 'G'),
    ('g_o', 'g(o)'),
    ('g', 'g'),
)

K_CHOICES = (
    ('K', 'K'),
    ('k', 'k'),
)

X_CHOICES = (
    ('X', 'X'),
    ('x', 'x'),
    ('xx', 'xx'),
)

class AddAnimal(forms.ModelForm):
    animal_name = forms.CharField(max_length=200, help_text="Navn*")
    animal_name.widget.attrs.update({'class': 'u-full-width', 'id':'name'})
    species = forms.CharField(max_length=100, help_text='Art*', widget=forms.Select(choices=ANIMAL_CHOICES),)
    species.widget.attrs.update({'class': 'u-full-width', 'id':'species'})
    born = forms.DateField(help_text='Født', required=False)
    born.widget.attrs.update({'class': 'u-full-width', 'id':'born'})
    arrived = forms.DateField(help_text='Ankommet*')
    arrived.widget.attrs.update({'class': 'u-full-width', 'id':'arrived'})
    dead = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    animal_characteristics = forms.CharField(widget=forms.Textarea, max_length=400, help_text='Kendetegn*')
    animal_characteristics.widget.attrs.update({'class': 'u-full-width', 'id':'animal_characteristics'})
    fur_colour = forms.CharField(max_length=100, help_text='Pelsfarve*')
    fur_colour.widget.attrs.update({'class': 'u-full-width', 'id':'fur_colour'})
    fur_type = forms.CharField(max_length=100, help_text='Pelstype', widget=forms.Select(choices=FUR_CHOICES))
    fur_type.widget.attrs.update({'class': 'u-full-width', 'id':'fur_type'})
    white_marks = forms.BooleanField(help_text='Hvide tegninger', required=False)
    white_marks.widget.attrs.update({'class': 'u-full-width', 'id':'white_marks'})
    eye_colour = forms.CharField(max_length=100, help_text='Øjenfarve', widget=forms.Select(choices=EYE_COLOUR_CHOICES), required=False)
    eye_colour.widget.attrs.update({'class': 'u-full-width', 'id':'eye_colour'})
    genotype_a1 = forms.CharField(max_length=50, help_text='A1 (Chin mm.)', widget=forms.Select(choices=A_CHOICES), required=False)
    genotype_a1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_a2 = forms.CharField(max_length=50, help_text='A2 (Chin mm.)', widget=forms.Select(choices=A_CHOICES), required=False)
    genotype_a2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_b1 = forms.CharField(max_length=50, help_text='B1 (Gul)', widget=forms.Select(choices=B_CHOICES), required=False)
    genotype_b1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_b2 = forms.CharField(max_length=50, help_text='B2 (Gul)', widget=forms.Select(choices=B_CHOICES), required=False)
    genotype_b2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_c1 = forms.CharField(max_length=50, help_text='C1 (Brun)', widget=forms.Select(choices=C_CHOICES), required=False)
    genotype_c1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_c2 = forms.CharField(max_length=50, help_text='C2 (Brun)', widget=forms.Select(choices=C_CHOICES), required=False)
    genotype_c2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_d1 = forms.CharField(max_length=50, help_text='D1 (Blå)', widget=forms.Select(choices=D_CHOICES), required=False)
    genotype_d1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_d2 = forms.CharField(max_length=50, help_text='D2 (Blå)', widget=forms.Select(choices=D_CHOICES), required=False)
    genotype_d2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_g1 = forms.CharField(max_length=50, help_text='G1 (Vildt)', widget=forms.Select(choices=G_CHOICES), required=False)
    genotype_g1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_g2 = forms.CharField(max_length=50, help_text='G2 (Vildt)', widget=forms.Select(choices=G_CHOICES), required=False)
    genotype_g2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_k1 = forms.CharField(max_length=50, help_text='K1 (Kappe)', widget=forms.Select(choices=K_CHOICES), required=False)
    genotype_k1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_k2 = forms.CharField(max_length=50, help_text='K2 (Kappe)', widget=forms.Select(choices=K_CHOICES), required=False)
    genotype_k2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_x1 = forms.CharField(max_length=50, help_text='X1 (BEW)', widget=forms.Select(choices=X_CHOICES), required=False)
    genotype_x1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_x2 = forms.CharField(max_length=50, help_text='X2 (BEW)', widget=forms.Select(choices=X_CHOICES), required=False)
    genotype_x2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    picture = forms.FileField(required=False)

    class Meta:
        model = Animals
        fields = ('animal_name', 'species', 'born', 'arrived', 'animal_characteristics', 'fur_colour', 'fur_type',
                  'white_marks', 'eye_colour', 'genotype_a1', 'genotype_a2', 'genotype_b1', 'genotype_b2',
                  'genotype_c1', 'genotype_c2', 'genotype_d1', 'genotype_d2', 'genotype_g1', 'genotype_g2',
                  'genotype_k1', 'genotype_k2', 'genotype_x1', 'genotype_x2', 'picture')

class AddComment(forms.ModelForm):
    animals = forms.ModelChoiceField(queryset=Animals.objects.all(), help_text='Vælg dyr', initial='1')
    comments_date = forms.DateField(initial='01/01/01', help_text='Vælg dato')
    comment = forms.CharField(widget=forms.Textarea, max_length=400, help_text='Skriv kommentaren her')
    comment.widget.attrs.update({'class': 'u-full-width', 'id':'comment'})

    class Meta:
        model = Comments
        fields = ('animals', 'comment_date','comment',)
        exclude = ['animals', 'comment_date']

class AddWeight(forms.ModelForm):
    animals_w = forms.ModelChoiceField(queryset=Animals.objects.all(), help_text='Vælg dyr', initial='1')
    weight_date = forms.DateField(initial=timezone.now(), help_text='Vælg dato')
    weight = forms.DecimalField(min_value=0.00)

    class Meta:
        model = Weights
        fields = ('animals_w', 'weight_date', 'weight')

class KillAnimal(forms.ModelForm):
    departure = forms.DateField(initial=timezone.now(), help_text='Vælg dato')
    dead = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = Animals
        fields = ('departure', 'dead')

class RemoveAnimal(forms.ModelForm):
    gone = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = Animals
        fields = ('gone',)

class AddRabbit(forms.ModelForm):
    animal_name = forms.CharField(max_length=200, help_text="Navn*")
    animal_name.widget.attrs.update({'class': 'u-full-width', 'id':'name'})
    species = forms.CharField(max_length=100, help_text='Art*', widget=forms.Select(choices=ANIMAL_CHOICES), initial='Kanin')
    species.widget.attrs.update({'class': 'u-full-width', 'id':'species'})
    born = forms.DateField(help_text='Født', required=False)
    born.widget.attrs.update({'class': 'u-full-width', 'id':'born'})
    arrived = forms.DateField(help_text='Ankommet*')
    arrived.widget.attrs.update({'class': 'u-full-width', 'id':'arrived'})
    dead = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    animal_characteristics = forms.CharField(widget=forms.Textarea, max_length=400, help_text='Kendetegn*')
    animal_characteristics.widget.attrs.update({'class': 'u-full-width', 'id':'animal_characteristics'})
    fur_colour = forms.CharField(max_length=100, help_text='Pelsfarve*')
    fur_colour.widget.attrs.update({'class': 'u-full-width', 'id':'fur_colour'})
    fur_type = forms.CharField(max_length=100, help_text='Pelstype', widget=forms.Select(choices=FUR_CHOICES))
    fur_type.widget.attrs.update({'class': 'u-full-width', 'id':'fur_type'})
    white_marks = forms.BooleanField(help_text='Hvide tegninger', required=False)
    white_marks.widget.attrs.update({'class': 'u-full-width', 'id':'white_marks'})
    eye_colour = forms.CharField(max_length=100, help_text='Øjenfarve', widget=forms.Select(choices=EYE_COLOUR_CHOICES), required=False)
    eye_colour.widget.attrs.update({'class': 'u-full-width', 'id':'eye_colour'})
    genotype_a1 = forms.CharField(max_length=50, help_text='A1 (Chin mm.)', widget=forms.Select(choices=A_CHOICES), required=False)
    genotype_a1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_a2 = forms.CharField(max_length=50, help_text='A2 (Chin mm.)', widget=forms.Select(choices=A_CHOICES), required=False)
    genotype_a2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_b1 = forms.CharField(max_length=50, help_text='B1 (Gul)', widget=forms.Select(choices=B_CHOICES), required=False)
    genotype_b1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_b2 = forms.CharField(max_length=50, help_text='B2 (Gul)', widget=forms.Select(choices=B_CHOICES), required=False)
    genotype_b2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_c1 = forms.CharField(max_length=50, help_text='C1 (Brun)', widget=forms.Select(choices=C_CHOICES), required=False)
    genotype_c1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_c2 = forms.CharField(max_length=50, help_text='C2 (Brun)', widget=forms.Select(choices=C_CHOICES), required=False)
    genotype_c2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_d1 = forms.CharField(max_length=50, help_text='D1 (Blå)', widget=forms.Select(choices=D_CHOICES), required=False)
    genotype_d1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_d2 = forms.CharField(max_length=50, help_text='D2 (Blå)', widget=forms.Select(choices=D_CHOICES), required=False)
    genotype_d2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_g1 = forms.CharField(max_length=50, help_text='G1 (Vildt)', widget=forms.Select(choices=G_CHOICES), required=False)
    genotype_g1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_g2 = forms.CharField(max_length=50, help_text='G2 (Vildt)', widget=forms.Select(choices=G_CHOICES), required=False)
    genotype_g2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_k1 = forms.CharField(max_length=50, help_text='K1 (Kappe)', widget=forms.Select(choices=K_CHOICES), required=False)
    genotype_k1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_k2 = forms.CharField(max_length=50, help_text='K2 (Kappe)', widget=forms.Select(choices=K_CHOICES), required=False)
    genotype_k2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_x1 = forms.CharField(max_length=50, help_text='X1 (BEW)', widget=forms.Select(choices=X_CHOICES), required=False)
    genotype_x1.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    genotype_x2 = forms.CharField(max_length=50, help_text='X2 (BEW)', widget=forms.Select(choices=X_CHOICES), required=False)
    genotype_x2.widget.attrs.update({'class': 'u-full-width', 'id':'genotype'})
    picture = forms.FileField(required=False)

    class Meta:
        model = Animals
        fields = ('animal_name', 'species', 'born', 'arrived', 'animal_characteristics', 'fur_colour', 'fur_type',
                  'white_marks', 'eye_colour', 'genotype_a1', 'genotype_a2', 'genotype_b1', 'genotype_b2',
                  'genotype_c1', 'genotype_c2', 'genotype_d1', 'genotype_d2', 'genotype_g1', 'genotype_g2',
                  'genotype_k1', 'genotype_k2', 'genotype_x1', 'genotype_x2', 'picture')

class AddChicken(forms.ModelForm):
    animal_name = forms.CharField(max_length=200, help_text="Navn*")
    animal_name.widget.attrs.update({'class': 'u-full-width', 'id':'name'})
    species = forms.CharField(max_length=100, help_text='Art*', widget=forms.Select(choices=ANIMAL_CHOICES), initial='Høne')
    species.widget.attrs.update({'class': 'u-full-width', 'id':'species'})
    born = forms.DateField(help_text='Født', required=False)
    born.widget.attrs.update({'class': 'u-full-width', 'id':'born'})
    arrived = forms.DateField(help_text='Ankommet*')
    arrived.widget.attrs.update({'class': 'u-full-width', 'id':'arrived'})
    dead = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    animal_characteristics = forms.CharField(widget=forms.Textarea, max_length=400, help_text='Kendetegn*')
    animal_characteristics.widget.attrs.update({'class': 'u-full-width', 'id':'animal_characteristics'})
    fur_colour = forms.CharField(max_length=100, help_text='Pelsfarve*')
    fur_colour.widget.attrs.update({'class': 'u-full-width', 'id':'fur_colour'})
    fur_type = forms.CharField(required=False, widget=forms.HiddenInput(), initial='---')
    eye_colour = forms.CharField(required=False, widget=forms.HiddenInput(), initial='---')
    white_marks = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    picture = forms.FileField(required=False)

    class Meta:
        model = Animals
        fields = ('animal_name', 'species', 'born', 'arrived', 'dead', 'animal_characteristics', 'fur_colour', 'picture')

class AddGoat(forms.ModelForm):
    animal_name = forms.CharField(max_length=200, help_text="Navn*")
    animal_name.widget.attrs.update({'class': 'u-full-width', 'id':'name'})
    species = forms.CharField(max_length=100, help_text='Art*', widget=forms.Select(choices=ANIMAL_CHOICES), initial='Ged')
    species.widget.attrs.update({'class': 'u-full-width', 'id':'species'})
    born = forms.DateField(help_text='Født', required=False)
    born.widget.attrs.update({'class': 'u-full-width', 'id':'born'})
    arrived = forms.DateField(help_text='Ankommet*')
    arrived.widget.attrs.update({'class': 'u-full-width', 'id':'arrived'})
    dead = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    animal_characteristics = forms.CharField(widget=forms.Textarea, max_length=400, help_text='Kendetegn*')
    animal_characteristics.widget.attrs.update({'class': 'u-full-width', 'id':'animal_characteristics'})
    fur_colour = forms.CharField(max_length=100, help_text='Pelsfarve*')
    fur_colour.widget.attrs.update({'class': 'u-full-width', 'id':'fur_colour'})
    fur_type = forms.CharField(required=False, widget=forms.HiddenInput(), initial='---')
    eye_colour = forms.CharField(required=False, widget=forms.HiddenInput(), initial='---')
    white_marks = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    picture = forms.FileField(required=False)

    class Meta:
        model = Animals
        fields = ('animal_name', 'species', 'born', 'arrived', 'dead', 'animal_characteristics', 'fur_colour', 'picture')
