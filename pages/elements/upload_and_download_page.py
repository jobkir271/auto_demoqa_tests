import allure
from playwright.sync_api import Page, expect


class UploadDownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.upload_input = page.locator("#uploadFile")
        self.uploaded_file_path = page.locator("#uploadedFilePath")

    @allure.step("Download file and check name: {expected_filename}")
    def download_and_check(self, expected_filename):
        with self.page.expect_download() as download_info:
            self.page.get_by_role("button", name="Download").click()
            download = download_info.value
        assert download.suggested_filename == expected_filename

    @allure.step("Upload file: {file_path}")
    def upload_and_check(self, file_path, expected_text):
        self.upload_input.set_input_files(file_path)
        expect(self.uploaded_file_path).to_contain_text(expected_text)