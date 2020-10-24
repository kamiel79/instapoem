from env import *
from PIL import Image, ImageDraw, ImageFont
import calendar
import random
from datetime import date
import glob
import sys
import os.path
import shutil

WEBDRIVER_PATH = r"C:\DRIVERS\chromedriver.exe"	#Set your webdriver path
ARCHIVE_PATH = "archive/"
IMAGE_PATH = "img/"
FONTS_PATH = "fonts/"
main_url = "https://www.instagram.com"

#Settings for text rendering
DEFAULT_BKG_DIR = 'img/default/'
DEFAULT_POEMS_DIR = 'poems/'
THE_FLICKR_IMAGE = 'img/bkg.jpg'
FONT_SIZE = 32
TITLE_SIZE = FONT_SIZE * 2
SMALL_SIZE = 16
MARGIN_RATIO = 1.2
MAX_POEM_PROPORTION = 0.7
#variables for image size
x1 = 612
y1 = 612
TEXT_COLOR = (240,240,240)
TINT_COLOR = (0, 0, 0)  # Black
TRANSPARENCY = .75  # Degree of transparency, 0-100%
OPACITY = int(255 * TRANSPARENCY)
credits = "© 2020 poetry_connects & creativechoice.org | share the love for poetry"


#selection of poetry related hashtags
possible_hashtags = ["instapoetry","poetry", "poetrycommunity", "poetryisnotdead", "poetryofinstagram", "poetryporn", "poetryofig", "poetryinmotion", "poetrygram", "poetrysociety", "poetrylovers", "poetryslam", "poetrycommunityofinstagram", "poetryislife", "poetryclub", "poetrylove", "poetrybook", "poetryhive", "poetryislove", "poetrycosmos", "poetrychallenge", "poetryisart", "poetrybooks", "poetrymaykhana", "poetrylover", "PoetryOfTheDay", "poetrytribe", "poetrybyme", "poetrylife", "poetrycorner", "poetrydaily", "poetryforthepeople", "poetryday", "poetryforlife", "poetrywithlily", "poetryofinsta", "poetryspam", "poetrywriters", "poetryoflife", "poetryprompt", "poetryoutsidethelines", "poetryisonthewall", "poetrycomunity", "poetrypage", "poetryofresistance", "poetrytime", "poetrynetwork", "POETRYNOTDEAD", "poetryofinstagrams", "poetrysocietyinstagram", "poetryphile", "poetryinstagram", "poetrygirl", "poetryaddicts", "poetrytellsastory", "poetrysocietyofinstagram", "poetrycanvas", "poetrypassion", "poetryeverywhere", "poetryfamily", "poetryforchildren", "poetryforever", "poetrygasm", "poetrynyc", "PoetryJunkie", "poetryafrica2017", "poetryandart", "poetrytea", "poetryofamadman", "poetryofthesoul", "poetrybandit", "poetryriot", "poetryuniverse", "poetrylines", "poetrywoman", "poetrycompetition", "poetrysavedme", "poetrytherapy", "poetryfoundation", "poetryig", "poetry247", "poetryandmusic", "poetryandwords", "poetrywriter", "poetryblogger", "poetrybyskye", "poetryismylife", "poetrymusic", "poetryteatime", "poetryofsl", "poetryportrait", "poetrydrug", "PoetryShow", "poetryevent", "poetryeveryday", "PoetryInPaint", "PoetryInABoxSlippers", "poetryfestival", "poetrysquadlove", "poetryisgreat", "PoetryInABox", "poetryhoe", "poetryrocks", "poetryisnotdeath", "poetryaboutlove", "poetryosnotdead", "PoetrySS18", "poetrylanguage", "poetryandprose", "poetryofplace", "poetryofintagram", "poetryiseverywhere", "poetrybyalan", "poetrybyandrealartiste", "poetryjunkies", "poetryonistagram", "poetryoutloud", "poetryofsin", "poetrypublisher", "poetryforchange", "poetryjazzcafe", "poetryforsoul", "poetrythoughts", "PoetryTuesday", "poetrymedicine", "poetryworld", "poetrygem", "poetrygoddess", "poetrymonth2016", "poetryideas", "poetry101", "poetryoig", "poetryandcoffee", "poetryonthestreet", "poetryandlife", "poetrypodcast", "poetrybillboard", "poetryrhyme", "poetrypoemspoetpoem", "poetryobsessed", "poetrycollective", "poetrycommunityofinsta", "poetrycommunitys", "Poetryorsomethinglikethat", "poetryonwalls", "poetryphotography", "poetrycummunity", "poetryreadings", "poetrymood", "poetryheals", "poetryi"]

