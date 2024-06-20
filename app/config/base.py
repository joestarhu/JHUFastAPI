from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """FastAPI的配置信息
    """

    model_config = ConfigDict(
        # 环境变量文件
        env_file=".env",
        # 环境变量参数读取策略[ignore:忽略]
        extra="ignore"
    )

    """
    FastAPI自身的配置
    """
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    title: str = "JHUTemplateFastAPI"
    version: str = "1.0.0"

    """
    CORS配置
    """
    allow_origins: list[str] = ["*"]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]

    """
    安全相关
    """
    # 账号的默认密码
    default_passwd: str = "default_passwd"
    # 对称加密用的key
    encrypt_key: str = "encrypt_key"
    # hash加密用的key
    hash_key: str = "hash_key"
    # JWT加密用的Key
    jwt_key: str = "jwt_key"
    # Jwt的默认过期时间(min)
    jwt_expire_min: int = 60*24

    # 钉钉的ak和sk
    dingtalk_ak: str = "dingtalk_ak"
    dingtalk_sk: str = "dingtalk_sk"

    """
    数据库存储相关
    """
    # SqlAlchemy 关系型数据库的连接字符串,比如mysql
    db_rds: str = "mysql+pymysql://username:passwd@host:port/database"
    # SqlAlchemy pool的重开时长
    pool_recycle_seconds: int = 3600

    @property
    def fastapi_kwargs(self) -> dict:
        return dict(
            docs_url=self.docs_url,
            redoc_url=self.redoc_url,
            title=self.title,
            version=self.version
        )

    @property
    def fastapi_cors_kwargs(self) -> dict:
        return dict(
            allow_origins=self.allow_origins,
            allow_credentials=self.allow_credentials,
            allow_methods=self.allow_methods,
            allow_headers=self.allow_headers
        )


settings = AppSettings()
