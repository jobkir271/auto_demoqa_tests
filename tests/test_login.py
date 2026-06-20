from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title("demosite")