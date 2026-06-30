import allure
import pytest
from playwright.sync_api import expect
from pages.alerts_frames_windows.modal_dialogs_page import ModalDialogsPage
@pytest.mark.parametrize("name_button, text_modal, class_button",
[
    ("Small modal","This is a small modal.",".modal-body"),
    ("Large modal","Lorem Ipsum is simply dummy text",".modal-content"),
]
                        )
@allure.epic("demoqa_tests")
@allure.feature("modal_dialogs")
@allure.story("Catching modal dialogs")
@allure.severity(allure.severity_level.NORMAL)
def test_modal_dialogs(browser_windows_page,name_button,text_modal,class_button):
    with allure.step("open tab modal dialogs"):
        modal = ModalDialogsPage(browser_windows_page)
        modal.cheking_modal_dialogs(browser_windows_page,name_button)
    with allure.step("checking text in modal dialogs and close modal dialogs"):
        expect(browser_windows_page.locator(class_button)).to_contain_text(text_modal)
        browser_windows_page.keyboard.press('Escape')

