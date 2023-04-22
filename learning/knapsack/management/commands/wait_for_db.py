"""
Django wait for the Database is available.
"""

import time 

from psycopg2 import OperationalError as psycopy2Operror
from django.db.utils import OperationalError

from django.core.management import BaseCommand


class Command(BaseCommand):
    """ Django commands wait for the database"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for the Database")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(psycopy2Operror, OperationalError):
                self.stdout.write("Database is not up.. waiting for the database..")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database Ready..."))

