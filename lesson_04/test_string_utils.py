import pytest
from StringUtils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

# Тесты для метода capitilize
def test_capitilize(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("hello world") == "Hello world"
    assert string_utils.capitilize("") == ""

# Тесты для метода trim
def test_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro   ") == "skypro   "
    assert string_utils.trim("   skypro   ") == "skypro   "
    assert string_utils.trim("") == ""

# Тесты для метода to_list
def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("") == []
    assert string_utils.to_list("one,two,three", "|") == ["one,two,three"]

# Тесты для метода contains
def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("SkyPro", "") is True  # Пустая строка считается присутствующей

# Тесты для метода delete_symbol
def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "x") == "SkyPro"  # Символ не найден
    assert string_utils.delete_symbol("", "a") == ""  # Пустая строка

# Тесты для метода starts_with
def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "P") is False

# Тесты для метода end_with
def test_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "y") is False

# Тесты для метода is_empty
def test_is_empty(string_utils):
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True
    assert string_utils.is_empty("SkyPro") is False

# Тесты для метода list_to_string
def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string([]) == ""  # Пустой список

if __name__ == '__main__':
    pytest.main()
