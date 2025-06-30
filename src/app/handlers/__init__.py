from aiogram import Dispatcher, Router


from src.app.handlers.start import start_router


def register_routers(dp: Dispatcher):
    main_router = Router()

    main_router.include_router(start_router)



    dp.include_router(main_router)