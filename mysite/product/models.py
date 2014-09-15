from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Product(models.Model):
	#id    = models.AutoField(primary_key=True)
	name   = models.CharField(max_length=200)
	price  = models.DecimalField(max_digits=10, decimal_places=2,default=0)
	stock  = models.IntegerField(default=0)
	image  = models.ImageField('Image', upload_to = '.', default = '', null=True, blank=True)
	description = models.CharField(max_length=500)

	# VODKA = 'vodka'
	# WHISKEY = 'whiskey'
	# GIN = 'gin'
	# SPECIAL = 'special'
	# ALC_CHOICES= (
	# 	(GIN, 'Gin'),
	# 	(VODKA, 'Vodka'),
	# 	(WHISKEY, 'Whiskey'),
	# 	(SPECIAL, 'Special'),
	# )
	# alcohol_tags= models.CharField(max_length=50,choices=ALC_CHOICES,default=SPECIAL)

	def __str__(self):
		return self.name

class Alcohol(Product):
	VODKA = 'vodka'
	WHISKEY = 'whiskey'
	GIN = 'gin'
	SPECIAL = 'special'
	ALC_CHOICE= (
		(GIN, 'Gin'),
		(VODKA, 'Vodka'),
		(WHISKEY, 'Whiskey'),
		(SPECIAL, 'Special'),
	)
	alc_tags= models.CharField(max_length=50,choices=ALC_CHOICE,default=VODKA)

	def __str__(self):
		return self.name

class Shoe(Product):
	DIABETIC= 'diabetic'
	ORTHOTIC = 'orthotic'
	RUNNING= 'running'
	NONE = 'none'
	SHOE_CHOICE= (
		(RUNNING, 'Running'),
		(ORTHOTIC, 'Orthotic'),
		(DIABETIC, 'Diabetic'),
		(NONE, 'None'),
	)
	shoe_tags= models.CharField(max_length=50,choices=SHOE_CHOICE,default=NONE,null=True,blank=True)

	def __str__(self):
		return self.name


class UserProfile(models.Model):
	# This field is required.
	user = models.OneToOneField(User)

	# Other fields here
	favorites = models.ManyToManyField(Product)



# definition of UserProfile from above
# ...
#
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)
#
#post_save.connect(create_user_profile, sender=User)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])