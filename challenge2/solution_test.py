import unittest, json

from solution import print_transfers


class TestPrintTransfers(unittest.TestCase):

    def test_print_transfers(self):
        transaction_hash = '0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263'
        result = print_transfers(transaction_hash)

        expected_result = [
        {
            "from": "0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD",
            "to": "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc",
            "amount":49999900000000000 ,
        },
        {
            "from": "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc",
            "to": "0x7c0b8a9716a00F8D13514c50e1282947DDA5C395",
            "amount":82212970 ,
        },
        ]


        self.assertEqual(json.loads(result), expected_result)
        



if __name__ == "__main__":
    unittest.main()