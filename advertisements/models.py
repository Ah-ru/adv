from django.db import models

# Create your models here.

class Adv(models.Model):

    title = models.CharField(max_length = 80)
    description = models.TextField()
    price = models.DecimalField(max_digits = 12, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    auction = models.BooleanField(help_text = "Select - auction or not")
    class Meta:
        db_table = "advertisements"
        
        def __str__(self):
            return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"