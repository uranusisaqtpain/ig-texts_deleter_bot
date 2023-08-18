import time
from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from vars import vars
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from webdriver_manager.firefox import GeckoDriverManager
print(Options.arguments)



def retry_action(action, max_attempts=3):
    """Retry an action a few times after an error.

  Args:
    action: The action to retry.
    max_attempts: The maximum number of attempts.

  Returns:
    The result of the action, if it was successful.

  Raises:
    Exception: If the action failed after max_attempts attempts.
  """
    for i in range(max_attempts):
        try:
            return action()
        except Exception as e:
            print(f'Attempt {i + 1}/{max_attempts} failed: {e}')

    raise Exception(f'Action failed after {max_attempts} attempts.')


def delete(text):
    # div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x1v4esvl > section > div > div > div > div.xjp7ctv > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k > div > div > div > div > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xmz0i5r.x6ikm8r.x10wlt62.x1n2onr6 > div > div > div > div > div > div > div: nth - child(
    #     3) > div > div > div > div:has(div.x78zum5.xdt5ytf.x193iq5w.x1n2onr6.xuk3077)
    # text = wait2.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x6prxxf.x1fc57z9.x1yc453h.x126k92a.x14ctfv'))
    # text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
    #                                                   'div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xmz0i5r.x6ikm8r.x10wlt62.x1n2onr6 > div > div > div > div > div > div > div > div > div > div > div:has(div.x78zum5.xdt5ytf.x193iq5w.x1n2onr6.xuk3077)')))
    # EC.element_located_selection_state_to_be(
    #     (By.CSS_SELECTOR, 'div.x6prxxf.x1fc57z9.x1yc453h.x126k92a.x14ctfv'), True)
    driver.execute_script("arguments[0].scrollIntoView();", text)
    actions.move_to_element(text).perform()
    threeDots = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div.x78zum5.x1iyjqo2.xs83m0k.xeuugli.x15zctf7 svg[aria-label="More"]')))
    threeDots.click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[@role=\'menuitem\' and contains(text(), \'Unsend\')]')))
    unsend = driver.find_element(By.XPATH, '//div[@role=\'menuitem\' and contains(text(), \'Unsend\')]')
    unsend.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Unsend']")))
    button = driver.find_element(By.XPATH, "//button[text()='Unsend']")
    button.click()
    wait.until(EC.visibility_of_element_located(text))

    return 'yes'


def scroll():
    previousHeight = driver.execute_script(
        "return document.querySelector('body > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section > div > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div > div > div > div > div >div').scrollHeight;")
    driver.execute_script(
        "const scrollDiv = document.querySelector('body > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section > div > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div > div > div > div > div >div');"
        "scrollDiv.scrollTop = -scrollDiv.clientHeight;")

    try:
        top = driver.find_element(By.CSS_SELECTOR,
                                  'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x1roi4f4.x2b8uid.x1tu3fi.x3x7a5m.x10wh9bi.x1wdrske.x8viiok.x18hxmgj')
        return top
    except NoSuchElementException:
        return previousHeight

        pass


