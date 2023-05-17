import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def handle_option_0():
    amount = input("Digite quantas notícias serão buscadas:\n")
    return get_tech_news(amount)


def handle_option_1():
    title = input("Digite o título:\n")
    return search_by_title(title)


def handle_option_2():
    date = input("Digite a data no formato aaaa-mm-dd:\n")
    return search_by_date(date)


def handle_option_3():
    category = input("Digite a categoria:\n")
    return search_by_category(category)


def handle_option_4():
    return top_5_categories()


def handle_option_5():
    return "Encerrando script\n"


OPTIONS = {
    0: handle_option_0,
    1: handle_option_1,
    2: handle_option_2,
    3: handle_option_3,
    4: handle_option_4,
    5: handle_option_5,
}


def prompt_user_to_select_option() -> int:
    try:
        selected_option = int(
            input(
                "Selecione uma das opções a seguir:\n"
                + " 0 - Popular o banco com notícias;\n"
                + " 1 - Buscar notícias por título;\n"
                + " 2 - Buscar notícias por data;\n"
                + " 3 - Buscar notícias por categoria;\n"
                + " 4 - Listar top 5 categorias;\n"
                + " 5 - Sair.\n"
            )
        )

    except ValueError:
        raise ValueError("Opção inválida\n")
    else:
        if selected_option in OPTIONS:
            return selected_option
        else:
            raise ValueError("Opção inválida\n")


def analyzer_menu():
    try:
        user_input = prompt_user_to_select_option()
        options_return = OPTIONS[user_input]()
        sys.stdout.write(str(options_return))
    except Exception as e:
        sys.stderr.write(str(e))