def get_hashtags(number):
	hashtags = ""
	num_tags = len(possible_hashtags)
	for x in range (number):
		hashtags+=" #" + possible_hashtags[random.randint(0,num_tags)-1] 
	return hashtags
	
def archive(filename):
	print("Archiving: " + filename)
	if (os.path.isfile(ARCHIVE_PATH + filename)):
		print ("File already archived")
	else:
		newpath = shutil.move (filename, ARCHIVE_PATH)
		print(newpath)
	
def get_image():
	#if image in args, load it
	if (len(sys.argv) == 2):
		imagename = sys.argv[1]
		imagename = ABSOLUTE_PATH + imagename
	else:
		#if not 1 parameter, use most recent file in folder
		list_of_files = glob.glob(ABSOLUTE_PATH + '\*.png')
		if (list_of_files):
			imagename = max(list_of_files, key=os.path.getctime)

	return imagename
	
def get_font():
	fntnames = ('Gabriola.ttf', 'ufonts.com_futura-t-light.ttf', 'iskpotab.ttf', 'MRSEA~10.TTF','BirchStd.otf', 'NotoSerif-Light.ttf', 'plantc.ttf', 'sylfaen.ttf')
	x = random.randint(0, len(fntnames)-1)
	fntname = fntnames[x]
	return fntname

def darken(img, treshold):
	if (treshold > 0.30):
		#overlay
		overlay = Image.new('RGBA', img.size, (255,255,255))
		draw = ImageDraw.Draw(overlay)  # Create a context for drawing things on it.
		draw.rectangle(((0, 0), (612, 612)), fill=TINT_COLOR+(10,))
		img = Image.alpha_composite(img, overlay)
	return img
	
def add_line_breaks(poem, fnt):
	#find the average size of the letter
	sum = 0
	for letter in poem:
	  sum += fnt.getsize(letter)[0]
	 
	average_length_of_letter = sum/len(poem)
	#find the number of letters to be put on each line using ratio
	number_of_letters_for_each_line = int((x1/MARGIN_RATIO)/average_length_of_letter)
	print(str(number_of_letters_for_each_line) + " letters per line.")
	result = ""
	incrementer = 0
	for letter in poem:
		if(letter == '~'):
			result += '\n\n' + letter
		elif(letter =='/' or letter == '\n'):
			result += '\n'
			incrementer=0
		elif(incrementer < number_of_letters_for_each_line):
			result += letter
		else:
			if(letter == ' ' or letter == '\n'):
				result += '\n'
				incrementer = 0
			else:
				result += letter
		incrementer+=1
	return result
	
#Today's weekday
my_date = date.today()
day = calendar.day_name[my_date.weekday()] 

#borrowed from https://gist.github.com/kmohrf/8d4653536aaa88965a69a06b81bcb022
def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale

def shade_block(image, x,y, trans):
	#draw a centered shade block of size x,y, with transparency trans
    overlay = Image.new('RGBA', image.size, TINT_COLOR+(0,))
    x1 = int((image.size[0]-x)/2)
    x2 = image.size[0]-x1
    y1 = int((image.size[0]-y)/2)
    y2 = image.size[0]-y1
    draw = ImageDraw.Draw(overlay)  # Create a context for drawing things on it.
    draw.rectangle(((x1, y1), (x2, y2)), fill=TINT_COLOR+(trans,))
    image = Image.alpha_composite(image, overlay)
    return image
