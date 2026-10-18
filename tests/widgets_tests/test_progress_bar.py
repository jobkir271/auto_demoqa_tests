import allure
from pages.widgets.progress_bar_page import ProgressBarPage


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking progress bar 100%")
@allure.severity(allure.severity_level.NORMAL)
def test_progress_bar(test_progress_bar):
    progress = ProgressBarPage(test_progress_bar)
    progress.click_start()
    progress.wait_for_100_percent()


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking progress bar 50%")
@allure.severity(allure.severity_level.NORMAL)
def test_progress_bar_stop(test_progress_bar):
    progress = ProgressBarPage(test_progress_bar)
    progress.click_start()
    progress.wait_for_at_least_50_percent()
    progress.click_stop()
    progress.check_stopped_value()