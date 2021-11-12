"""
Developed by Mohanad Abu-Nayla, Nov-2021.
This work comes without any warrenty of any type, use it at your own risk.
If you find any thing useful, please send me a message/credit me, but you are not required to do so.
"""


import unittest
from helpers import DateUtil as util
import datetime


class DateUtilTest(unittest.TestCase):
    """ Test module for DateUtil helper class """
    def setUp(self) -> None:
        """
        Mocks data for the tests.
        """
        # For test 1
        self.semi_dirty_list = ['asdasd', '2021-11-29 04:19:05', 'asdasd', '2021-12-11 03:19:05']
        self.dirty_list = ['as88dasd', 'aa2021-11-29 04:19:05', 'asdasd', '2aaa02*&###1-12-11 03:19:05']
        self.clean_list = ['2021-11-29 04:19:05', '2021-12-11 03:19:05']

        # For test 2
        self.unordered_list = ['2021-11-30 10:19:05', '2022-01-07 10:19:05', '2021-11-25 03:19:05']
        self.ordered_list = ['2021-11-25 03:19:05', '2021-11-30 10:19:05', '2022-01-07 10:19:05']

        # For Test 3
        self.string_date_list =['2021-12-27 20:22:24']
        self.true_date_object = datetime.datetime

        # For test 4
        self.full_date_list= [datetime.datetime(2021, 12, 24, 14, 22, 24), datetime.datetime(2021, 12, 27, 20, 22, 24)]
        self.truncated_date_list = [datetime.date(2021, 12, 24), datetime.date(2021, 12, 27)]

        # For test 5
        self.lengths = 4

    # Test 1
    def test_clean_list_from_alphabet(self):
        """
        Test the removal of alphabet characters from a stream of date stamps.
        Using clean_list_from_alphabet()
        """
        test_list = util.clean_list_from_alphabet(self.semi_dirty_list)
        self.assertEqual(test_list, self.clean_list)
        test_list = util.clean_list_from_alphabet(self.dirty_list)
        self.assertEqual(test_list, self.clean_list)

    # Test 2
    def test_sort_list_descending(self):
        """
        Test the descending order of time stamps
        Using sort_list_descending()
        """
        test_list = util.sort_list_descending(self.unordered_list)
        self.assertEqual(self.unordered_list, self.ordered_list)

    # Test 3
    def test_parse_list_of_dates(self):
        """
        Test the conversion of string to datetime objects.
        Using parse_list_of_dates()
        """
        dates = util.parse_list_of_dates(self.string_date_list)

        self.assertEqual(type(dates[0]), self.true_date_object)

    # Test 4
    def test_drop_hours_minutes_seconds_microseconds(self):
        """
        Test dropping hours, minutes, seconds, and microseconds from the list of datetime objects
        Using drop_hours_minutes_seconds_microseconds()
        """
        test_list = util.drop_hours_minutes_seconds_microseconds(self.full_date_list)
        self.assertEqual(test_list, self.truncated_date_list)

    # Test 5
    def test_count_logins(self):
        test_dict = util.count_logins(self.truncated_date_list)
        self.assertEqual(test_dict['LENGTHS'][0], self.lengths)


if __name__ == '__main__':
    unittest.main()