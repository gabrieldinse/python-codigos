# Author: Gabriel Dinse
# File: pytest_funcarg_example
# Date: 25/05/2019
# Made with PyCharm

# Standard Library

# Third party modules

# Local application imports


def pytest_funcarg__valid_stats(request):
    return StatsList([1,2,2,3,3,4])


def test_mean(valid_stats):
    assert valid_stats.mean() == 2.5


def test_median(valid_stats):
    assert valid_stats.median() == 2.5
    valid_stats.append(4)
    assert valid_stats.median() == 3


def test_mode(valid_stats):
    assert valid_stats.mode() == [2,3]
    valid_stats.remove(2)
    assert valid_stats.mode() == [3]


def main():
    pass


if __name__ == "__main__":
    main()
