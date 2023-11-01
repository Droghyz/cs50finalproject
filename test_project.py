import project
import pytest

def main():
   test_check_name()
   test_is_date_valid()
   test_negative_days()

def test_check_name():
    assert project.check_name("Marco,Di Fatta") == ("Marco", "Di Fatta")
    assert project.check_name("Marco,Rinaudo") == ("Marco", "Rinaudo")

def test_is_date_valid():
    with pytest.raises(ValueError):
        project.is_date_valid([2023, 30, 10], [2023, 10, 10])
        project.is_date_valid([2023, 10, 10], [2023, 40, 10])


def test_negative_days():
    with pytest.raises(ValueError):
        project.negative_days(0)
        project.negative_days(-1)


if __name__ == "__main__":
    main()