import os
import shutil
import requests
import urllib3
import ssl
import json
import logging
import logging.handlers
import sys
from titlecase import titlecase
from logging import handlers
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from googletrans import Translator
from selenium.webdriver.common.by import By

#Dictionary for tags & Series names
with open('tag_translation.json') as f:
    data = f.read()
    lookup_dict = json.loads(data)

set_lookup_dict = {
    "オナニーで絶頂に達する瞬間に生挿入" : "Insert Big Cock Right Before Climax From Masturbation",
    "この女、ふしだら" : "Naughty Woman",
    "マンコ図鑑" : "Pussy Encyclopedia",
    "女熱大陸" : "The Continent Full Of Hot Girls",
    "ダイナマイト" : "Dynamite",
    "朝から晩まで隙があったら即挿入" : "Fucking All Night Long If I Have A Chance",
    "ネトラレ" : "Cuckold",
    "洗練された大人のいやし亭" : "Luxury Adult Healing Spa",
    "怒涛の連続挿入180分" : "Non Stop XXX for 180min",
    "視界侵入！たちまち挿入！" : "Surprise Ambush",
    "女優魂" : "The Soul Of Actress",
    "いじられ続けてガチガチになるマゾ乳首" : "Getting Up Sensitive Masochist Nipples",
    "大好きな挿入とおしゃぶりを繰り返す欲しがり女子" : "Alternated BJ And Insert",
    "何度イっても終わらない！" : "Endless Orgasm",
    "私のセックスを見てください！" : "Look At Me having SEX! and Jerk Off On My Face!",
    "○○を手懐ける" : "Tame...",
    "いい大人の預かり所" : "Adult Kindergarten",
    "新入社員のお仕事" : "The Task of New Employee",
    "痴漢電車" : "Orgy In The Train",
    "ロリコン専用ソープらんど" : "Lolicon Soapland",
    "蝶が如く" : "Like The Butterflies",
    "僕の彼女が○○だったら" : "If My Girlfirend Is...",
    "社長秘書のお仕事" : "Task of the President's Secretary",
    "極上泡姫物語" : "The Story Of Luxury Spa Lady",
    "ハウツー愛のあるセックスのあり方" : "Popular Japanese Porn Actor Will Tell You: How to Make Love in The Right Way",
    "サマーヌード" : "Summer Nude",
    "カリビアンキューティー" : "Caribbean Cutie",
    "あまえんぼう" : "Sweet Girl",
    "中出しサンタ" : "Creampie Santa Girl",
    "美★ジーンズ" : "Jeans Beauty",
    "アンソロジー" : "Anthology",
    "アナル図鑑" : "Anal Encyclopedia",
    "早抜きBEST" : "Quick Shooting: The Best Of",
    "THE 未公開" : "The Undisclosed",
    "セクシー女優エンサイクロペディア" : "Porn Star Encyclopedia",
    "○○がぼくのお嫁さん" : "My Wife...",
    "クレーム処理のOLにカラダで謝罪してもらいました！" : "Complaint Office Lady Apologize with the Body",
    "〇〇を我慢できたら生中出し" : "Challenge...",
    "AV女優をあなたの自宅に宅配！" : "Sending AV Actress To Your Home",
    "カリビアン・ダイヤモンド" : "Caribbean Diamond",
    "放課後に、仕込んでください" : "Special Lesson After School",
    "童貞狩り" : "Virginity Hunter",
    "着ハメCandy" : "Chaku-hame Candy",
    "恍惚" : "The Ecstasy",
    "ほんとにあったHな話" : "True Erotic Story",
    "中出しいただくまで男の乳首を離しません" : "Licking His Nipples Until Cumshot Inside",
    "いいなり慰み妻" : "Obedient Wife",
    "夫の目の前で妻が" : "In Front of Her Husband",
    "OLの尻に埋もれたい" : "Buried In Her Ass",
    "制服美女倶楽部" : "School Uniform Club",
    "極上セレブ婦人" : "Nicest Celeb Ladies",
    "夏の想い出" : "Summer Memory",
    "大人の日曜劇場" : "Adult Sunday Theater",
    "禁じられた関係" : "Forbidden Correlation",
    "家政婦はシた！" : "The Work Of A Maid",
    "絶潮スプラッシュ" : "Ejaculation Splash",
    "女王のソープ" : "Spa Queen",
    "美微乳" : "Pretty Small Tits",
    "サマーガールズ" : "Summer Girls",
    "巨乳で痴女で絶品ボディの女たち" : "Big Tits Exquisite Body Sluts",
    "女郎蜘蛛" : "Spider Tachibana",
    "令嬢と召使" : "Ladyship And Servant",
    "シェアガール" : "Share Girl",
    "なすがまま" : "The Instinct in...",
    "パシオン・アモローサ ～愛する情熱～" : "Passion And Amorosa",
    "いきなり！ぶっかけ隊。" : "Suddenly Bukkake",
    "見晴らし最高" : "The Best View Of...",
    "清純エンジェル" : "Pure Angel",
    "所持金ゼロ！目指せ○○！ヒッチハイク" : "Hitchhiking",
    "恋オチ" : "Fall In Love",
    "ローションエロダンス" : "Lotion Erotic Dance",
    "パーフェクトボディ" : "Perfect Body",
    "○○の家で撮影しちゃおう" : "Shoot In Her Home...",
    "透けフェチ巨乳" : "Fetishism",
    "僕のペット" : "My Adorable Pet",
    "獄畜" : "Cornered Beast",
    "アナル天使" : "Anal Angel",
    "鬼イキトランス" : "Plunged Into Wild And Crazy Orgy",
    "執事愛撫喫茶" : "Butler Caress Cafe",
    "私の家で" : "At My Home",
    "ふしだらの虜" : "Can't Help Being Dirty",
    "初めてのＡＶ" : "My First Time Porn Filming",
    "激乱交" : "Hard Orgy",
    "密室凌辱" : "Humiliation In Secret Room",
    "性欲処理マゾマスク" : "Masochism Mask",
    "MMG・マジックミラーギロチン" : "Magic Mirror",
    "FICAサッカーカリビアンコムカップ" : "FICA Soccer Caribbeancom Cup",
    "血液型別SEX鑑定" : "Blood Type Interpret",
    "実録投稿" : "True Story",
    "かりのり" : "Karinori",
    "ぶっかけ美熟女" : "Bukkake MILF",
    "ザ・管理人" : "The Manager",
    "団地妻のおもいきッて逆ナン" : "Wives Trying to Pick up",
    "熟女ファイル" : "Mature File",
    "女体観察" : "FBI: Female Body Inspection",
    "カリVR" : "[VR]",
    "竿美人" : "Shemale",
    "鬼のドキュメンタリスト" : "The Demon Documentary",
    "ドリームルームアニメーション" : "Dream Room Animation",
    "縦型動画" : "Vertical Style Video",
    "Debut" : "Debut",
    "One more time, One more fuck" : "One More Time, One More Fuck",
    "BOGA x BOGA" : "BOGA x BOGA",
    "Time Fuck Bandits" : "Time Fuck Bandits",
    "CRB48" : "CRB48"
}

