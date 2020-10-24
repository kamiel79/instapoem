# First, you should install flickrapi
# pip install flickrapi

#returns true if image saved 
#returns false otherwise
def get_flickr_img (keyword, filename):
	import flickrapi
	import urllib
	from PIL import Image

	# see https://joequery.me/code/flickr-api-image-search-python/

	# Flickr api access key 
	flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

	insta_size = (612, 612)
	if (keyword == ""):
		return False
	try:
		photos = flickr.walk(text=keyword,
						 tag_mode='all',
						 tags=keyword,
						 extras='url_c',
						 per_page=10,           # may be you can try different numbers..
						 sort='relevance')
	except:
		return False
	#license 1,4,5,7,9
	#fetch one photo	
	url = False
	for i, photo in enumerate(photos):
		url = photo.get('url_c')
		if i>1:
			break

	if (url):
		# Download image from the url and save it to 'bkg.jpg'
		try:
			urllib.request.urlretrieve(url, filename)
		except:
			return False

		# Resize the image and overwrite it
		image = Image.open(filename) 
		image = image.resize((insta_size), Image.ANTIALIAS)
		image.save(filename)
		return True
	else:
		return False