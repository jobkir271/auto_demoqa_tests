https://jobkir271.github.io/auto_demoqa_tests/

# Auto DemoQA Tests

тесты для demoqa.com на Playwright + pytest.

## Запуск через Docker

docker pull jobkir271/demoqa:latest
docker run --rm jobkir271/demoqa:latest

## Параллельный запуск
docker run --rm jobkir271/demoqa:latest pytest -v -n 4