### Required to get legacy connection because server doesnt support "RFC 5746 secure renegotiation"
class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)

def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session

class JAVMetadata:
    file_name = ''
    folder_name = ''
    code = ''
    source = ''
    title = ''
    original_title = ''
    description = ''
    original_description = ''
    release_date = ''
    duration = ''
    studio = ''
    set = ''
    original_set = ''
    actors_string = ''
    trailer = ''
    actors = []
    tags = []
    images = []

    def __init__(self):
        self.file_name = ''
        self.folder_name = ''
        self.code = ''
        self.source = ''
        self.title = ''
        self.original_title = ''
        self.description = ''
        self.original_description = ''
        self.release_date = ''
        self.duration = ''
        self.studio = ''
        self.set = ''
        self.original_set = ''
        self.actors_string = ''
        self.trailer = ''
        self.actors = []
        self.tags = []
        self.images = []

def get_carib_metadata(code):
    logging.info(f'[{count + skipped_count + duplicate_count + 1}] Getting Caribbean metadata for code {code}')
    jav = JAVMetadata
    en_expired = False
    #for some reason, the arrays don't clear when new data is populated
    jav.images.clear()
    jav.tags.clear()
    jav.actors.clear()
    jav.set = ''
    #get urls
    en_url = f'https://en.caribbeancom.com/eng/moviepages/{code}/index.html'
    ja_url = f'https://www.caribbeancom.com/moviepages/{code}/index.html'
    #Get session responses
    en_response = get_legacy_session().get(en_url)
    ja_response = get_legacy_session().get(ja_url)
    #get soup parsers
    en_soup = BeautifulSoup(en_response.content, 'html.parser')
    ja_soup = BeautifulSoup(ja_response.content, 'html.parser')

    #validate title is available in both languages
    if en_soup.find("span", class_="after-link-arrow") is not None:
        if en_soup.find("span", class_="after-link-arrow").text.strip() == "This movie is available for a limited time only. Expiration date: --":
            en_expired = True
            logging.warning("This movie is no longer available in English")
            logging.warning(en_url)
            if ja_soup.find("span", class_="after-link-arrow"):
                logging.warning("This movie is no longer available in Japanese")
                logging.error("Content is not available")
                return jav, False
    if en_expired:
        logging.warning('Using only translated values')

    #get movie info
    en_movie_info = en_soup.find('div', class_='movie-info')
    ja_movie_info = ja_soup.find('div', class_='movie-info')
    #validate urls
    if en_movie_info is None or ja_movie_info is None:
        logging.error('Failed to get movie info')
        return jav, False

    #set code
    jav.code = code
    #set source
    if en_expired:
        jav.source = ja_url
    else:
        jav.source = en_url
    #set studio
    jav.studio = 'Caribbeancom'
    #set set
    if ja_movie_info.findAll('span', class_="spec-content") is not None:
        spec_content = ja_movie_info.findAll('span', class_="spec-content")
        if len(spec_content) >= 3:
            if isinstance(spec_content[3].text, str):
                set = spec_content[3].text.strip()
                if set in set_lookup_dict:
                    jav.set = set_lookup_dict.get(set)

    if en_expired:
        movie_info = ja_movie_info
    else:
        movie_info = en_movie_info
    #set title and original titles
    if movie_info.find('h1', itemprop="name") is not None:
        jav.title = titlecase(movie_info.find('h1', itemprop="name").text.strip())
    if ja_movie_info.find('h1', itemprop="name") is not None:
        jav.original_title = ja_movie_info.find('h1', itemprop="name").text.strip()
    #set descriptions (need to translate later)
    if movie_info.find('p', itemprop="description") is not None:
        jav.description = movie_info.find('p', itemprop="description").text.strip()
    if ja_movie_info.find('p', itemprop="description") is not None:
        jav.original_description = ja_movie_info.find('p', itemprop="description").text.strip()
    #set actor name
    if movie_info.find('span', itemprop="name") is not None:
        jav.actors_string = movie_info.find('span', itemprop="name").text.strip()
        jav.actors = jav.actors_string.split(",")
    #set release date
    if movie_info.find('span', itemprop="datePublished") is not None:
        jav.release_date = movie_info.find('span', itemprop="datePublished").text.strip()
    #set duration
    if movie_info.find('span', itemprop="duration") is not None:
        jav.duration = movie_info.find('span', itemprop="duration").text.strip()
    #set tags
    if movie_info.find_all('a', itemprop='url') is not None:
        for tag in movie_info.find_all('a', itemprop='url'):
            if tag.text in lookup_dict:
                jav.tags.append(lookup_dict.get(tag.text))
            else:
                jav.tags.append(tag.text.capitalize())
    if movie_info.find_all('a', itemprop='genre') is not None:
        for tag in movie_info.find_all('a', itemprop='genre'):
            if tag.text in lookup_dict:
                jav.tags.append(lookup_dict.get(tag.text))
            else:
                jav.tags.append(tag.text.capitalize())

    #set poster
    if ja_soup.find('div', class_='movie-gallery') is not None:
        images_info = ja_soup.find('div', class_='movie-gallery')
        jav.images.append(f'https://caribbeancom.com/moviepages/{code}/images/l_l.jpg')
        #set all other images
        if images_info.find_all('img', itemprop="thumbnail") is not None:
            all_images = images_info.find_all('img', itemprop="thumbnail")
            for i in range(0, len(all_images)-1):
                tag = all_images[i]
                src = list(tag['src'])
                src[30] = 'l'
                img_url = 'https://en.caribbeancom.com' + "".join(src)
                jav.images.append(img_url)

    #set trailer
    jav.trailer = f'https://smovie.caribbeancom.com/sample/movies/{code}/720p.mp4'

    #translate title if set to actor names
    ##this is what carib does for untranslated titles
    translator = Translator()
    if jav.title == jav.actors_string or jav.title == '':
        if jav.original_title != '':
            jav.title = titlecase(translator.translate(jav.original_title, 'en', 'ja').text.strip())
    #translate description if default for untranslated descriptions
    if jav.original_description != '' and jav.description == "Caribbeancom has the widest selection of best looking Japanese and American girls getting fucked hardcore in every hole.The videos are extremely high quality - up to 4000kbps DVD quality, so it lets you jump right into the action and forget that you're just sitting in front of your computer screen!  With over 1000 titles to choose from and new movies updated 6 times a week, where else would you get your hands on fulfilling fantasy of fucking a petite babe with a tight snatch from the Far East?":
        jav.description = translator.translate(jav.original_description).text.strip()
    #Translate items when English content is expired
    if en_expired:
        index = 0
        jav.title = translator.translate(jav.title).text.strip()
        jav.description = translator.translate(jav.description).text.strip()
        for actor in jav.actors:
            jav.actors[index] = titlecase(translator.translate(actor).text.strip())
            index += 1
        index = 0
        for tag in jav.tags:
            jav.tags[index] = translator.translate(tag).text.strip()
            index += 1

    # set filename
    jav.file_name = f'CARIB-{code}'
    #set folder name
    jav.folder_name = f'{"".join([c for c in jav.title if c.isalpha() or c.isdigit() or c==" "]).rstrip()} ({jav.file_name} - {jav.studio} - {jav.actors_string})'
    if len(jav.folder_name):
        jav.folder_name = jav.folder_name[0:254]

    return jav, True

