# chicago-three
Extend the Code for America's Open 311 wrapper to allow for non Open 311 requests

In Chicago, we have an [Open 311 System](http://dev.cityofchicago.org/docs/api), but it [only supports 13 services](http://dev.cityofchicago.org/docs/api/service_list): 

- Abandoned Vehicles
- Alley Light Out
- Building Violation
- Graffiti Removal
- Pavement Cave-In Survey
- Pothole in Street
- Restaurant Complaint
- Rodent Baiting / Rat Complaint
- Sanitation Code Violation
- Street Cut Complaints
- Street Light Out
- Traffic Signal Out
- Tree Debris

The city provides many, many more services, and programatic access to service requests through web forms: https://servicerequest.cityofchicago.org/web_intake_chic/Controller

The idea of this project is to extend the [Code For America's 311 Python wrapper](https://github.com/codeforamerica/three) to provide a seamless interface to the rest of these 311 service types. Ideally, the user of this library should not need to know whether the service they care about is part of the Open 311.

Describe the service types here:

https://docs.google.com/spreadsheets/d/10XGY4TevLh9Z49-BJ7WowT5aRvrRCguX43KlvC35jBE/edit?usp=sharing



