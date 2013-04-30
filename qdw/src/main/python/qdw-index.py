#!/usr/bin/python
import argparse
import json
import os
import dwfuncts
import logging
import ConfigParser
import pyes

parser = argparse.ArgumentParser(description="Check for changed profiles and re-index them.")
parser.add_argument('--debug', action='store_true', default=False)
args = parser.parse_args()

logger = logging.Logger("qdw")
logger.setLevel(logging.INFO)
log_handler = logging.StreamHandler()
log_handler.setFormatter(logging.Formatter("%(levelname)8s: %(message)s"))
logger.addHandler(log_handler)

config = ConfigParser.ConfigParser()
config.read('/etc/quattor-datawarehouse/dw.conf')

logger.debug("qdw: read config %s" % (config))

dwfuncts.BATCHSIZE = config.getint('dw', 'batchsize') #size of each bulk indexing operation (no.profiles)
dwfuncts.SINGLEINDEXLIMIT = config.getint('dw', 'singleindexlimit') #number of profiles before bulk indexing takes over from single
dwfuncts.INDEX = config.get('dw', 'index')
dwfuncts.TYPE = config.get('dw', 'type')
dwfuncts.ADDRESS = config.get('dw', 'address') #address of elastic search server
dwfuncts.PORT = config.get('dw', 'port')

server = pyes.es.ES(server="%s:%s" % (dwfuncts.ADDRESS, dwfuncts.PORT)) #initialises the conection to elastic search

if args.debug:
    logger.setLevel(logging.DEBUG)

if not os.path.isdir('../Profiles/.git'):
    logger.debug("qdw: Initialising index and populating git repo")
    dwfuncts.indexinstall(logger, server) #inits index and populates
else:
    logger.debug("qdw: Existing index found, updating")
    dwfuncts.updater(logger, server) #updates the index
