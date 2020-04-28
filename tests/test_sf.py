import unittest
import datetime
from services.slots_finder import get_next_n_slots


class TestSlotsFinder(unittest.TestCase):

    def test_slots_finder(self):

        INP_1 = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
                {"start_time": "07:00", "end_time": "07:30"},
                {"start_time": "07:30", "end_time": "08:00"}
            ], [  # Tuesday
            ], [  # Wednesday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
                {"start_time": "07:00", "end_time": "07:30"},
                {"start_time": "07:30", "end_time": "08:00"}
            ], [  # Thursday
                {"start_time": "09:00", "end_time": "09:30"},
                {"start_time": "09:30", "end_time": "10:00"},
                {"start_time": "10:00", "end_time": "10:30"},
                {"start_time": "10:30", "end_time": "11:00"}
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]

        OUT_1 = [
            {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
            {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
            {"start_time": "2017-01-02 07:00:00", "end_time": "2017-01-02 07:30:00"},
            {"start_time": "2017-01-02 07:30:00", "end_time": "2017-01-02 08:00:00"},
            {"start_time": "2017-01-04 06:00:00", "end_time": "2017-01-04 06:30:00"},
            {"start_time": "2017-01-04 06:30:00", "end_time": "2017-01-04 07:00:00"},
            {"start_time": "2017-01-04 07:00:00", "end_time": "2017-01-04 07:30:00"},
            {"start_time": "2017-01-04 07:30:00", "end_time": "2017-01-04 08:00:00"},
            {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 09:30:00"},
            {"start_time": "2017-01-05 09:30:00", "end_time": "2017-01-05 10:00:00"}
        ]

        INP_2 = [
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]

        OUT_2 = []

        INP_3 = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ], [  # Tuesday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "07:00", "end_time": "07:30"},
                {"start_time": "07:30", "end_time": "07:45"}
            ], [  # Wednesday
            ], [  # Thursday
                {"start_time": "09:00", "end_time": "10:00"}
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]

        OUT_3 = [
            {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
            {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
            {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
            {"start_time": "2017-01-03 07:00:00", "end_time": "2017-01-03 07:30:00"},
            {"start_time": "2017-01-03 07:30:00", "end_time": "2017-01-03 07:45:00"},
            {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},
            {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
            {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},
            {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
            {"start_time": "2017-01-10 07:00:00", "end_time": "2017-01-10 07:30:00"}
        ]

        INP_4 = [
            [  # Monday
                {"start_time": "06:00", "end_time": "07:30"}
            ], [  # Tuesday
            ], [  # Wednesday
            ], [  # Thursday
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]

        OUT_4 = [
            {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
            {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
            {"start_time": "2017-01-16 06:00:00", "end_time": "2017-01-16 06:30:00"},
            {"start_time": "2017-01-23 06:00:00", "end_time": "2017-01-23 06:30:00"},
            {"start_time": "2017-01-30 06:00:00", "end_time": "2017-01-30 06:30:00"},
            {"start_time": "2017-02-06 06:00:00", "end_time": "2017-02-06 06:30:00"},
            {"start_time": "2017-02-13 06:00:00", "end_time": "2017-02-13 06:30:00"},
            {"start_time": "2017-02-20 06:00:00", "end_time": "2017-02-20 06:30:00"},
            {"start_time": "2017-02-27 06:00:00", "end_time": "2017-02-27 06:30:00"},
            {"start_time": "2017-03-06 06:00:00", "end_time": "2017-03-06 06:30:00"}
        ]


        SAMPLE_INPUT_OUTPUTS = [
            (INP_1, OUT_1),
            (INP_2, OUT_2),
            (INP_3, OUT_3),
            (INP_4, OUT_4),
        ]

        time_of_run = datetime.datetime(2017, 1, 1, 20, 30)  # Sunday
        for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
            output = get_next_n_slots(ip, time_of_run)
            assert output.sort() == expected_output.sort()


if __name__ == '__main__':
    unittest.main()
