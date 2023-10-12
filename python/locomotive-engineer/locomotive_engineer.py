"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    (*lista,) = args
    print(lista)
    return lista


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    [first, second, *rest] = each_wagons_id
    (*each_wagons_id,) = *rest, *[first, second]
    uno = each_wagons_id.index(1)
    (*wagons,) = (
        *each_wagons_id[0 : uno + 1],
        *missing_wagons,
        *each_wagons_id[uno + 1 :],
    )
    print(list(wagons))
    return wagons


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops = list(kwargs.values())
    return {**route, "stops": stops}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [[a,b,c],[d,e,f],[g,h,i]] = wagons_rows
    return [[a,d,g],[b,e,h],[c,f,i]]
