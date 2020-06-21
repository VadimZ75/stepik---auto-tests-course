import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.implicitly_wait(30)
    rezult = browser.find_element_by_css_selector("#add_to_basket_form")
    assert rezult, "кнопка не найдена"