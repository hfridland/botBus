import requests
import datetime


def get_bus_info(lat, long):
    params = {
        'apiKey': '3Ct2U9w7g4EihDHM6Jih',
        'Lat': lat,
        'Long': long
    }
    headers = {
        'accept': 'application/JSON'
    }
    response = requests.get('http://api.translink.ca/RTTIAPI/V1/stops',
                            params=params, headers=headers)
    stops = response.json()[:5]
    for stop in stops:
        stop_id = stop['StopNo']
        params = {
            'apiKey': '3Ct2U9w7g4EihDHM6Jih',
        }
        response = requests.get(f"https://api.translink.ca/rttiapi/v1/stops/{stop_id}/estimates",
                                params=params, headers=headers)
        routes = response.json()
        stop['routes'] = routes

    return stops


def bus_info_to_string(bus_unfo):
    s = ''
    for stop in bus_unfo:
        stop_no = stop['StopNo']
        stop_name = stop['Name']
        if len(stop['routes']) > 0:
            s += f"{stop_no} {stop_name}\n"
            for route in stop['routes']:
                route_no = route['RouteNo']
                route_name = route['RouteName']
                route_direction = route['Direction']
                s += f"  {route_no} {route_name} {route_direction}\n    "
                for schedule in route['Schedules']:
                    elt = schedule['ExpectedLeaveTime']
                    # elt = datetime.datetime.strptime(elt, "%I:%M%p %Y-%m-%d").time()
                    # s += f"{elt:%I:%M%p} "
                    s += f"{elt} "
                s += "\n------------------------------------------------\n"

    return s


if __name__ == "__main__":
    s = bus_info_to_string(get_bus_info(49.2227, -122.6940))
    print(s)