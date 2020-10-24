# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'poetryconnects'
insta_password = 'Rhyme79'

comments = ['Beautifully written @{}',
        'Poetry is not dead :raised_hands:',
        'Love your poems @{}',
        'Poetry is the best antidote to cynicism @{}',
        'Your words are an inspiration @{}',
        'Yes! It captures that very special atmosphere',
		'Poetry Connects us beyond our differences. Thank you!!',
        'I can feel your passion for poetry @{} :muscle:',
		'Thank you for your wonderful words @{}']
		
tags = ["instapoetry","poetry", "poetrycommunity", "poetryisnotdead", "poetryofinstagram", "poetryporn", "poetryofig", "poetryinmotion", "poetrygram", "poetrysociety", "poetrylovers", "poetryslam", "poetrycommunityofinstagram", "poetryislife", "poetryclub", "poetrylove", "poetrybook", "poetryhive", "poetryislove", "poetrycosmos", "poetrychallenge", "poetryisart", "poetrybooks", "poetrymaykhana", "poetrylover", "PoetryOfTheDay", "poetrytribe", "poetrybyme", "poetrylife", "poetrycorner", "poetrydaily", "poetryforthepeople", "poetryday", "poetryforlife", "poetrywithlily", "poetryofinsta", "poetryspam", "poetrywriters", "poetryoflife", "poetryprompt", "poetryoutsidethelines", "poetryisonthewall", "poetrycomunity", "poetrypage", "poetryofresistance", "poetrytime", "poetrynetwork", "POETRYNOTDEAD", "poetryofinstagrams", "poetrysocietyinstagram", "poetryphile", "poetryinstagram", "poetrygirl", "poetryaddicts", "poetrytellsastory", "poetrysocietyofinstagram", "poetrycanvas", "poetrypassion", "poetryeverywhere", "poetryfamily", "poetryforchildren", "poetryforever", "poetrygasm", "poetrynyc", "PoetryJunkie", "poetryafrica2017", "poetryandart", "poetrytea", "poetryofamadman", "poetryofthesoul", "poetrybandit", "poetryriot", "poetryuniverse", "poetrylines", "poetrywoman", "poetrycompetition", "poetrysavedme", "poetrytherapy", "poetryfoundation", "poetryig", "poetry247", "poetryandmusic", "poetryandwords", "poetrywriter", "poetryblogger", "poetrybyskye", "poetryismylife", "poetrymusic", "poetryteatime", "poetryofsl", "poetryportrait", "poetrydrug", "PoetryShow", "poetryevent", "poetryeveryday", "PoetryInPaint", "PoetryInABoxSlippers", "poetryfestival", "poetrysquadlove", "poetryisgreat", "PoetryInABox", "poetryhoe", "poetryrocks", "poetryisnotdeath", "poetryaboutlove", "poetryosnotdead", "PoetrySS18", "poetrylanguage", "poetryandprose", "poetryofplace", "poetryofintagram", "poetryiseverywhere", "poetrybyalan", "poetrybyandrealartiste", "poetryjunkies", "poetryonistagram", "poetryoutloud", "poetryofsin", "poetrypublisher", "poetryforchange", "poetryjazzcafe", "poetryforsoul", "poetrythoughts", "PoetryTuesday", "poetrymedicine", "poetryworld", "poetrygem", "poetrygoddess", "poetrymonth2016", "poetryideas", "poetry101", "poetryoig", "poetryandcoffee", "poetryonthestreet", "poetryandlife", "poetrypodcast", "poetrybillboard", "poetryrhyme", "poetrypoemspoetpoem", "poetryobsessed", "poetrycollective", "poetrycommunityofinsta", "poetrycommunitys", "Poetryorsomethinglikethat", "poetryonwalls", "poetryphotography", "poetrycummunity", "poetryreadings", "poetrymood", "poetryheals", "poetryi"]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
   
  # general settings		
  # session.set_dont_include(["friend1", "friend2", "friend3"])		
  # https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
  # activity		
  
  # session.set_smart_hashtags(['poetry', 'writing'], limit=3, sort='top', log_tags=True)
  # session.like_by_tags(amount=10, use_smart_hashtags=True)
  
  # Exclude unwanted
  session.set_dont_like(["naked", "nsfw", "sex", "nigga", "fuck"])
 
  # Liking
  session.set_delimit_liking(enabled=True, max_likes=50, min_likes=1)
  
  # Follow
  session.set_do_follow(True, percentage=50)
  session.set_dont_unfollow_active_users(enabled=True, posts=5)
  session.set_relationship_bounds(enabled=True, potency_ratio=1.5, delimit_by_numbers=True, max_followers=10005, max_following=24200, min_followers=10, min_following=0)

  #session.set_relationship_bounds(min_posts=3, max_posts=10000)

  # Comments
  session.set_do_comment(True, percentage=40)
  session.set_delimit_commenting(enabled=True, max_comments=32, min_comments=0)
  
  # Spare Friends
  session.set_dont_include(['yeonchoi'])
  
  # Mandatory Language
  session.set_mandatory_language(enabled=True, character_set=['LATIN'])
  
  # Quota
  session.set_quota_supervisor(enabled=True, peak_comments_daily=100, peak_comments_hourly=21)
  session.set_relationship_bounds(enabled=True, max_followers=8500)
  
  # Activity
  session.like_by_tags(tags, amount=20)
  
  session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)
						   
  session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=601)

  # Joining Engagement Pods
  session.set_do_comment(enabled = True, percentage = 50)
  session.set_comments(comments, media = 'Photo')
  session.join_pods(topic='general', engagement_mode='no_comments')
  
  #session.end()