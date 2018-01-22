from tigereye.configs.default import DefaultConfig


class ProductionConfig(DefaultConfig):
    DEBUG = False
    JSON_SORT_KEYS = False
    JSON_PERTTYPRINT_REGULAR = False
    SQLALCHEMY_ECHO = True

    EMAIL_HOST = 'smtp.163.com'
    # EMAIL_PORT = 465
    EMAIL_HOST_USER = SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'm15506590756@163.com'
    EMAIL_HOST_PASSWORD = 'abc123456'
    EMAIL_USE_SSL = True
    ADMINS = ['m15506590756@163.com']




