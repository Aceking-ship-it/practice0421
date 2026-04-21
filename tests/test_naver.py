from playwright.sync_api import Page
 
def test_naver_search(page: Page):
    page.goto("https://www.naver.com")
    page.fill("input[name='query']", "아이폰")
    page.keyboard.press("Enter")
    assert "search" in page.url or "naver" in page.url
