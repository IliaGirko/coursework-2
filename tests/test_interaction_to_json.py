import pytest

from src.interaction_to_json_file import WorkToJSON


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


def test_load(data):
    wrj = WorkToJSON()
    assert not wrj.dump_vacancies(data)


def test_del():
    wrj = WorkToJSON()
    assert not wrj.del_vacancy()
