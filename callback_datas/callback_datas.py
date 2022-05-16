from aiogram.utils.callback_data import CallbackData

cb_language = CallbackData("language", "language_code", "language_id")
cb_answers = CallbackData("answers", "test", "key")
cb_answers2 = CallbackData("answers2", "test", "key")
cb_test = CallbackData("test", "number")
cb_subject = CallbackData("subject", "subject_id", "test_id", "id")
cb_reset = CallbackData("reset", "test_id")
cb_reset2 = CallbackData("reset2", "test_id")
cb_pagination = CallbackData("pages", "page", "location")
cb_delete_all = CallbackData("delete_all", "page")