from pathlib import Path
import datetime

import holidays
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Constants
AT_HOLIDAYS = holidays.AUT()

# Dynamization function coefficients
A4 = -3.92e-10
A3 = 0.00000032
A2 = -0.0000702
A1 = 0.0021
A0 = 1.24


def get_profile_from_file(fp: Path, type: str = "H0") -> pd.DataFrame:
    """From the VDEW profiles xls file, get one sheet.

    Args:
        fp (Path): Path to .xls file.
        type (str): Profile type corresponding to the sheet name in the file.
            Defaults to H0.

    Returns:
        pd.DataFrame: DataFrame with column Multiindex Season
            (Winter, Sommer, Übergangszeit) and Daytype (Samstag, Sonntag, Werktag),
            and Index Time from 0:15 to 24:00 in 15 minute intervals.
    """
    df = pd.read_excel(fp, sheet_name=type, header=[1, 2], index_col=0, nrows=24 * 4)

    return df


def dynamize_day(ser: pd.Series, dayofyear: int) -> pd.Series:
    """Dynamize profile 15 minute series by dayofyear."""
    dynamization_value = (
        np.power(dayofyear, 4) * A4
        + np.power(dayofyear, 3) * A3
        + np.power(dayofyear, 2) * A2
        + dayofyear * A1
        + A0
    )
    return ser * dynamization_value


def load_profile_for_day(
    day: datetime.date, profile_df: pd.DataFrame, dynamize: bool = False
) -> pd.Series:
    """Get the 15 minute load profile for a single day.

    Args:
        day (datetime.date): Date for which to get the load profile.
        profile_df (pd.DataFrame): In the format as given by get_profile_from_file.
        dynamize (bool): Should dynamization by the 4th-grade polynomial dynamization
            function for day of year be applied. This should be only done for H0. Defaults to False.

    Returns:
        pd.Series: Series with Watt values every 15 minutes, and a pd.DatetimeIndex.
    """
    if (day <= datetime.date(day.year, 3, 20)) or (
        day >= datetime.date(day.year, 11, 1)
    ):
        season = "Winter"
    elif (day >= datetime.date(day.year, 5, 15)) and (
        day <= datetime.date(day.year, 9, 14)
    ):
        season = "Sommer"
    else:
        season = "Übergangszeit"

    if (day in AT_HOLIDAYS) or (day.isoweekday == 7):
        weekday = "Sonntag"
    elif (day.isoweekday == 6) or (
        day in [datetime.date(day.year, 12, 24), datetime.date(day.year, 12, 31)]
    ):
        weekday = "Samstag"
    else:
        weekday = "Werktag"

    df = profile_df[season][weekday]

    def combine_day_time(time: datetime.time) -> datetime.datetime:
        """Combine day and time and account for 00:00 being on the next day"""
        dt = datetime.datetime.combine(day, time)
        if time == datetime.time(0, 0):
            dt = dt + datetime.timedelta(days=1)
        return dt

    df.index = df.index.map(combine_day_time)

    if dynamize:
        df = dynamize_day(df, df.index.dayofyear[0])

    return df


def get_load_profile(
    fp: Path, from_: datetime.date | str, to: datetime.date | str, type: str = "H0"
) -> pd.Series:
    """Get a 15 minutes load profiles for given time span.

    Args:
        fp (Path): Path to .xls file.
        from_ (datetime.date | str): Start date.
        to (datetime.date | str): End date.
        type (str): Profile type corresponding to the sheet name in the file.
            Defaults to H0.

    Returns:
        pd.Series: Series with Watt values every 15 minutes between from_ date
            and to date, with a pd.DatetimeIndex.
    """
    profile_df = get_profile_from_file(fp, type)
    dynamize = type == "H0"

    daily_profiles = []
    for day in pd.date_range("2015-01-01", datetime.date(2015, 12, 31), freq="D"):
        daily_profiles.append(load_profile_for_day(day.date(), profile_df, dynamize))

    return pd.concat(daily_profiles, axis="index")
