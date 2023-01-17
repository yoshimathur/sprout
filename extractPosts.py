import time 
import firebase_admin

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

username = ""
password = ""

# db setup
cred = credentials.Certificate("/Users/yashmathur/Downloads/sprout-akcyl333-firebase-adminsdk-4bq7t-5594ca04c8.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()
db = firestore_client.collection("insta")

# driver setup
driver = webdriver.Chrome(ChromeDriverManager().install())
actions = ActionChains(driver)
driver.get("https://www.instagram.com")
driver.maximize_window()
time.sleep(10)

# function to check if element exists
def doesExist(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

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

# getting saved user posts
name = "victoriaparis"
docs = db.where("user", "==", name).stream()

postLinks = set([])
for doc in docs: 
    docID = doc.id
    link = "https://www.instagram.com/p/" + docID +"/"
    print(link)
    postLinks.add(link)

print("Starting post data extraction...")

# function to check if element exists
def doesExist(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

counter = 0
skipped = set([])
# grab data from each post 
for postLink in postLinks: 
    counter = counter + 1
    # opening post
    driver.get(postLink)
    driver.maximize_window()
    time.sleep(5)

    # creating docID 
    split = postLink.split("/")
    index = len(split) - 2
    docID = split[index] 

    # data - date, caption, likes, alt
    data = {}

    # get date
    datePath = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/div[2]/div/div/a/div/time"
    if doesExist(datePath):
        dateTag = driver.find_element(By.XPATH, datePath)
        date = dateTag.get_attribute("datetime")
        data["date"] = str(date)
    else: 
        data["date"] = None

    # get captions and media sources
    captions = set([])
    sources = set([])
    altTags = set([])

    # check for carousel 
    def isCarousel():
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons: 
            if button.get_attribute("aria-label") == "Next":
                return [True, button]
        return [False]

    # caption path 
    captionPath = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span"
    # post media holder
    holderPath = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[1]"
    
    if doesExist(holderPath):
        holder = driver.find_element(By.XPATH, holderPath)
    
        if isCarousel()[0]: 
            # looping through carousel
            while True: 
                try:
                    imgs = holder.find_elements(By.TAG_NAME, "img")
                    srcs = map(lambda x: x.get_attribute("currentSrc"), imgs)
                    alts = map(lambda x: x.get_attribute("alt"), imgs)
                    sources.update(srcs)
                    altTags.update(alts)

                    if doesExist(captionPath):
                        captionTag = driver.find_element(By.XPATH, captionPath)
                        captions.add(captionTag.get_attribute("innerText"))

                    hasNext = isCarousel()
                    if hasNext[0]:
                        hasNext[1].click()
                        time.sleep(1)
                    else: 
                        break 
                except NoSuchElementException: 
                    try: 
                        # get vid src
                        vids = holder.find_elements(By.TAG_NAME, "video")
                        srcs = map(lambda x: x.get_attribute("currentSrc"), vids)
                        alts = map(lambda x: x.get_attribute("alt"), vids)
                        sources.update(srcs)
                        altTags.update(alts)

                        if doesExist(captionPath):
                            print("Got Caption")
                            captionTag = driver.find_element(By.XPATH, captionPath)
                            captions.add(captionTag.get_attribute("innerText"))

                        hasNext = isCarousel()
                        if hasNext[0]:
                            hasNext[1].click()
                            time.sleep(1)
                        else: 
                            break 
                    except NoSuchElementException: 
                        print("No Media Found")
                        continue
        else: 
            # get media src
            try: 
                img = holder.find_element(By.TAG_NAME, "img")
                src = img.get_attribute("currentSrc")
                altTag = img.get_attribute("alt")
                sources.add(src)
                altTags.add(altTag)

                if doesExist(captionPath):
                    captionTag = driver.find_element(By.XPATH, captionPath)
                    captions.add(captionTag.get_attribute("innerText"))
            except NoSuchElementException: 
                try: 
                    video = holder.find_element(By.TAG_NAME, "video")
                    src = video.get_attribute("currentSrc")
                    altTag = video.get_attribute("alt")
                    sources.add(src)
                    altTags.add(altTag)

                    if doesExist(captionPath):
                        captionTag = driver.find_element(By.XPATH, captionPath)
                        captions.add(captionTag.get_attribute("innerText"))
                except NoSuchElementException: 
                    print("No Media Found")

        data["caps"] = list(captions)
        data["srcs"] = list(sources)
        data["alts"] = list(altTags)

        # saving data -> fade the overrites (too costly) -> nvm fixed it
        db.document(docID).update(data)
    else: 
        # post not found? 
        print("No media found...")
        skipped.add(docID)

print(skipped)

print("Completed Data Extraction on " + str(counter) + " posts!")