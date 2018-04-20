from zulip_bots.test_lib import BotTestCase

class TestHelpBot(BotTestCase):
    bot_name = "prepsetup"  # type: str

    def test_bot(self) -> None:
        dialog = [
            ('', 'beep boop'),
            ('help', 'beep boop'),
            ('foo', 'beep boop'),
        ]

        self.verify_dialog(dialog)
