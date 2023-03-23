import logging

log = logging.getLogger('musen')
log.setLevel('DEBUG')
sh = logging.FileHandler('demo.log')
sh.setLevel('DEBUG')
sh1 = logging.StreamHandler()
sh1.setLevel('DEBUG')
log.addHandler(sh)
log.addHandler(sh1)
log.debug('debug')
