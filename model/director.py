from sys import maxsize

class Director:
    def __init__(self, firstname = None, lastname = None, appountmentdate = None, buildingnumber = None, street = None,
                 city = None, region = None, postcode = None, country = None, id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.appointmentdate = appountmentdate
        self.buidingnumber = buildingnumber
        self.street = street
        self.city = city
        self.region = region
        self.postcode = postcode
        self.country = country
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or slef.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize