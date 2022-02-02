import unittest
from sig_code_translator import convert_to_english_from_sig
from sig_code_translator import convert_to_sig_from_english


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.test_data = [
            {
                "input": "take 1 daily by mouth for nausea and vomiting at night for pain in left eye",
                "output": "tk 1 d po for nv noct for p in os",
            },
            {
                "input": "take 1 before meals and apply to affected area twice daily",
                "output": "tk 1 ac & aaa bid",
            },
            {
                "input": "take 2 capsule daily in left ear twice daily as needed for anxiety",
                "output": "tk 2 c d in as bid pra",
            },
            {
                "input": "as needed as needed for as needed for anxiety as needed for",
                "output": "prn prf pra prf",
            },
        ]
        super().__init__(*args, **kwargs)

    def test_convert_to_english_from_sig(self):
        # test case and stripping
        self.assertEqual(
            "as needed as needed for as needed for anxiety as needed for",
            convert_to_english_from_sig(" PRN PRF PRA PRF  "),
        )
        for test in self.test_data:
            self.assertEqual(test["input"], convert_to_english_from_sig(test["output"]))

    def test_convert_to_sig_from_english(self):
        self.assertEqual(
            "prn prf pra prf",
            convert_to_sig_from_english(
                " AS NEEDED AS NEEDED FOR AS NEEDED FOR ANXIETY AS NEEDED FOR  "
            ),
        )
        for test in self.test_data:
            self.assertEqual(test["output"], convert_to_sig_from_english(test["input"]))


if __name__ == "__main__":
    unittest.main()
