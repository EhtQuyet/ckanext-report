# -*- coding: utf-8 -*-

import ckan.plugins as p

from ckanext.report.blueprint import reports as report_blueprint
import ckanext.report.cli as cli


class MixinPlugin(p.SingletonPlugin):

    p.implements(p.IBlueprint)
    p.implements(p.IClick)

    def get_blueprint(self):
        return [report_blueprint]

    def get_commands(self):
        return cli.get_commands()
