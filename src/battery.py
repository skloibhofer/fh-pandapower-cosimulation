import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

class Battery:
    """A simple battery class."""

    def __init__(
        self, capacity_kWh: float=1000, charge_kWh: float=200, discharge_kWh: float=200, current_kWh: float=0
    ):
        """Create a new battery object with default values.

        Args:
            capacity_kWh, current_kWh (float): Battery capacity and current charge in kWh.
            charge_kWh, discharge_kWh (float): Maximum charge and discharge in a single time step.
                Time step has to be tracked by user.
        """
        self.capacity_kWh = capacity_kWh
        self.charge_kWh   = charge_kWh
        self.discharge_kWh= discharge_kWh
        self.current_kWh  = current_kWh

    @property
    def SoC(self):
        """returns the State of Charge als Wert zwischen [0 - 1]"""
        return self.current_kWh/self.capacity_kWh 

    @property
    def max_charge(self):
        """returns the maximum possible charge to the battery 
        limited by the maximum charging power and the current battery charge 
        for a given hour in [kWh]"""
        return min(self.charge_kWh, self.capacity_kWh-self.current_kWh)

    @property
    def max_discharge(self):
        """returns the maximum possible DIScharge FROM the battery 
        limited by the maximum DIScharging power and the current battery charge 
        for a given hour in [kWh]"""
        return min(self.discharge_kWh, self.current_kWh)

    def charge(self, amount):
        """charges the battery by the maximum possible amount, 
        up to the requested parameter [amount] 
        and RETURNS the actual amount charged (which is <= the [amount] requested)"""
        actual = min(amount, self.max_charge)
        self.current_kWh += actual
        return actual

    def discharge(self, amount):
        """DIScharges the battery by the maximum possible amount, 
        up to the requested parameter [amount] 
        and RETURNS the actual amount charged (which is <= the [amount] requested)"""
        actual = min(amount, self.max_discharge)
        self.current_kWh -= actual
        return actual