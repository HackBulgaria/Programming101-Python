import unittest
from batch_bill import BatchBill
from bill import Bill


class TestBatchBill(unittest.TestCase):
    def setUp(self):
        self.bill5 = Bill(5)
        self.bill10 = Bill(10)
        self.batch = BatchBill([self.bill5, self.bill10])

    def test_batchbill_init(self):
        self.assertIn(self.bill5, self.batch)
        self.assertIn(self.bill10, self.batch)

if __name__ == '__main__':
    unittest.main()
