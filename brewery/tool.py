from django.utils.crypto import get_random_string
from string import ascii_lowercase

def random_slug(slug, length=4):
	random_string = get_random_string(length=length, allowed_chars=ascii_lowercase)
	return '%s-%s' %(slug,random_string)