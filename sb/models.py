from django.db import models

# Create your models here.

class Syllabus(models.Model):
	university = models.CharField(max_length=30)
	STATE_SELECTION = (
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AR', 'Arkansas'),
        ('AS', 'American Samoa'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'District of Columbia'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('GU', 'Guam'),
        ('HI', 'Hawaii'),
        ('IA', 'Iowa'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MO', 'Missouri'),
        ('MP', 'Northern Mariana Islands'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NA', 'National'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NE', 'Nebraska'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VA', 'Virginia'),
        ('VI', 'Virgin Islands'),
        ('VT', 'Vermont'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming'),
	)
	state = models.CharField(max_length=2, choices=STATE_SELECTION)
	prof_last = models.CharField(max_length=30)
	prof_first = models.CharField(max_length=30)
	course_name = models.CharField(max_length=100)
	course_code = models.CharField(max_length=30)
	credits = models.CharField(max_length=30)
	COURSE_LEVEL_SELECTION = (
		('D', 'Developmental'),
		('U', 'Undergraduate'),
		('G', 'Graduate'),
	)
	course_level = models.CharField(max_length=1, choices=COURSE_LEVEL_SELECTION)
	year = models.CharField(max_length=4)
	TERM_SELECTION = (
		('FA', 'Fall'),
		('WI', 'Winter'),
		('SP', 'Spring'),
		('SU', 'Summer'),
	)
	term = models.CharField(max_length=2, choices=TERM_SELECTION)
	rate_my_prof_url = models.URLField(max_length=500)
	pdf_doc = models.FileField(upload_to='pdf/')
	uploaded_at = models.DateTimeField(auto_now_add=True)