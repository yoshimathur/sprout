import time 
import firebase_admin
import locale

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from firebase_admin import credentials
from firebase_admin import firestore

# db setup
cred = credentials.Certificate("/Users/yashmathur/Downloads/sprout-akcyl333-firebase-adminsdk-4bq7t-5594ca04c8.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()
db = firestore_client.collection("insta")

username = "yoshimathur"
password = "Aryan2007"

# driver setup
driver = webdriver.Chrome(ChromeDriverManager().install())
actions = ActionChains(driver)
driver.get("https://www.instagram.com")
driver.maximize_window()
time.sleep(10)

# locale setup 
locale.setlocale(locale.LC_ALL, '')

# log in 
inputs = driver.find_elements(By.TAG_NAME, "input")
for input in inputs:
    if input.get_attribute("aria-label") == "Phone number, username, or email":
        print("Entering username...")
        input.send_keys(username)
        print("Entered username...")

    if input.get_attribute("aria-label") == "Password":
        print("Entering password...")
        input.send_keys(password)
        print("Entered password...")
        break

print("Clicking log in...")
button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
button.click()
print("Clicked log in ...")
time.sleep(10)

# clearing info dialog
print("Clearing dialog...")
buttons = driver.find_elements(By.TAG_NAME, "button")
for button in buttons:
    if button.get_attribute("innerHTML").strip() == "Not Now":
        button.click()
        print("Cleared dialog...")
        time.sleep(2)
        break

# clearing notification dialog
buttons = driver.find_elements(By.TAG_NAME, "button")
for button in buttons:
    if button.get_attribute("innerHTML").strip() == "Not Now":
        button.click()
        print("Cleared dialog...")
        time.sleep(2)
        break

# collecting images from people
links = ["https://www.instagram.com/kimkardashian/", "https://www.instagram.com/khloekardashian/", "https://www.instagram.com/kourtneykardash/", "https://www.instagram.com/bellahadid/", "https://www.instagram.com/gigihadid/", "https://www.instagram.com/zendaya/", "https://www.instagram.com/emmachamberlain/", "https://www.instagram.com/oliviarodrigo/", "https://www.instagram.com/billieeilish/", "https://www.instagram.com/badgalriri/", "https://www.instagram.com/arianagrande/", "https://www.instagram.com/dualipa/", "https://www.instagram.com/matildadjerf/", "https://www.instagram.com/selenagomez/", "https://www.instagram.com/iamcardib/", "https://www.instagram.com/haileybieber/", "https://www.instagram.com/staskaranikolaou/", "https://www.instagram.com/emrata/", "https://www.instagram.com/devonleecarlson/", "https://www.instagram.com/gracieabrams/", "https://www.instagram.com/lilychee/", "https://www.instagram.com/lilyrose_depp/", "https://www.instagram.com/mimimoocher/", "https://www.instagram.com/rosalia.vt/", "https://www.instagram.com/_dilone/", "https://www.instagram.com/anokyai/", "https://www.instagram.com/jlo/", "https://www.instagram.com/victoriaparis/", "https://www.instagram.com/addisonraee/", "https://www.instagram.com/voguerunway/", "https://www.instagram.com/voguemagazine/", "https://www.instagram.com/vogue/", "https://www.instagram.com/emmamacdonald/", "https://www.instagram.com/maggiemacdonald/", "https://www.instagram.com/tessamaethompson/", "https://www.instagram.com/theestallion/", "https://www.instagram.com/hoskelsa/", "https://www.instagram.com/victoriabeckham/", "https://www.instagram.com/jodiesmith/", "https://www.instagram.com/hedislimane/", "https://www.instagram.com/harpersbazaarus/", "https://www.instagram.com/anyataylorjoy/", "https://www.instagram.com/charlidamelio/", "https://www.instagram.com/dixiedamelio/", "https://www.instagram.com/tayrussell/", "https://www.instagram.com/kaiagerber/", "https://www.instagram.com/isseymiyakeofficial/", "https://www.instagram.com/rickowensonline/", "https://www.instagram.com/jennaortega/", "https://www.instagram.com/beyonce/", "https://www.instagram.com/bryonjavar/", "https://www.instagram.com/tiffanyhaddish/", "https://www.instagram.com/luxurylaw/", "https://www.instagram.com/jasonrembert/", "https://www.instagram.com/sza/", "https://www.instagram.com/kehlani/", "https://www.instagram.com/zerinaakers/", "https://www.instagram.com/thomascarterphillips/", "https://www.instagram.com/violadavis/", "https://www.instagram.com/gal_gadot/", "https://www.instagram.com/milliebobbybrown/", "https://www.instagram.com/mimicuttrell/", "https://www.instagram.com/elizabethstewart1/", "https://www.instagram.com/meganfox/", "https://www.instagram.com/stylememaeve/", "https://www.instagram.com/lorenzoposocco/", "https://www.instagram.com/venedaacarter/", "https://www.instagram.com/suedebrooks/", "https://www.instagram.com/fatherkels/", "https://www.instagram.com/alexademie/", "https://www.instagram.com/sydney_sweeney/", "https://www.instagram.com/hunterschafer/", "https://www.instagram.com/maudeapatow/", "https://www.instagram.com/barbieferreira/", "https://www.instagram.com/evaniefrausto/", "https://www.instagram.com/hommeplisse_isseymiyake/", "https://www.instagram.com/celinedion/", "https://www.instagram.com/kerrywashington/", "https://www.instagram.com/priyankachopra/", "https://www.instagram.com/danixmichelle/", "https://www.instagram.com/illjahjah/", "https://www.instagram.com/kateyoung/", "https://www.instagram.com/nyfw/", "https://www.instagram.com/nyfwshows.dcsw/", "https://www.instagram.com/explore/tags/nyfw/", "https://www.instagram.com/explore/tags/kendalljenner/", "https://www.instagram.com/explore/tags/emmachamberlain/", "https://www.instagram.com/cosmopolitan/", "https://www.instagram.com/closetofemmachambie/", "https://www.instagram.com/closetofbellahadid/", "https://www.instagram.com/explore/tags/bellahadid/", "https://www.instagram.com/explore/tags/voguefashion/", "https://www.instagram.com/bof/", "https://www.instagram.com/heavn/", "https://www.instagram.com/themetgalaofficial/", "https://www.instagram.com/oscardelarenta/", "https://www.instagram.com/aimeesong/", "https://www.instagram.com/jessicawang/", "https://www.instagram.com/lilamoss/", "https://www.instagram.com/katemossagency/", "https://www.instagram.com/amaliestar/", "https://www.instagram.com/nigo/", "https://www.instagram.com/matthieu_blazy/", "https://www.instagram.com/viviennewestwood/", "https://www.instagram.com/demnagram/", "https://www.instagram.com/ibrahimkamara_/", "https://www.instagram.com/guapmag/", "https://www.instagram.com/dazedfashion/", "https://www.instagram.com/alessandrarich/"]

for link in links:
    driver.get(link)
    time.sleep(5)

    # get name
    nametag = driver.find_elements(By.TAG_NAME, "h2")
    name = nametag[0].get_attribute("innerText")

    # getting posts
    print("Collecting posts...")
    postCountTag = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[1]/div/span/span")
    postCount = int(locale.atof(postCountTag.get_attribute("innerText")))

    article = driver.find_element(By.TAG_NAME, "article")
    postLinks = set(map(lambda x: x.get_attribute("href"), article.find_elements(By.TAG_NAME, "a")))

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    # world won't end if we miss one - instagram dumb too dw 
    while len(postLinks) != postCount: 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        postLinks.update(map(lambda x: x.get_attribute("href"), article.find_elements(By.TAG_NAME, "a")))

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print("Received " + str(len(postLinks)) + " posts from " + str(name))
    
    for postLink in postLinks: 
        split = postLink.split("/")
        index = len(split) - 2
        docID = split[index] 

        # save doc as shell to db
        db.document(docID).update({"user" : name, "diln" : postCount})

    print("Saved " + str(len(postLinks)) + " posts from " + str(name))


time.sleep(10)
print("End of script!")