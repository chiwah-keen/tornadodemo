#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import traceback
from base import BaseHandler


class MessagesHandler(BaseHandler):

    def post(self):
        try:
            pass
            f = self.get_argument('file', '-')
            print f
        except Exception as e:
            self.log.error(traceback.format_exc())
