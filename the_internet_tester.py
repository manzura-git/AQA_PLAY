from playwright.sync_api import sync_playwright


BASE_URL = "https://the-internet.herokuapp.com/"
TITLE = "the-internet"
TITLE_FORM_AUTH = "Form Authentication"

def navigate_to_example(example_name: str):
    el_form_auth = page.get_by_role("link", name=example_name)
    el_form_auth.click()
    return page.url


with sync_playwright() as drv:
    browser = drv.chromium.launch(headless=False)
    page = browser.new_page()

    # 🌐26x01: Базовый вход на сайт
    page.goto(BASE_URL)
    page.wait_for_timeout(200)
    el_head = page.get_by_role("heading", name="to the-internet")
    el_head_text = el_head.inner_text()
    assert TITLE in el_head_text, \
        f"Заголовок '{el_head_text}' не содержит '{TITLE}'"

    # 🌐26x02: Навигация по ссылкам
    current_url = navigate_to_example(TITLE_FORM_AUTH)
    assert "/login" in current_url, "Не та страница!"
    print(f"✅ Перешли в: Form Authentication | URL: {current_url}")



