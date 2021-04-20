# Если что-то не запускаеться, сделай: "pip install requirements.txt"

from time import sleep


def test_item(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    sleep(30)
    button = browser.find_elements_by_css_selector('#add_to_basket_form [data-loading-text]')
    assert len(button) > 0, "Похоже, что кнопки нет"