def get_carib_pr_metadata(code):
    code = code.replace("-", "_")
    logging.info(f'[{count + skipped_count + duplicate_count + 1}] Getting Caribbean PR metadata for code {code}')
    jav = JAVMetadata
    # for some reason, the arrays don't clear when new data is populated
    jav.images.clear()
    jav.tags.clear()
    jav.actors.clear()
    # get urls

    en_url = f'https://en.caribbeancompr.com/eng/moviepages/{code}/index.html'
    ja_url = f'https://www.caribbeancompr.com/moviepages/{code}/index.html'
    # Get session responses
    en_response = get_legacy_session().get(en_url)
    ja_response = get_legacy_session().get(ja_url)
    # get soup parsers
    en_soup = BeautifulSoup(en_response.content, 'html.parser')
    ja_soup = BeautifulSoup(ja_response.content, 'html.parser')
    # get movie info
    en_movie_info = en_soup.find('div', class_='movie-info')
    ja_movie_info = ja_soup.find('div', class_='movie-info')

    # set code
    jav.code = code
    # set source
    jav.source = en_url
    # set studio
    jav.studio = 'Caribbeancom Premium'
    # set set and original set
    ##currently cant find a way to grab set because it is only on the ja side and has no itemprop or class
    # set title and original titles
    if en_movie_info.find('h1') is not None:
        jav.title = titlecase(en_movie_info.find('h1').text.strip())
    if ja_movie_info is not None:
        if ja_movie_info.find('h1') is not None:
            jav.original_title = ja_movie_info.find('h1').text.strip()

    # set descriptions (need to translate later)
    if en_movie_info.find('p') is not None:
        jav.description = en_movie_info.find('p').text.strip()
    if ja_movie_info is not None:
        if ja_movie_info.find('p') is not None:
            jav.original_description = ja_movie_info.find('p').text.strip()

    movie_spec = en_soup.findAll(class_='spec-content')
    spec_length = len(movie_spec)
    # set actor name
    if spec_length-1 >= 0:
        jav.actors_string = movie_spec[0].text.strip()
        jav.actors_string = jav.actors_string.replace("\n", ", ")
        jav.actors = jav.actors_string.split(', ')

    # set release date
    if spec_length-1 >= 1:
        jav.release_date = movie_spec[1].text.strip()

    # set duration
    if spec_length-1 >= 2:
        jav.duration = movie_spec[2].text.strip()

    # set tags
    if en_movie_info.find_all('a', class_='spec-item') is not None:
        for tag in en_movie_info.find_all('a', class_='spec-item'):
            if tag.text.strip() not in jav.actors:
                if tag.text.lower() in lookup_dict:
                    jav.tags.append(lookup_dict.get(tag.text.lower()))
                else:
                    jav.tags.append(tag.text.title())

    # set poster
    if en_soup.find('div', class_='movie-gallery') is not None:
        images_info = en_soup.find('div', class_='movie-gallery')
        jav.images.append(f'https://caribbeancompr.com/moviepages/{code}/images/l_l.jpg')
        # set all other images
        if images_info.find_all('img', class_="gallery-image") is not None:
            all_images = images_info.find_all('img', class_="gallery-image")
            for i in range(0, len(all_images)-1):
                tag = all_images[i]
                src = list(tag['src'])
                src[30] = 'l'
                img_url = 'https://en.caribbeancompr.com' + "".join(src)
                jav.images.append(img_url)

    #set trailer
    jav.trailer = f"https://smovie.caribbeancompr.com/sample/movies/{code}/480p.mp4"

    # translate title if set to actor names
    ##this is what carib does for untranslated titles
    translator = Translator()
    if jav.title == jav.actors_string or jav.title == '':
        if jav.original_title != '':
            jav.title = titlecase(translator.translate(jav.original_title, 'en', 'ja').text.strip())
    # translate description if default for untranslated descriptions
    if jav.description == "Caribbeancom has the widest selection of best looking Japanese and American girls getting fucked hardcore in every hole.The videos are extremely high quality - up to 4000kbps DVD quality, so it lets you jump right into the action and forget that you're just sitting in front of your computer screen!  With over 1000 titles to choose from and new movies updated 6 times a week, where else would you get your hands on fulfilling fantasy of fucking a petite babe with a tight snatch from the Far East?":
        jav.description = translator.translate(jav.original_description).text.strip()
    # translate set if needed
    if jav.set == '' and jav.original_set != '':
        jav.set = translator.translate(jav.set).text.strip()
    # set filename
    jav.file_name = f'CARIBPR-{code}'
    # set folder name
    jav.folder_name = f'{"".join([c for c in jav.title if c.isalpha() or c.isdigit() or c==" "]).rstrip()} ({jav.file_name} - {jav.studio} - {jav.actors_string})'
    if len(jav.folder_name):
        jav.folder_name = jav.folder_name[0:254]

    return jav, True