def deleteNode():
    texts_received = driver.find_elements(By.CSS_SELECTOR,
                                          "div > div > div.xjp7ctv > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k > div > div > div > div > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xmz0i5r.x6ikm8r.x10wlt62.x1n2onr6 > div > div > div > div > div > div > div:nth-child(3) > div  div.x78zum5.xdt5ytf.x1n2onr6:has(a.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1rg5ohu.x1a2a7pz)")
    for element in texts_received:
        driver.execute_script("arguments[0].remove();", element)

    date_elements = driver.find_elements(By.CSS_SELECTOR,
                                         'div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x1v4esvl > section > div > div > div > div.xjp7ctv > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k > div > div > div > div > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xmz0i5r.x6ikm8r.x10wlt62.x1n2onr6 > div > div > div > div > div > div > div > div > div[role="row"]:has(div.xzpqnlu.x1hyvwdk.xqtp20y.x6ikm8r.x10wlt62.xnalus7)')
    for element in date_elements:
        driver.execute_script("arguments[0].remove();", element)

    reply_text_elements = driver.find_elements(By.CSS_SELECTOR,
                                               'div.x78zum5.xdt5ytf.x1iyjqo2.xs83m0k.x1xzczws.x6ikm8r.x1rife3k.x1n2onr6.xh8yej3 div.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6:has(div.x78zum5.x1iyjqo2.xs83m0k.xeuugli):has(div.x6prxxf.x1fc57z9.x1yc453h.x126k92a.xzsf02u):has(div[role="button"][aria-label="Double tap to like"].x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xggy1nq.x11njtxf):has(span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.x1fhwpqd.xo1l8bm.x1roi4f4.x1s3etm8.x676frb.x10wh9bi.x1wdrske.x8viiok.x18hxmgj[dir="auto"][style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height: 16px;"])')
    for element in reply_text_elements:
        driver.execute_script("arguments[0].remove();", element)

    reply_text_elements = driver.find_elements(By.CSS_SELECTOR,
                                               'div.x78zum5.xdt5ytf.x1iyjqo2.xs83m0k.x1xzczws.x6ikm8r.x1rife3k.x1n2onr6.xh8yej3 div.x78zum5.xdt5ytf.x1n2onr6:has(a.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1rg5ohu.x1a2a7pz):has(img.x1lliihq.x193iq5w.x5yr21d.xh8yej3):has(h5.x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz )> div >div.x78zum5>div.x78zum5.x1iyjqo2.xs83m0k.xeuugli')
    for element in reply_text_elements:
        driver.execute_script("arguments[0].remove();", element)


if __name__ == '__main__':
    params = vars()
    # options = Options()
    # # options.add_argument("--headless")
    # # # options.add_argument("--remote-debugging-port=9222")
    # options.add_argument('--no-sandbox')
    # # # options.add_argument('--headless=new')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # # # options.add_argument('--disable-blink-features=AutomationControlled')
    # # # options.add_argument('--shm-size=1g')
    # # options.add_argument('--disable-browser-side-navigation')
    # # options.add_argument("--disable-popup-blocking")
    # # options.add_argument("--disable-extensions")
    # # options.add_argument("--disable-notifications")
    # # options.add_argument("--disable-infobars")
    # #
    # # service = Service('/opt/homebrew/bin/chromedriver')
    # service = Service('/opt/homebrew/bin/geckodriver')
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Safari()
    driver.get('https://www.instagram.com')
    usernamefield = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, params.usernamefield)))
    usernamefield.send_keys(params.username, Keys.TAB)
    driver.execute_script("arguments[0].setAttribute('readonly', true)",
                          usernamefield)  # set the readonly attribute to true
    driver.execute_script("arguments[0].setAttribute('disabled', true)", usernamefield)
    wait = WebDriverWait(driver, 10)
    wait2 = WebDriverWait(driver, 2)

    actions = ActionChains(driver)  # Create an ActionChains object

    passwordfield = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, params.passwordfield)))
    passwordfield.send_keys(params.password, Keys.ENTER)
    time.sleep(5)
    driver.get(params.chatbox)
    time.sleep(30)

    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, params.notiButtonSelector)))
    noti = driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9_1')

    noti.click()
    wait.until(EC.invisibility_of_element(noti))
    scrollableDiv = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, params.scrollableDiv)))
    heights = []
    deleteNode()
    while True:

        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, params.loadingIcon)))
        oui = driver.find_elements(By.CSS_SELECTOR,
                                   'div.x6prxxf.x1fc57z9.x1yc453h.x126k92a.x14ctfv')
        deleteNode()

        if len(oui) > 0:
            texts = driver.find_elements(By.CSS_SELECTOR,
                                         'div.x6prxxf.x1fc57z9.x1yc453h.x126k92a.x14ctfv')
            for text in texts:
                try:
                    siryessir = delete(text)
                    print(siryessir)

                except Exception:
                    pass

        else:
            height = scroll()
            heights.append(height)
            deleteNode()
            print(height)

        if heights:

            if isinstance(heights[-1], int):
                print('not lop')
                deleteNode()
            else:
                driver.close()
                break
