from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = model.models.CharField(max_length=50)
    pub_date = models.DataTimeField(' date published')
    
    def _str_(self):
        return self.question_text
    
    
    class Choice(models.Models ):
        questions = models.ForeignKey(Question,on_delete=models.CASCADE)
        choice_text =models.IntegerField(default=0)