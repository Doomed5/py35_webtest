import logging

def create_log():
    #1.创建日志收集器
    log = logging.getLogger('Doomed')
    #2.设置收集器手机日志等级
    log.setLevel('DEBUG')
    #3.设置日志收集器输出渠道
    #输出到文件
    fh = logging.FileHandler('test.log',encoding='utf-8')
    fh.setLevel('DEBUG')
    log.addHandler(fh)
    #输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel('DEBUG')
    log.addHandler(sh)
    #4.设置日志输出格式
    formats = '%(asctime)s - [%(filename)s -->line:%(lineno)d] -%(levelname)s: %(message)s'
    log_format = logging.Formatter(formats)
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    #返回一个日志收集器
    return log