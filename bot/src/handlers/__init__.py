from . import start


def setup_routers(dp):
    """
    Конфигурация роутеров

    :param dp: диспетчер
    :return:
    """
    dp.include_router(start.router)
