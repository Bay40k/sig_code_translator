import unittest
from sig_code_translator import from_sig
from sig_code_translator import to_sig


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.test_data = [
            {
                "input": "take 1 tablet by mouth every day as needed for pain",
                "output": "tk 1 t po qd prn p",
            },
            {
                "input": "take 1 before meals and apply to affected area twice daily",
                "output": "tk 1 ac and aaa bid",
            },
            {
                "input": "take 2 capsule daily in left ear twice daily as needed for anxiety",
                "output": "tk 2 c d in as bid pra",
            },
            {
                "input": "as needed as needed for anxiety as needed for anxiety as needed as needed for anxiety",
                "output": "prn pra pra prn pra",
            },
        ]
        super().__init__(*args, **kwargs)

    def test_from_sig(self):
        # test case and stripping
        self.assertEqual(
            "AS NEEDED AS NEEDED FOR ANXIETY AS NEEDED FOR ANXIETY AS NEEDED AS NEEDED FOR ANXIETY",
            from_sig(" prn Pra pRa prn pra  "),
        )
        for test in self.test_data:
            self.assertEqual(test["input"].upper(), from_sig(test["output"]))

    def test_to_sig(self):
        self.assertEqual(
            "PRN PRA PRA PRN PRA",
            to_sig(
                " as needed as neeDed for anXiety as neEded for anxiety as needed as needed for anxiety  "
            ),
        )
        for test in self.test_data:
            self.assertEqual(test["output"].upper(), to_sig(test["input"]))


if __name__ == "__main__":
    unittest.main()
