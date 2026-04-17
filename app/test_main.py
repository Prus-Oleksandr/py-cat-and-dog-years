import pytest

from app.main import get_human_age, NegativeAgeError, LargeAgeError


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="zero_zero"),
        pytest.param(14, 14, [0, 0], id="before_first_step"),
        pytest.param(15, 15, [1, 1], id="first_step"),
        pytest.param(23, 23, [1, 1], id="before_second_step"),
        pytest.param(24, 24, [2, 2], id="second_step"),
        pytest.param(27, 27, [2, 2], id="before_third_step"),
        pytest.param(28, 28, [3, 2], id="third_step_transition"),
        pytest.param(29, 29, [3, 3], id="after_third_step"),
    ]
)
def test_different_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_age() -> None:
    with pytest.raises(NegativeAgeError):
        get_human_age(-5, -5)


def test_large_age() -> None:
    with pytest.raises(LargeAgeError):
        get_human_age(555555, 555555)
