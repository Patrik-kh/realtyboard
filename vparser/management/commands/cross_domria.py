﻿# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from time import time
# from board.models import *
# from django.db.models.loading import get_model
from vparser.parser_for_all_cities_dom_ria import *
from vparser.utils import *
import urllib2

#example: manage.py port_terminal
class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--test',
                    action='store_true',
                    # dest='proxy_fine',
                    default=False,
                    help='parser domria '),
        make_option('--city',
                    action='store_true',
                    # dest='proxy_fine',
                    default=False,
                    help='parser domria '),
    )

    def handle(self, *args, **options):
        t1 = time()
        # if options.get('domria'):
        #     site = SiteStructureParser(thread_number=int(args[0]))
        #     site.run()
        #     self.stdout.write(u'domria was here')
        if options.get('test'):
            test_domria()
        if options.get('city'):
            self.stdout.write( u'running multithreading')
            site = SiteStructureParser( city_pars=args[0], thread_number=int(args[1]), service_proxy=args[2])
            site.run()
            print 'count of thread = ', args[0]
            self.stdout.write(str(args[0])+u' have been worked.')
        

        print "Total time %s" % (time() - t1)
        self.stdout.write('Successfully import data')