import allure
import pytest
from pages.alerts_frames_windows.alerts_page import AlertsPage

@pytest.mark.smoke
@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching alerts")
@allure.severity(allure.severity_level.NORMAL)
def test_alerts_base(test_alerts):
    alert = AlertsPage(test_alerts)
    alert.alert_processing_base()


@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching alerts delay 5 seconds")
@allure.severity(allure.severity_level.NORMAL)
def test_alerts_delay(test_alerts):
    alert = AlertsPage(test_alerts)
    alert.alert_processing_delay()


@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching confirm")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("action,ok_or_cancel", [("accept", "Ok"), ("dismiss", "Cancel")])
def test_confirm_base(test_alerts, action, ok_or_cancel):
    confirm = AlertsPage(test_alerts)
    confirm.confirm_processing(action)
    confirm.check_confirm_result(ok_or_cancel)


@allure.epic("demoqa_tests")
@allure.feature("alert,confirm,prompt")
@allure.story("Catching confirm")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text", ["1", "Hello", "Привет", "hH2"])
def test_prompt_base(test_alerts, text):
    prompt = AlertsPage(test_alerts)
    prompt.prompt_processing(text)
    prompt.check_prompt_result(text)