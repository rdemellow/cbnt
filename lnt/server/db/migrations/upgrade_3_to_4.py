# Version 4 of the database adds the bigger_is_better column to StatusField.

from sqlalchemy import Column, Integer

from lnt.server.db.migrations.util import introspect_table, add_column


def upgrade(engine, _):
    bigger_is_better = Column('bigger_is_better', Integer, default=0)
    test_suite_sample_fields = introspect_table(engine,
                                                'TestSuiteSampleFields')
    add_column(engine, test_suite_sample_fields, bigger_is_better)
    test_suite_sample_fields_cv = introspect_table(engine,
                                                'TestSuiteCVSampleFields')
    add_column(engine, test_suite_sample_fields_cv, bigger_is_better)
