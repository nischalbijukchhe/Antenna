from modules.config.models import Config, DnsConfig
from modules.config.constants import CONFIG_TYPES


def get_bool(key):
    if key.lower() == "true" or key.lower() == "1":
        return True
    elif key.lower() == "false" or key.lower() == "0":
        return False


try:
    config_record = Config.objects.all()
    dns_record = DnsConfig.objects.all()
    # 平台域名
    PLATFORM_DOMAIN = config_record.get(name="PLATFORM_DOMAIN").value
    # 服务器外网地址
    SERVER_IP = config_record.get(name="SERVER_IP").value
    # 开放邮箱通知
    OPEN_EMAIL = int(get_bool(config_record.get(name="OPEN_EMAIL").value))
    # 邮箱服务器地址
    EMAIL_HOST = config_record.get(name="EMAIL_HOST_USER").value
    # 邮箱服务器端口
    EMAIL_PORT = int(config_record.get(name="EMAIL_PORT").value)
    # 邮箱账户
    EMAIL_HOST_USER = config_record.get(name="EMAIL_HOST").value
    # 邮箱授权码
    EMAIL_HOST_PASSWORD = config_record.get(name="EMAIL_HOST_PASSWORD").value
    # 隐藏后台地址
    LOGIN_PATH = config_record.get(name="LOGIN_PATH").value
    # 消息七天保存
    SAVE_MESSAGE_SEVEN_DAYS = int(get_bool(config_record.get(name="SAVE_MESSAGE_SEVEN_DAYS").value))
    # 注册方式
    REGISTER_TYPE = int(config_record.get(name="REGISTER_TYPE").value)
    # DNS域名
    dns_domain = dns_record.get(id=1).domain
    DNS_DOMAIN = dns_domain.strip("*.")
    # 端口
    JNDI_PORT = 2345
    HTTPS_PORT = 443
    FTP_PORT = 21
    DNS_PORT = 53

except Exception as e:
    print(e)
    pass


def reload_config(type):
    """根据配置类型选择决定重启哪些配置"""
    config_record = Config.objects.all()
    globals()['PLATFORM_DOMAIN'] = config_record.get(name="PLATFORM_DOMAIN").value
    globals()['SERVER_IP'] = config_record.get(name="SERVER_IP").value
    globals()['LOGIN_PATH'] = config_record.get(name="LOGIN_PATH").value
    globals()['REGISTER_TYPE'] = config_record.get(name="REGISTER_TYPE").value
    globals()['INVITE_TO_REGISTER'] = int(get_bool(config_record.get(name="INVITE_TO_REGISTER").value))
    globals()['EMAIL_HOST'] = config_record.get(name="EMAIL_HOST_USER").value
    globals()['EMAIL_PORT'] = int(config_record.get(name="EMAIL_PORT").value)
    globals()['EMAIL_HOST_USER'] = config_record.get(name="EMAIL_HOST").value
    globals()['EMAIL_HOST_PASSWORD'] = config_record.get(name="EMAIL_HOST_PASSWORD").value
    globals()['SAVE_MESSAGE_SEVEN_DAYS'] = int(config_record.get(name="EMAIL_SAVE_MESSAGE_SEVEN_DAYS").value)
    globals()['OPEN_EMAIL'] = int(get_bool(config_record.get(name="OPEN_EMAIL").value))
