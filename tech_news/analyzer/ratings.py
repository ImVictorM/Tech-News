from tech_news.database import db
from collections import Counter


def top_5_categories():
    news_from_db = list(db.news.find({}, {"_id": False, "category": True}))

    categories_list = [element["category"] for element in news_from_db]

    categories_count = Counter(categories_list)

    top_5_categories = [
        category
        for category, _category_count in categories_count.most_common(5)
    ]

    top_5_sorted = sorted(
        top_5_categories,
        key=lambda category: (-categories_count[category], category),
    )

    return top_5_sorted
