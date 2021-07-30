""" Guestbook """

import datetime

class Guestbook:
    """ Handle all guestbook operations """
    
    def __init__(self):
        self.signatures = {}

    def add(self, name_to_add: str, date_added: datetime.date):
        """ Add a signature to the book if not already signed """

        if not name_to_add in self.signatures:
            self.signatures.update(
                {name_to_add: date_added}
            )
        else:
            raise RuntimeError(str(name_to_add) + " already signed on " + str(self.signatures[name_to_add]))

    def delete(self, name_to_delete: str):
        """ Delete a signature from the book """

        if name_to_delete in self.signatures:
            self.signatures.pop(name_to_delete)
        else:
            raise RuntimeError(str(name_to_delete) + " is not in the book")

    def update(self, name_to_update: str, date_updated: datetime.date):
        """ Update when a guest signed the book """

        if name_to_update in self.signatures:
            self.signatures.update(
                {name_to_update: date_updated}
            )
        else:
            raise RuntimeError(str(name_to_update) + " is not in the book")
