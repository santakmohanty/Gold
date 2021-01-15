import logging
import sys
import traceback

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_mixins import ActiveRecordMixin, ReprMixin

from gold import settings

Base = declarative_base()

# SQLALCHEMY_URL = "postgresql+psycopg2://archita:archita@localhost/mycandidature"

DATABASE_NAME = settings.DATABASES['default']['NAME']
DB_USERNAME = settings.DATABASES['default']['USER']
DB_PASSWORD = settings.DATABASES['default']['PASSWORD']
DB_HOST = settings.DATABASES['default']['HOST']

SQLALCHEMY_URL = "postgresql+psycopg2://" + DB_USERNAME + ":" + DB_PASSWORD + '@' + DB_HOST + '/' + DATABASE_NAME

engine = create_engine(SQLALCHEMY_URL, pool_size=125, max_overflow=150, pool_pre_ping=True)
session = scoped_session(sessionmaker(bind=engine, autocommit=True))

Base.metadata.create_all(engine)


def log(msg):
    print('\n{}\n'.format(msg))


# Used SQLAlchemy Mixin
# we also use ReprMixin which is optional
class BaseModel(Base, ActiveRecordMixin, ReprMixin):
    __abstract__ = True
    __repr__ = ReprMixin.__repr__
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


    @classmethod
    def log_stack_trace(cls, error):
        trace = traceback.extract_tb(sys.exc_info()[2])
        # Add the event to the log
        output = "Error in the server: %s.\n" % (error)
        output += "\tTraceback is:\n"
        for (file, linenumber, affected, line) in trace:
            output += "\t> Error at function %s\n" % (affected)
            output += "\t  At: %s:%s\n" % (file, linenumber)
            output += "\t  Source: %s\n" % (line)
        output += "\t> Exception: %s\n" % (error)
        cls.logger.info('Exception Stack Trace')
        cls.logger.info(output)
        cls.logger.info('=========END=========')


BaseModel.set_session(session)
