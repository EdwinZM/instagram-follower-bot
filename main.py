from instagram_bot import InstagramBot
import os

INSTAGRAM_EMAIL = "YOUR ACCOUNT'S EMAIL HERE"
INSTAGRAM_PASSWORD = "YOUR PASSWORD HERE"
ACCOUNT_TO_FOLLOW = "THE NAME OF THE ACCOUNT YOU WANT TO FOLLOW HERE WITHOUT THE @"

bot = InstagramBot() 

bot.login(acc=INSTAGRAM_EMAIL, password=INSTAGRAM_PASSWORD)
bot.find_following(ACCOUNT_TO_FOLLOW)
bot.follow()

bot.driver.quit()