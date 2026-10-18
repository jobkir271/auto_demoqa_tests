import allure
from pages.elements.upload_and_download_page import UploadDownloadPage


@allure.epic("demoqa_tests")
@allure.feature("Download")
@allure.story("Checking download")
@allure.severity(allure.severity_level.NORMAL)
def test_download(test_download_fix):
    download = UploadDownloadPage(test_download_fix)
    download.download_and_check("sampleFile.jpeg")


@allure.epic("demoqa_tests")
@allure.feature("Upload")
@allure.story("Checking upload")
@allure.severity(allure.severity_level.NORMAL)
def test_upload(test_download_fix):
    upload = UploadDownloadPage(test_download_fix)
    upload.upload_and_check("resources/file_test.txt", "file_test")