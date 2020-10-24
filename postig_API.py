from instapy_cli import client
import random
from datetime import date
import calendar

username = 'poetryconnects' #your username
password = 'Rhyme79' #your password 
image = 'img/poem.png' #here you can put the image directory

tags = ["instapoetry","poetry", "poetrycommunity", "poetryisnotdead", "poetryofinstagram", "poetryporn", "poetryofig", "poetryinmotion", "poetrygram", "poetrysociety", "poetrylovers", "poetryslam", "poetrycommunityofinstagram", "poetryislife", "poetryclub", "poetrylove", "poetrybook", "poetryhive", "poetryislove", "poetrycosmos", "poetrychallenge", "poetryisart", "poetrybooks", "poetrymaykhana", "poetrylover", "PoetryOfTheDay", "poetrytribe", "poetrybyme", "poetrylife", "poetrycorner", "poetrydaily", "poetryforthepeople", "poetryday", "poetryforlife", "poetrywithlily", "poetryofinsta", "poetryspam", "poetrywriters", "poetryoflife", "poetryprompt", "poetryoutsidethelines", "poetryisonthewall", "poetrycomunity", "poetrypage", "poetryofresistance", "poetrytime", "poetrynetwork", "POETRYNOTDEAD", "poetryofinstagrams", "poetrysocietyinstagram", "poetryphile", "poetryinstagram", "poetrygirl", "poetryaddicts", "poetrytellsastory", "poetrysocietyofinstagram", "poetrycanvas", "poetrypassion", "poetryeverywhere", "poetryfamily", "poetryforchildren", "poetryforever", "poetrygasm", "poetrynyc", "PoetryJunkie", "poetryafrica2017", "poetryandart", "poetrytea", "poetryofamadman", "poetryofthesoul", "poetrybandit", "poetryriot", "poetryuniverse", "poetrylines", "poetrywoman", "poetrycompetition", "poetrysavedme", "poetrytherapy", "poetryfoundation", "poetryig", "poetry247", "poetryandmusic", "poetryandwords", "poetrywriter", "poetryblogger", "poetrybyskye", "poetryismylife", "poetrymusic", "poetryteatime", "poetryofsl", "poetryportrait", "poetrydrug", "PoetryShow", "poetryevent", "poetryeveryday", "PoetryInPaint", "PoetryInABoxSlippers", "poetryfestival", "poetrysquadlove", "poetryisgreat", "PoetryInABox", "poetryhoe", "poetryrocks", "poetryisnotdeath", "poetryaboutlove", "poetryosnotdead", "PoetrySS18", "poetrylanguage", "poetryandprose", "poetryofplace", "poetryofintagram", "poetryiseverywhere", "poetrybyalan", "poetrybyandrealartiste", "poetryjunkies", "poetryonistagram", "poetryoutloud", "poetryofsin", "poetrypublisher", "poetryforchange", "poetryjazzcafe", "poetryforsoul", "poetrythoughts", "PoetryTuesday", "poetrymedicine", "poetryworld", "poetrygem", "poetrygoddess", "poetrymonth2016", "poetryideas", "poetry101", "poetryoig", "poetryandcoffee", "poetryonthestreet", "poetryandlife", "poetrypodcast", "poetrybillboard", "poetryrhyme", "poetrypoemspoetpoem", "poetryobsessed", "poetrycollective", "poetrycommunityofinsta", "poetrycommunitys", "Poetryorsomethinglikethat", "poetryonwalls", "poetryphotography", "poetrycummunity", "poetryreadings", "poetrymood", "poetryheals", "poetryi"]

#generate 20 randomly picked hashtags from this list
hashtags=""
num_tags = len(tags)
for x in range (20):
   hashtags+=" #"+tags[random.randint(0,num_tags)-1] 

#Today!   
my_date = date.today()
day = calendar.day_name[my_date.weekday()] 
   
text = day+'\'s Poem of the day' + '\r\n' + hashtags

with client(username, password) as cli:
    cli.upload(image, text)
	
print ('Posted to Instagram with hashtags:' + hashtags)