def get_pondo_metadata(code):
    code = code.replace("-", "_")
    logging.info(f'[{count + skipped_count + duplicate_count + 1}] Getting 1Pondo metadata for code {code}')
    jav = JAVMetadata
    # for some reason, the arrays don't clear when new data is populated
    jav.images.clear()
    jav.tags.clear()
    jav.actors.clear()
    # get urls
    en_url = f'https://en.1pondo.tv/movies/{code}/'
    ja_url = f'https://www.1pondo.tv/movies/{code}/'
    #fake javascript (requires chrome installed)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    en_driver = webdriver.Chrome(options=options)
    ja_driver = webdriver.Chrome(options=options)
    en_driver.get(en_url)
    ja_driver.get(ja_url)

    #simulate clicking see more button
    en_see_more = en_driver.find_element(By.CLASS_NAME, "see-more")
    ja_see_more = ja_driver.find_element(By.CLASS_NAME, "see-more")
    en_see_more.click()
    ja_see_more.click()
    # Get HTML
    en_html = en_driver.page_source
    ja_html = ja_driver.page_source
    # get soup parsers
    en_soup = BeautifulSoup(en_html, 'html.parser')
    ja_soup = BeautifulSoup(ja_html, 'html.parser')

    # get movie info
    if en_soup.find('div', id='page') is not None:
        en_movie_info = en_soup.find('div', id='page')
    if ja_soup.find('div', class_='container-main') is not None:
        ja_movie_info = ja_soup.find('div', class_='container-main')

    # set code
    jav.code = code
    # set source
    jav.source = en_url
    # set studio
    jav.studio = '1Pondo'
    # set title and original titles
    if en_movie_info.find('h1', class_='h1--dense') is not None:
        jav.title = titlecase(en_movie_info.find('h1', class_='h1--dense').text.strip())
    if ja_movie_info.find('h1', class_='h1--dense') is not None:
        jav.original_title = ja_movie_info.find('h1', class_='h1--dense').text.strip()

    en_movie_data = en_movie_info.find('div', class_='movie-detail')
    ja_movie_data = ja_movie_info.find('div', class_='movie-detail')
    # set descriptions (need to translate later)
    if en_movie_data.find('p') is not None:
        jav.description = en_movie_data.find('p').text.strip()
    else:
        jav.description = ''
    if ja_movie_data.find('p') is not None:
        jav.original_description = ja_movie_data.find('p').text.strip()


    movie_spec = en_movie_data.findAll(class_='spec-content')
    spec_length = len(movie_spec)
    # set release date
    if spec_length > 0:
        jav.release_date = movie_spec[0].text.strip()

    # set actor name
    if spec_length > 1:
        jav.actors_string = movie_spec[1].text.strip()
        jav.actors_string = jav.actors_string.replace("\n", ", ")
        jav.actors = jav.actors_string.split(', ')

    # set set and original set
    if spec_length > 2:
        second_spec = movie_spec[2].text.strip()
        if len(second_spec) == 8 and second_spec[2] == ':' and second_spec[5] == ":":
            movie_spec.insert(2, "")
        else:
            jav.set = second_spec

    # set duration
    if spec_length > 3:
        jav.duration = movie_spec[3].text.strip()

    tags = en_movie_info.find_all('a', class_='spec__tag')
    # set tags
    if en_movie_info.find_all('a', class_='spec__tag') is not None:
        for tag in en_movie_info.find_all('a', class_='spec__tag'):
            if tag.text.strip() not in jav.actors:
                if tag.text.lower() in lookup_dict:
                    jav.tags.append(lookup_dict.get(tag.text.lower()))
                else:
                    jav.tags.append(tag.text.title())
    # set poster
    jav.images.append(f'https://1pondo.tv/assets/sample/{code}/str.jpg')

    if en_soup.find('div', class_='movie-gallery') is not None:
        images_info = en_soup.find('div', class_='movie-gallery')
        # set all other images
        if images_info.find_all('img', class_="gallery-image") is not None:
            all_images = images_info.find_all('img', class_="gallery-image")
            print(len(all_images)-1)
            for i in range(0, len(all_images)-1):
                tag = all_images[i]
                src = list(tag['src'])
                if 'thum' in "".join(src):
                    jav.images.append(f'https://www.1pondo.tv/assets/sample/{code}/popu/{i + 1}.jpg')
                else:
                    img_url = 'https://1pondo.tv' + "".join(src)
                    img_url = img_url.replace('__@120', '')
                    jav.images.append(img_url)


    # translate title if set to actor names
    ##this is what pondo does for untranslated titles
    translator = Translator()
    if jav.title.replace(",", "") == jav.actors_string.replace(",", ""):
        logging.info('Using Japanese Title Translation')
        jav.title = titlecase(translator.translate(jav.original_title, 'en', 'ja').text.strip())
    # translate description if default for untranslated descriptions
    if jav.description == '':
        logging.info('Using Japanese Description Translation')
        jav.description = translator.translate(jav.original_description).text.strip()
    # translate set if needed
    if jav.set == '' and jav.original_set != '':
        jav.set = translator.translate(jav.set).text.strip()
        # set filename
    jav.file_name = f'1Pondo-{code}'
    # set folder name
    jav.folder_name = f'{"".join([c for c in jav.title if c.isalpha() or c.isdigit() or c==" "]).rstrip()} ({jav.file_name} - {jav.studio} - {jav.actors_string})'
    if len(jav.folder_name):
        jav.folder_name = jav.folder_name[0:254]

    #quit drivers
    en_driver.quit()
    ja_driver.quit()

    return jav, True

