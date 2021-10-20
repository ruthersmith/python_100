import datetime as dt
import logging
import sys


class FlightData:
    """
        This class is responsible for structuring the flight data.
    """

    def __init__(self, **kwargs):
        """
        @:kw fly_from -> destination code of the departure location
        @:kw fly_to -> destination code of arrival destination
        @:kw date_from -> search flights from this date (dd/mm/yyyy).
        @:kw date_to -> search flights upto this date (dd/mm/yyyy)
        @:kw nights_in_dst_from -> the minimal length of stay in the destination given in the fly_to parameter
        @:kw nights_in_dst_to -> the maximal length of stay in the destination given in the fly_to parameter.
        @:kw curr -> currency
        @:kw max_stopovers -> max number of stopovers per itinerary. 'max_stopovers=0' for direct flights only.
        """

        # Some default
        today = dt.datetime.now().strftime("%d/%m/%Y")
        six_month_from_today = (dt.datetime.now() + dt.timedelta(days=6*30)).strftime("%d/%m/%Y")
        min_len_of_stay = 7
        max_len_of_stay = 28

        self.fly_from = kwargs.get("fly_from", "BOS")
        self.fly_to = kwargs.get("fly_to")
        self.date_from = kwargs.get("date_from", today)
        self.date_to = kwargs.get("date_to",six_month_from_today)
        self.limit = kwargs.get("limit","3")
        self.nights_in_dst_from = kwargs.get("nights_in_dst_from", min_len_of_stay)
        self.nights_in_dst_to = kwargs.get("nights_in_dst_to",max_len_of_stay)
        self.flight_type = "round"
        self.one_for_city = kwargs.get("one_for_city", 1)
        self.curr = kwargs.get("curr", "usd")
        self.max_stopovers = kwargs.get("max_stopovers", "0")

        if self.fly_to is None:
            message = "fly_to kwarg location is not set exiting program"
            logging.info(message)
            sys.exit(message)