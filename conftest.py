import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="give url as a parameter"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")