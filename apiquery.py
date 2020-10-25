import requests
import json
overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
/*
This shows the cycleway and cycleroute network.
*/

[out:json];

(
  // get cycle route relations
  relation[route=bicycle](51.33533076546221,-2.7029800415039062,51.60650393311422,-2.4619674682617188);
  // get cycleways
  way[highway=cycleway](51.33533076546221,-2.7029800415039062,51.60650393311422,-2.4619674682617188);
  way[highway=path][bicycle=designated](51.33533076546221,-2.7029800415039062,51.60650393311422,-2.4619674682617188);
);

out body;
>;
out skel qt;
"""
response = requests.get(overpass_url,
                        params={'data': overpass_query})
data = response.json()
