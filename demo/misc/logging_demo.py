import logging
from logging import handlers

logging.basicConfig(
    format = "[%(asctime)s] %(levelname)-8s %(message)s"
)

log=logging

log.info('this is info')
log.debug('this is info')
log.warn('this is warn')
log.warning('this is warn')
log.critical('this is info')
log.fatal('this is info')
log.error('this is info')
log.exception('this is info')
log.log('this is info')



log2 = logging.getLogger()
#handler = logging.StreamHandler(stream=sys.stdout) 
handler = handlers.TimedRotatingFileHandler(filename="./mylog.log",
	when="D",
	interval=1)
fmt = logging.Formatter('%(asctime)s|%(message)s', '%Y-%m-%d %H:%M:%S')
handler.setFormatter(fmt)
log2.addHandler(handler)
log2.setLevel(logging.DEBUG)
log2.info("what you want to do")



# 输出到标准输出
import sys
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout  
)
logger = logging.getLogger(__name__)
logger.info("xxxx")

