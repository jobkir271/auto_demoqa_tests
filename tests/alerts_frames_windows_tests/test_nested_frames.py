import allure
from pages.alerts_frames_windows.nested_frames_page import NestedFramesPage


@allure.epic("demoqa_tests")
@allure.feature("nested frames")
@allure.story("Catching text in nested frames")
@allure.severity(allure.severity_level.NORMAL)
def test_nested_frames(browser_windows_page):
    nested = NestedFramesPage(browser_windows_page)
    nested.open_nested_frames_tab()
    nested.check_parent_frame_text()
    nested.check_child_frame_text()