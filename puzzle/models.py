from django.db import models

# Create your models here.

	
class product(models.Model):   #ibps rrb clerk

	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'product'

class rrbpo(models.Model): 
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1

	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'rrbpo'
class ibpsclerk(models.Model):
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'ibpsclerk'
class ibpspo(models.Model):
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'ibpspo'
#################################################################################################################################################################
class rrbclerkmain(models.Model):   #ibps rrb clerk
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'rrbclerkmain'

class rrbpomain(models.Model): 
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1

	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'rrbpomain'
class ibpsclerkmain(models.Model):
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'ibpsclerkmain'
class ibpspomain(models.Model):
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'ibpspomain'
	
class sbipo(models.Model):
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	




	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'sbipo'
	
class sbiclerk(models.Model):
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	




	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'sbiclerk'
class sbipomain(models.Model):
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	




	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'sbipomain'
class sbiclerkmain(models.Model):
	id = models.AutoField(primary_key=True)
	puzzle_hindi=models.TextField()
	puzzle_eng=models.TextField()
	




	solution_img= models.ImageField(upload_to="gallery/",null=True)
	#q1
	question_1=models.CharField(max_length=500)
	question1_answer=models.CharField(max_length=200)
	question1_option_1=models.CharField(max_length=200)
	question1_option_2=models.CharField(max_length=200)
	question1_option_3=models.CharField(max_length=200)
	question1_option_4=models.CharField(max_length=200)
	#q2
	question_2=models.CharField(max_length=500)
	question2_answer=models.CharField(max_length=200)
	question2_option_1=models.CharField(max_length=200)
	question2_option_2=models.CharField(max_length=200)
	question2_option_3=models.CharField(max_length=200)
	question2_option_4=models.CharField(max_length=200)
	#q3
	question_3=models.CharField(max_length=500)
	question3_answer=models.CharField(max_length=200)
	question3_option_1=models.CharField(max_length=200)
	question3_option_2=models.CharField(max_length=200)
	question3_option_3=models.CharField(max_length=200)
	question3_option_4=models.CharField(max_length=200)
	#q4
	question_4=models.CharField(max_length=500)
	question4_answer=models.CharField(max_length=200)
	question4_option_1=models.CharField(max_length=200)
	question4_option_2=models.CharField(max_length=200)
	question4_option_3=models.CharField(max_length=200)
	question4_option_4=models.CharField(max_length=200)
	#q5
	question_5=models.CharField(max_length=500)
	question5_answer=models.CharField(max_length=200)
	question5_option_1=models.CharField(max_length=200)
	question5_option_2=models.CharField(max_length=200)
	question5_option_3=models.CharField(max_length=200)
	question5_option_4=models.CharField(max_length=200)
	class Meta:
		db_table = 'sbiclerkmain'
