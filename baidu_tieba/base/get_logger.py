# 导包
import logging.handlers


# 创建logger类
class GetLogger:

    # 设置类属性log为空
    lg = None

    @classmethod
    # 定义logging方法
    def tb_logging(cls):
        # 判断lg为空
        if cls.lg is None:
            # 生成日志器
            cls.lg = logging.getLogger('admin')
            # 设置日志器级别
            cls.lg.setLevel(level=logging.INFO)
            # 生成处理器
            ti1 = logging.handlers.TimedRotatingFileHandler(filename='../log/tb_logger_info.log',
                                                            when='midnight',
                                                            interval=1,
                                                            backupCount=30,
                                                            encoding='utf-8')
            # 设置处理器级别
            ti1.setLevel(level=logging.INFO)
            # 设置格式器
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] -- %(message)s'
            fm = logging.Formatter(fmt)
            # 为处理器添加格式器
            ti1.setFormatter(fm)
            # 为日志器添加处理器
            cls.lg.addHandler(ti1)
        # 返回日志器
        return cls.lg
