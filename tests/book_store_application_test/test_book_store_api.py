import allure
import requests

BASE_URL = "https://demoqa.com"

@allure.epic("demoqa_tests")
@allure.feature("book_store_api")
@allure.story("checking get all books")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_books():
    with allure.step("Send GET request to /BookStore/v1/Books"):
        response = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    with allure.step("Check status code is 200"):
        assert response.status_code == 200
    with allure.step("Check that books list is not empty"):
        data = response.json()
        assert len(data["books"]) > 0
        print(f"Книг в магазине:{len(data['books'])}")

@allure.epic("demoqa_tests")
@allure.feature("book_store_api")
@allure.story("checking get all books")
@allure.severity(allure.severity_level.NORMAL)
def test_get_book_by_isbn():
    isbn = "9781449325862"
    with allure.step(f"Send GET request to /BookStore/v1/Book with ISBN={isbn}"):
        response = requests.get(f"{BASE_URL}/BookStore/v1/Book/", params={"ISBN": isbn})
    with allure.step("Check status code is 200"):
        assert response.status_code == 200
    with allure.step("Check that returned ISBN matches requested"):
        data = response.json()
        assert data["isbn"] == isbn
        print(f"Название книги: {data['title']}")

# def test_get_book():
#     response = requests.get(f"{BASE_URL}/BookStore/v1/Books")
#     data = response.json()
#     for book in data["books"]:
#         print(book["isbn"])


