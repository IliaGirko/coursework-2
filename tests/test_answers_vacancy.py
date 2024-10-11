import pytest

from src.answers_vacancy import answer


@pytest.fixture
def data():
    return [
        {
            "Вакансия": "Младший Back-end разработчик",
            "Ссылка на вакансию": "https://hh.ru/vacancy/108444291",
            "Зарплата": {"от": 80000, "до": 100000},
            "Опыт работы": "Нет опыта",
        }
    ]


def test_answer():
    assert answer(data, 5) == []
