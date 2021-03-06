#!/usr/bin/env python3

import pprint
from database import find_airport
from database import find_runway
from database import find_runway_end

pp = pprint.PrettyPrinter()

include = ["demographic"]

print("#  DPA ###############################")
airport = find_airport("DPA", include=include)
pp.pprint(airport.to_dict(include=include))

print("#  dpa ###############################")
airport = find_airport("dpa", include=include)
pp.pprint(airport.to_dict(include=include))

print("# KDPA ###############################")
airport = find_airport("KDPA", include=include)
pp.pprint(airport.to_dict(include=include))

print("#  3CK ###############################")
airport = find_airport("3CK", include=include)
pp.pprint(airport.to_dict(include=include))

include = ["demographic", "runways"]
print("# LL10 ###############################")
airport = find_airport("LL10", include=include)
pp.pprint(airport.to_dict(include=include))

include = ["additional", "runway_ends"]
print("# LL10 runway 18/36 ##################")
runway = find_runway("18", airport, include=include)
pp.pprint(runway.to_dict(include=include))

include = ["geographic", "lighting"]
print("# LL10 runway 36 #####################")
rwend = find_runway_end("36", runway, include=include)
pp.pprint(rwend.to_dict(include=include))

