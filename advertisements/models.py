from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
# Create your models here.

class Adv(models.Model):
    title = models.CharField(verbose_name= 'name', max_length = 80)#verbose_name = представление в админке 
    description = models.TextField()
    price = models.DecimalField(max_digits = 12, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True, )
    updated_at = models.DateTimeField(auto_now = True)
    auction = models.BooleanField(help_text = "Select - auction or not")

    @admin.display(description = 'Created at')
    def chd(self): 
        l_time = timezone.localtime(self.created_at)
        if self.created_at.date() == timezone.now().date():
            c_time = l_time.time().strftime('%H:%M')
            return format_html("<span style='color:green'> today at {} </span>", c_time) #green span 
        return l_time
    
    @admin.display(description = 'Updated at')
    def chu(self):
        l_time = timezone.localtime(self.updated_at)
        if self.updated_at.date() == timezone.now().date():
            c_time = l_time.time().strftime('%H:%M')
            return format_html("<span style='color:red'> today at {} </span>", c_time)#red span
        return l_time
        
    class Meta:
        db_table = "advertisements"
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

        
    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"