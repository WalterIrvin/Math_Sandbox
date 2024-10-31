import random
import pandas
import numpy as np
import math
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime
from dateutil.relativedelta import relativedelta


@dataclass
class FinancialData:
    amount: float = None
    interest: float = None
    time_stamp: datetime = None


class InterestCalculator:
    def __init__(self):
        self__financial_records: Dict[datetime.date, FinancialData] = {}
        self.create_range_data(datetime(2024, 9, 1), datetime(2024, 12, 3), 0, 0.08, 0.04)

    def create_range_data(self, start_time: datetime.date, end_time: datetime.date, starting_amount: float,
                          avg_interest: float, interest_fluctuation: float):
        """Creates records that will showcase growth over time, using semi-realistic randomness of interest_rates
        and monthly snapshots.

        Parameters
        ----------
        start_time: datetime.date
            Beginning time of simulation
        end_time: datetime.date
            End time of simulation
        starting_amount: datetime.date
            Amount to begin simulation with
        avg_interest: float
            Nominal interest rate for a given amount
        interest_fluctuation: float
            Amount that interest will flucutate by (0.5, for a 0.8 avg interest means that interest can be
             between 0.3 and 0.13)
        """
        r = relativedelta(end_time, start_time)
        months_difference = (r.years * 12) + r.months
        cur_amount = starting_amount
        for month in range(months_difference):
            new_date = start_time.date() + relativedelta(months=month)
            cur_interest = random.uniform(avg_interest - interest_fluctuation, avg_interest + interest_fluctuation)
            monthly_data = FinancialData(cur_amount, cur_interest, )
        print(months_difference)
	# Test months difference
