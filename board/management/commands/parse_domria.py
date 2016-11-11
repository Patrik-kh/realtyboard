# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
# from django.core.mail import send_mail

from slparser.pars_domria import DomriaSpider


class Command(BaseCommand):

    def handle(self, *args, **options):
        o = DomriaSpider(city=args[0],
                      network_try_limit=3,
                      thread_number=1,
                      depth=30)
        o.run()
        print o.stats