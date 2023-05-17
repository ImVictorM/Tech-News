from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest import mock
import pytest

MOCK_NEWS = [
    {
        "url": "url",
        "title": "Titulo 1",
        "timestamp": "04/04/2001",
        "writer": "Autor 1",
        "reading_time": 5,
        "summary": "Sumário 1",
        "category": "categoria 1",
    },
    {
        "url": "url",
        "title": "Titulo 1",
        "timestamp": "04/04/2001",
        "writer": "Autor 1",
        "reading_time": 4,
        "summary": "Sumário 1",
        "category": "categoria 1",
    },
    {
        "url": "url",
        "title": "Titulo 1",
        "timestamp": "04/04/2001",
        "writer": "Autor 1",
        "reading_time": 14,
        "summary": "Sumário 1",
        "category": "categoria 1",
    },
]


def test_reading_plan_group_news():
    def test_throws_an_error_when_time_is_negative():
        with pytest.raises(ValueError):
            ReadingPlanService().group_news_for_available_time(-5)

    def test_returns_correct_value():
        with mock.patch(
            "tech_news.analyzer.reading_plan.find_news", return_value=MOCK_NEWS
        ):
            response = ReadingPlanService().group_news_for_available_time(10)
            expect = {
                "readable": [
                    {
                        "chosen_news": [("Titulo 1", 5), ("Titulo 1", 4)],
                        "unfilled_time": 1,
                    }
                ],
                "unreadable": [("Titulo 1", 14)],
            }
            assert response == expect

    test_throws_an_error_when_time_is_negative()
    test_returns_correct_value()
