import click

import ckanext.report.utils as utils


def get_commands():
    return [report]


@click.group()
def report():
    pass


@report.command()
def initdb():
    """Adds simple pages to ckan

    Usage:

        pages initdb
        - Creates the necessary tables in the database
    """
    utils.initdb()
    click.secho(u"DB tables created", fg=u"green")
