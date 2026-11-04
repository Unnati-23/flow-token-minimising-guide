import unittest
from unittest.mock import Mock

from triage import route


class RoutingTests(unittest.TestCase):
    def test_known_inputs_skip_model(self):
        model = Mock()
        self.assertEqual(route("billing ticket #1234", model),
                         ("billing", "rule"))
        self.assertEqual(route(" ", model), ("review", "rule"))
        self.assertEqual(route("x" * 1001, model), ("review", "rule"))
        model.assert_not_called()

    def test_model_label(self):
        model = Mock(return_value={"label": "technical"})
        self.assertEqual(route("The app closes", model),
                         ("technical", "model"))
        model.assert_called_once_with("The app closes")

    def test_unexpected_label(self):
        self.assertEqual(route("Help", lambda _: {"label": "admin"}),
                         ("review", "fallback"))

    def test_timeout(self):
        model = Mock(side_effect=TimeoutError)
        self.assertEqual(route("Help", model), ("review", "fallback"))


if __name__ == "__main__":
    unittest.main()
