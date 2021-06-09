import logging
import logging.handlers

def set_log_config():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    ls = logging.StreamHandler()
    lf = logging.handlers.TimedRotatingFileHandler(filename="./log/setting.log", when="d", backupCount=5, encoding='utf-8')

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)

    ls.setFormatter(formatter)
    lf.setFormatter(formatter)

    logger.addHandler(ls)
    logger.addHandler(lf)

