# models/state.py

from models import storage
from models.city import City

class State(BaseModel, Base):
    # existing code...

    if storage._FileStorage__storage_type == "fs":
        @property
        def cities(self):
            """Returns the list of City objects linked to the current State"""
            from models.city import City
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    else:
        @property
        def cities(self):
            """Returns the list of City objects linked to the current State"""
            cities_list = []
            for city in self.cities:
                cities_list.append(city)
            return cities_list

