import allure
from pages.alerts_frames_windows.frames_page import FramesPage


@allure.epic("demoqa_tests")
@allure.feature("frames")
@allure.story("Catching frames")
@allure.severity(allure.severity_level.NORMAL)
def test_frames(browser_windows_page):
    frames = FramesPage(browser_windows_page)
    frames.open_frames_tab()
    frames.check_frame1_text()
    frames.check_frame2_text()