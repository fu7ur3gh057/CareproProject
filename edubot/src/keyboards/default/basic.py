import aiogram.types

from .constructor import DefaultConstructor


class ButtonFabric(DefaultConstructor):
    @staticmethod
    def _create_schema(button_list: list) -> list[int]:
        if len(button_list) > 1:
            print("")
        a, b = divmod(len(button_list), 2)
        schema = [2] * a + [1] * b
        return schema

    @staticmethod
    def _create_single_schema(button_list: list) -> list[int]:
        return [1 for i in button_list]

    @staticmethod
    def make(
        buttons: list[str],
        schema: list[int] | None = None,
        one_time: bool = True,
        add_skip: bool = False,
        add_back: bool = False,
    ) -> aiogram.types.ReplyKeyboardMarkup:
        if add_back:
            buttons.append("◀️Назад")
        if add_skip:
            buttons.append("▶️Пропустить")
        if not schema:
            schema = ButtonFabric._create_schema(button_list=buttons)
        else:
            schema = ButtonFabric._create_single_schema(button_list=buttons)
        return BasicButtons._create_kb(buttons, schema, one_time_keyboard=one_time)

    # @staticmethod
    # def exam_kb(data: ExaminationStateData, schema: list[int] | None = None):
    #     buttons = []
    #     for item in data.q_a:
    #         numeration = item.numeration
    #         has_answer = data.get_answer_by_question(pk_id=item.pk_id)
    #         text = f"Задание {numeration}"
    #         if has_answer:
    #             text = "✅" + text
    #         buttons.append(text)
    #     buttons.append("Завершить 🏁")
    #     if not schema:
    #         schema = ButtonFabric._create_schema(button_list=buttons)
    #     return BasicButtons._create_kb(buttons, schema, one_time_keyboard=False)


class BasicButtons(DefaultConstructor):
    @staticmethod
    def back() -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["◀️Назад"]
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def cancel() -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["🚫 Отмена"]
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def back_n_cancel() -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1, 1]
        btns = ["◀️Назад", "🚫 Отмена"]
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def confirmation(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = []
        btns = []
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Отмена")
        schema.append(1)
        btns.append("✅Подтвердить")
        if add_back:
            schema.append(1)
            btns.append("◀️Назад")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def skip(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["▶️Пропустить"]
        if add_back:
            schema.append(1)
            btns.append("◀️Назад")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Отмена")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def yes(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["✅Да"]
        if add_back:
            schema.append(1)
            btns.append("◀️Назад")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Отмена")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def no(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["❌Нет"]
        if add_back:
            schema.append(1)
            btns.append("◀️Назад")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Отмена")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def yes_n_no(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [2]
        btns = ["✅Да", "❌Нет"]
        if add_back:
            schema.append(1)
            btns.append("◀️Назад")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Отмена")
        return BasicButtons._create_kb(btns, schema)
