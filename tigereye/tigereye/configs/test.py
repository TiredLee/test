from tigereye.configs.default import DefaultConfig


class Testconfig(DefaultConfig):
    TESTING = True
    JSON_SORT_KEYS = False
    SQLALCHEMY_ECHO = False
    # 不写路径 数据在内存中
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
