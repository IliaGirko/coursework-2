from src.interaction_with_api import HeadHunterAPI


def test_one():
    test = HeadHunterAPI()
    assert test.json_list("jhcbjsab") == []
