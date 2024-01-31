import unittest
from deliveryfeeapi.views import DeliveryFeeView

# Create your tests here.
class TestDeliveryFeeView(unittest.TestCase):

    def setUp(self):
        self.delivery_fee_calculator = DeliveryFeeView()

    def test_calculate_delivery_fee(self):
        cart_value = 790
        delivery_distance = 2235
        number_of_items = 4
        time = "2024-01-15T13:00:00Z"
        
        if 'Z' in time:
            time = time.rstrip('Z')

        expected_fee = self.delivery_fee_calculator.calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time)

        self.assertEqual(expected_fee, 710)

if __name__ == '__main__':
    unittest.main()
