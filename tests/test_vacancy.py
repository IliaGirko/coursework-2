import pytest

from src.vacancy import FilterVacancy, FilterVacancySalary


@pytest.fixture
def data():
    return [
        {
            "Вакансия": "Младший Back-end разработчик",
            "Ссылка на вакансию": "https://hh.ru/vacancy/108444291",
            "Зарплата": {"от": 80000, "до": 100000},
            "name": "Test",
            "Опыт работы": "Нет опыта",
        }
    ]


@pytest.fixture
def data_2():
    return [
        {
            "name": "Test",
            "salary": {"from": 95000, "to": 153000},
            "alternate_url": "https://hh.ru/vacancy/107179024",
            "employer": {"alternate_url": "https://hh.ru/employer/10602050"},
            "experience": {"name": "None"},
        }
    ]


@pytest.fixture
def data_3():
    return [
        {
            "name": "Test",
            "salary": {"from": "100000", "to": 153000},
            "alternate_url": "https://hh.ru/vacancy/107179024",
            "employer": {"alternate_url": "https://hh.ru/employer/10602050"},
            "experience": {"name": "None"},
        }
    ]


@pytest.fixture
def data_4():
    return [
        {
            "name": "Test",
            "salary": {"from": 100000, "to": "153000"},
            "alternate_url": "https://hh.ru/vacancy/107179024",
            "employer": {"alternate_url": "https://hh.ru/employer/10602050"},
            "experience": {"name": "None"},
        }
    ]


@pytest.fixture
def data_5():
    return [
        {
            "name": "Test",
            "alternate_url": "https://hh.ru/vacancy/107179024",
            "employer": {"alternate_url": "https://hh.ru/employer/10602050"},
            "experience": {"name": "None"},
        }
    ]


def test_filter_vacancy(data_2, data_3, data_4, data_5):
    test = FilterVacancy()
    assert test._Vacancy__filter_vacancies("Test", data_2) == [
        {
            "Вакансия": "Test",
            "Зарплата": {"до": 153000, "от": 95000},
            "Опыт работы": "None",
            "Ссылка на вакансию": "https://hh.ru/vacancy/107179024",
        }
    ]
    assert test._Vacancy__filter_vacancies("Test", data_3) == [
        {
            "Вакансия": "Test",
            "Зарплата": {"до": 153000, "от": 0},
            "Опыт работы": "None",
            "Ссылка на вакансию": "https://hh.ru/vacancy/107179024",
        }
    ]
    assert test._Vacancy__filter_vacancies("Test", data_4) == [
        {
            "Вакансия": "Test",
            "Зарплата": {"до": "Максимальный порог не указан", "от": 100000},
            "Опыт работы": "None",
            "Ссылка на вакансию": "https://hh.ru/vacancy/107179024",
        }
    ]
    assert test._Vacancy__filter_vacancies("Test", data_5) == [
        {
            "Вакансия": "Test",
            "Зарплата": {"до": "Зарплата не указана", "от": "Зарплата не указана"},
            "Опыт работы": "None",
            "Ссылка на вакансию": "https://hh.ru/vacancy/107179024",
        }
    ]
    assert test._Vacancy__filter_vacancies("Test", data) == []


def test_filter_vacancy_salary(data):
    test = FilterVacancySalary()
    assert test._VacancySalary__salary_range(data) == [
        {
            "name": "Test",
            "Вакансия": "Младший Back-end разработчик",
            "Ссылка на вакансию": "https://hh.ru/vacancy/108444291",
            "Зарплата": {"от": 80000, "до": 100000},
            "Опыт работы": "Нет опыта",
        }
    ]


def test_filter_vacancy_salary_zero_list():
    test = FilterVacancySalary()
    assert test._VacancySalary__salary_range([{"Зарплата": {"от": "Зарплата не указана"}}], "100") == []
