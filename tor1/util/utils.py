import logging
from util import dbmemcache

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s-%(levelname)s-%(filename)s-%(lineno)d]%(message)s')
logger = logging.getLogger(__name__)


def setMem(key, values, time=3600):
    try:
        dbmemcache.mc.set(key, values, time=time)
    except Exception as e:
        logger.error(e)

def setMemReplace(key, values):
    try:
        dbmemcache.mc.replace(key, values)
    except Exception as e:
        logger.error(e)


def getMem(key):
    try:
        return dbmemcache.mc.get(key)
    except Exception as e:
        logger.error(e)