def create_NFO(JAVMetadata, directory):
    logging.info(f'Generating NFO for file {JAVMetadata.file_name}')
    indent = '  '
    file_name = f'{JAVMetadata.file_name}.nfo'
    file_path = os.path.join(directory, file_name)
    f = open(file_path, 'w+')
    #add encoding
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
    f.write('\n')
    #add UJavScraper identifier
    f.write(f'<!--created on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - UJAVScraper 0.0.0.2-->')
    f.write('\n')
    #add movie tag
    f.write('<movie>')
    f.write('\n')
    #add title tag
    f.write(indent + create_with_tag('title', JAVMetadata.title))
    f.write('\n')
    #add original title tag
    f.write(indent + create_with_tag('originaltitle', JAVMetadata.original_title))
    f.write('\n')
    #add set tag
    f.write(indent + '<set>')
    f.write('\n')
    f.write(indent + indent + create_with_tag('name', JAVMetadata.set))
    f.write('\n')
    #close set tag
    f.write(indent + '</set>')
    f.write('\n')
    #add plot tag
    f.write(indent + create_with_tag('plot', JAVMetadata.description))
    f.write('\n')
    #add runtime tag
    f.write(indent + create_with_tag('runtime', JAVMetadata.duration))
    f.write('\n')
    #add poster
    if len(JAVMetadata.images)-1 > 1:
        f.write(indent + f'<thumb aspect="poster">{JAVMetadata.images[1]}</thumb>')
        f.write('\n')
    #add fanart
    f.write(indent + '<fanart>')
    f.write('\n')
    if len(JAVMetadata.images)-1 > 0:
        f.write(indent + indent + create_with_tag('thumb', JAVMetadata.images[0]))
        f.write('\n')
    f.write(indent + '</fanart>')
    f.write('\n')
    #add country tag
    f.write(indent + create_with_tag('country', 'Japan'))
    f.write('\n')
    #add premiered tag
    f.write(indent + create_with_tag('premiered', JAVMetadata.release_date))
    f.write('\n')
    #add genre tags
    for tag in JAVMetadata.tags:
        f.write(indent + create_with_tag('genre', tag))
        f.write('\n')
    #add studio
    f.write(indent + create_with_tag('studio', JAVMetadata.studio))
    f.write('\n')
    #add actors
    for actor in JAVMetadata.actors:
        f.write(indent + '<actor>')

        f.write('\n')
        f.write(indent + indent + create_with_tag('name', actor.strip()))
        f.write('\n')
        f.write(indent + indent + create_with_tag('role', actor.strip()))
        f.write('\n')

        profile_url = f"https://sextb.net/actress/{actor.strip().replace(' ', '-')}"
        profile_response = get_legacy_session().get(profile_url)
        profile_soup = BeautifulSoup(profile_response.content, 'html.parser')
        #validate sextb
        if profile_soup.find('img', class_="lazy") is not None:
            tag = profile_soup.find('img', class_="lazy")
            f.write(indent + indent + create_with_tag('thumb', tag['data-src']))
            f.write('\n')
            f.write(indent + indent + create_with_tag('profile', profile_url))
            f.write('\n')
        else:
            logging.warning("sexTB is unavailable")
        f.write(indent + '</actor>')
        f.write('\n')
    #add source tag
    f.write(indent + create_with_tag('source', JAVMetadata.source))
    f.write('\n')

    #close movie tag
    f.write('</movie>')

    f.close()

    #Download images
    if len(JAVMetadata.images) > 0:
        image_session = get_legacy_session().get(JAVMetadata.images[0])
        if image_session.status_code == 200:
            fanart = image_session.content
            a = open(os.path.join(directory, 'fanart.png'), 'wb')
            a.write(fanart)
            a.close()
    if len(JAVMetadata.images) > 1:
        image_session = get_legacy_session().get(JAVMetadata.images[1])
        if image_session.status_code == 200:
            poster = image_session.content
            p = open(os.path.join(directory, 'poster.png'), 'wb')
            p.write(poster)
            p.close()

    new_path = os.path.join(directory, 'fanart')
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    length = len(JAVMetadata.images)
    for i in range (2, length):
        image_session = get_legacy_session().get(JAVMetadata.images[i])
        if image_session.status_code == 200:
            bonus = image_session.content
            b = open(os.path.join(new_path, f'fanart{i}.png'), 'wb')
            b.write(bonus)
            b.close()

    #Download trailer
    if JAVMetadata.trailer != '':

        trailer_name = f"{JAVMetadata.file_name}-trailer"
        r = get_legacy_session().get(JAVMetadata.trailer, stream=True)
        with open(os.path.join(directory, f'{JAVMetadata.file_name}-trailer.mp4'), 'wb') as t:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    t.write(chunk)
        logging.info(f"{trailer_name} downloaded!")
        t.close()

