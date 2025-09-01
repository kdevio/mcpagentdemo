

# Create a mcp server for the date_helper tool

from mcp.server.fastmcp import FastMCP
import datetime as dt


mcp = FastMCP("date_helper")

MYSTERY_DAYS = 9
MYSTERY_HOURS = 3

@mcp.tool()
def get_mystery_date():
    """Returns the current date + an unknown number of days"""
    current_date = dt.datetime.now()
    current_date += dt.timedelta(days=MYSTERY_DAYS)
    return current_date.strftime("%Y-%m-%d")

@mcp.tool()
def get_mystery_datetime():
    """Returns the current date + an unknown number of days - an unknown number of hours"""
    current_date = dt.datetime.now()
    current_date += dt.timedelta(days=MYSTERY_DAYS, hours=-MYSTERY_HOURS)
    return current_date.strftime("%Y-%m-%d %H:%M:%S.%f")

if __name__ == "__main__":
    mcp.run()
