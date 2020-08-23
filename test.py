import logging
from derw import makeLogger

log = makeLogger(__name__)
log.setLevel(logging.DEBUG)


log.debug("DEBUG")
log.info("INFO")
log.warning("WARNING")
log.critical("CRITICAL")
log.error("ERROR")
