def test_open_login_page(browser):
    browser.get("https://the-internet.herokuapp.com/login")
    assert "Login Page" in browser.page_source
