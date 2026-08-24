import allure

from playwright.sync_api import expect, Page


@allure.epic("demoqa_tests")
@allure.feature("Download")
@allure.story("Checking download")
@allure.severity(allure.severity_level.NORMAL)
def test_download(test_download_fix: Page):
    with allure.step("Open upload and download page"):
        page = test_download_fix
    with allure.step("Download file"):
        with page.expect_download() as download_info:
            page.get_by_role("button", name ="Download").click()
            download = download_info.value
    with allure.step("Checking download file"):
        assert download.suggested_filename == "sampleFile.jpeg"
@allure.epic("demoqa_tests")
@allure.feature("Upload")
@allure.story("Checking upload")
@allure.severity(allure.severity_level.NORMAL)
def test_upload(test_download_fix:Page):
    with allure.step("Open upload and download page"):
        page = test_download_fix
    with allure.step("Upload file"):
        page.set_input_files("#uploadFile","resources/file_test.txt")
    with allure.step("Checking upload file"):
        expect(page.locator("#uploadedFilePath")).to_contain_text("file_test")

