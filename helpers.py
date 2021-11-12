"""
Developed by Mohanad Abu-Nayla, Nov-2021.
This work comes without any warrenty of any type, use it at your own risk.
If you find any thing useful, please send me a message/credit me, but you are not required to do so.
"""

import re
from tqdm import tqdm
import ciso8601
import datetime


class DateUtil:
    """
    Helper class for dates cleaning, conversion and validation.
    """
    @staticmethod
    def clean_list_from_alphabet(dirty_list):
        """
        remove alphabet characters from time stamps
        Expected Input: ['asdasd', '2021-12-24 14:22:24', '2021-12-27 20:22:24', 'asdasd']
        Expected Output: ['2021-12-24 14:22:24', '2021-12-27 20:22:24']
        """
        new_list = []
        for i in tqdm(dirty_list):
            if not i.isalnum():
                # regex expression includes digits, a dash symbol (-), a colon (:) and a space.
                new_list.append(re.sub('[^0-9-: ]', '', i))
        return new_list

    @staticmethod
    def sort_list_descending(unsorted_list):
        """
        sorts the list of dates in descending order
        Expected Input: ['2021-12-27 14:22:24', '2021-12-24 20:22:24']
        Expected Output: ['2021-12-24 14:22:24', '2021-12-27 20:22:24']
        """
        unsorted_list.sort(reverse=False)
        return unsorted_list

    @staticmethod
    def parse_list_of_dates(list_of_dates):
        """
        parses the list of dates into a list of datetime objects
        Expected Input: ['2021-12-24 14:22:24', '2021-12-27 20:22:24']
        Expected Output: [datetime.datetime(2021, 12, 24, 14, 22, 24), datetime.datetime(2021, 12, 27, 20, 22, 24)]
        """
        list_of_datetime = []
        for i in tqdm(list_of_dates):
            try:
                list_of_datetime.append(ciso8601.parse_datetime(i))
            except ValueError as error:
                print(error)
                print('the parse_list_of_dates() was not executed')

        return list_of_datetime

    @staticmethod
    def drop_hours_minutes_seconds_microseconds(list_of_datetime):
        """
        drops hours, minutes, seconds, and microseconds from the list of datetime objects
        Expected Input: [datetime.datetime(2021, 12, 24, 14, 22, 24), datetime.datetime(2021, 12, 27, 20, 22, 24)]
        Expected Output: [datetime.datetime(2021, 12, 24), datetime.datetime(2021, 12, 27)]
        """
        new_list = []
        print("Step 4: drop hours, minutes, seconds, and microseconds from the list of datetime objects")
        for i in tqdm(list_of_datetime):
            new_list.append(datetime.date(i.year, i.month, i.day))
        return new_list

    @staticmethod
    def count_logins(formatted_date_list):
        """
        Count the longest period of consecutive logins occur per time-stamp(s).
        Expected Input: ['2021-12-24, '2021-12-27']
        Expected Output: '4'
        :param formatted_date_list:
        :return: dictionary of timestamps and login counts i.e. LENGTHS
        """
        logins_dict = {'START': [], 'END': [], 'LENGTHS': []}
        for i in range(len(formatted_date_list)):
            if i + 1 < len(formatted_date_list):
                logins_dict['START'].append(str(formatted_date_list[i]))
                logins_dict['END'].append(str(formatted_date_list[i + 1]))
                logins_dict['LENGTHS'].append(1 + int((formatted_date_list[i + 1] - formatted_date_list[i]).days))
        return logins_dict