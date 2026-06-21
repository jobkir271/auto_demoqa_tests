import allure
import pytest
from playwright.sync_api import Page,expect
from pages.alerts_frames_windows.alerts_page import AlertsPage
from pages.forms_page import AlertsFrameAndWindows
from pages.main_page import MainPage

@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching alerts")
@allure.severity(allure.severity_level.NORMAL)
def test_alerts_base(page: Page):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
    with allure.step("Go to the tab AlertsFrameAndWindows"):
        main.click_alerts_frame_and_windows()
    with allure.step("open Alert tab"):
        form = AlertsFrameAndWindows(page)
        form.click_alerts()
    with allure.step("Calling and processing the alert"):
        alert = AlertsPage(page)
        alert.alert_processing_base()

@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching alerts delay 5 seconds")
@allure.severity(allure.severity_level.NORMAL)
def test_alerts_delay(page: Page):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
    with allure.step("Go to the tab AlertsFrameAndWindows"):
        main.click_alerts_frame_and_windows()
    with allure.step("open Alert tab"):
        form = AlertsFrameAndWindows(page)
        form.click_alerts()
    with allure.step("Calling and processing the alert delay"):
        alert = AlertsPage(page)
        alert.alert_processing_delay()

@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching confirm")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("action,ok_or_cancel", [("accept","Ok"),("dismiss","Cancel")])
def test_confirm_base(page: Page, action: str, ok_or_cancel: str):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
    with allure.step("Go to the tab AlertsFrameAndWindows"):
        main.click_alerts_frame_and_windows()
    with allure.step("open Alert tab"):
        form = AlertsFrameAndWindows(page)
        form.click_alerts()
    with allure.step("Calling and processing the confirm"):
        confirm = AlertsPage(page)
        confirm.confirm_processing(action)
    expect(page.locator("#confirmResult")).to_have_text(f"You selected {ok_or_cancel}")

@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching confirm")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text", ["1","Hello","Привет","hH2"])
def test_prompt_base(page: Page,text: str):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
    with allure.step("Go to the tab AlertsFrameAndWindows"):
        main.click_alerts_frame_and_windows()
    with allure.step("open Alert tab"):
        form = AlertsFrameAndWindows(page)
        form.click_alerts()
    with allure.step("Calling and processing the prompt"):
        prompt = AlertsPage(page)
        prompt.prompt_processing(text)
    with allure.step("expect text"):
        expect(page.locator("#promptResult")).to_have_text(f"You entered {text}")