def write_NFO(JAVMetadata, dir_path):
    new_path = os.path.join(dir_path, JAVMetadata.folder_name)

    if os.path.exists(new_path):
        logging.error(f'File Path {new_path} Already Exists. Skipping')
        return False
    else:
        os.mkdir(new_path)

    old_file_path = dir_path + file_name + '.' + extension
    new_file_path = new_path + '/' + JAVMetadata.file_name + '.' + extension

    shutil.move(old_file_path, new_file_path)

    create_NFO(JAVMetadata, new_path)
    logging.info(f'Successfully Created NFO in {new_file_path}')
    logging.info('')

    return True

def create_with_tag(tag, value):
    if value != '':
        return f'<{tag}>{value}</{tag}>'
    else:
        return f'<{tag}/>'

if __name__ == '__main__':
    log = logging.getLogger('')
    log.setLevel(logging.INFO)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    log.addHandler(ch)
    LOGFILE = f'logs/UJAV.log'

    fh = handlers.TimedRotatingFileHandler(LOGFILE, when='M', backupCount=6)
    fh.setFormatter(format)
    log.addHandler(fh)
    logging.info('============================================')
    logging.info(f'     Running UJAV Version 0.0.0.2     ')
    logging.info('============================================')
    logging.info('')

    # directory/folder path
    dir_path = input("Enter Your Directory: ")
    while not os.path.exists((dir_path)):
        logging.warning(f'Directory "{dir_path}" does not exist')
        dir_path = input("Enter Your Directory: ")
    # validate path is complete
    if dir_path[len(dir_path)-1] != '/':
        dir_path += '/'
    count = 0
    skipped_count = 0
    duplicate_count = 0
    logging.info(f'{len(os.listdir(dir_path))} files found')
    # Iterate directory
    for file in os.listdir(dir_path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(dir_path, file)) and not file.startswith('.'):
            # add filename to list
            file_name = os.path.basename(file)
            extension = file_name[-3:]
            file_name = os.path.splitext(file_name)[0].lower()

            ##Check Caribbean
            alias1 = "carib-"
            alias2 = "caribbean-"
            alias3 = "caribbeancom-"
            alias4 = "-carib"
            alias5 = "-caribbean"
            alias6 = "-caribbeancom"
            ##Check Caribbeanpr
            alias7 = "caribpr-"
            alias8 = "caribbeanpr-"
            alias9 = "caribbeancompr-"
            alias10 = "-caribpr"
            alias11 = "-caribbeanpr"
            alias12 = "-caribbeancompr"
            ##Check Pondo
            alias13 = "pondo-"
            alias14 = "1pondo-"
            alias15 = "1pon-"
            alias16 = "-pondo"
            alias17 = "-1pondo"
            alias18 = "-1pon"
            code = ''
            if alias1 in file_name or alias2 in file_name or alias3 in file_name:
                code = file_name[-10:]
                result = get_carib_metadata(code)

                if result[1]:
                    if write_NFO(result[0], dir_path):
                        count += 1
                    else:
                        duplicate_count += 1
                else:
                    skipped_count += 1
                    logging.error(f'Failed to get results for {file_name}')
                logging.info('')

            elif alias4 in file_name or alias5 in file_name or alias6 in file_name:
                code = file_name[:10]
                result = get_carib_metadata(code)

                if result[1]:
                    if write_NFO(result[0], dir_path):
                        count += 1
                    else:
                        duplicate_count += 1
                else:
                    skipped_count += 1
                    logging.error(f'Failed to get results for {file_name}')
                logging.info('')

            elif alias7 in file_name or alias8 in file_name or alias9 in file_name:
                code = file_name[-10:]
                result = get_carib_pr_metadata(code)

                if result[1]:
                    if write_NFO(result[0], dir_path):
                        count += 1
                    else:
                        duplicate_count += 1
                else:
                    skipped_count += 1
                    logging.error(f'Failed to get results for {file_name}')
                logging.info('')

            elif alias10 in file_name or alias11 in file_name or alias12 in file_name:
                code = file_name[:10]
                result = get_carib_pr_metadata(code)

                if result[1]:
                    if write_NFO(result[0], dir_path):
                        count += 1
                    else:
                        duplicate_count += 1
                else:
                    skipped_count += 1
                    logging.error(f'Failed to get results for {file_name}')
                logging.info('')

            elif alias13 in file_name or alias14 in file_name or alias15 in file_name:
                code = file_name[-10:]
                result = get_pondo_metadata(code)

                if result[1]:
                    if write_NFO(result[0], dir_path):
                        count += 1
                    else:
                        duplicate_count += 1
                else:
                    skipped_count += 1
                    logging.error(f'Failed to get results for {file_name}')
                logging.info('')

            elif alias16 in file_name or alias17 in file_name or alias18 in file_name:
                code = file_name[:10]
                result = get_pondo_metadata(code)

                if result[1]:
                    if write_NFO(result[0], dir_path):
                        count += 1
                    else:
                        duplicate_count += 1
                else:
                    skipped_count += 1
                    logging.error(f'Failed to get results for {file_name}')
                logging.info('')
            else:
                logging.error(f'filename - {file_name} is not recognized')
                logging.info('')

    logging.info('============================================')
    logging.info(f'      Successfully scraped {count} title(s)     ')
    logging.info(f'           {duplicate_count} Duplicate title(s)     ')
    logging.info(f'            Skipped {skipped_count} title(s)     ')
    logging.info('============================================')