import pytest
import allure
from pages.alerts_frames_windows.modal_dialogs_page import ModalDialogsPage


@pytest.mark.parametrize("name_button, text_modal, class_button", [
    ("Small modal", "This is a small modal.", ".modal-body"),
    ("Large modal", "Lorem Ipsum is simply dummy text", ".modal-content"),
])
@allure.epic("demoqa_tests")
@allure.feature("modal_dialogs")
@allure.story("Catching modal dialogs")
@allure.severity(allure.severity_level.NORMAL)
def test_modal_dialogs(browser_windows_page, name_button, text_modal, class_button):
    modal = ModalDialogsPage(browser_windows_page)
    modal.open_modal_dialogs_tab()
    modal.click_modal_button(name_button)
    modal.check_modal_text_and_close(class_button, text_modal)