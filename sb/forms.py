#forms.py

from django import forms
from .models import Syllabus

class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = (
        	'university',
			'state',
			'prof_last', 
			'prof_first', 
			'course_name', 
			'course_code',
			'credits', 
			'course_level',
			'year',
			'term',
			'rate_my_prof_url', 
			'pdf_doc' 
		)