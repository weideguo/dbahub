#coding:utf8

"""
django 命令
python manage.py <command> --help

文件放在目录，每一个文件对应一个命令
my_model/management/commands

在sttings.py文件的INSTALLED_APPS中添加模块名my_model
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "encrypt/decrypt data use Mirage ~"

    def add_arguments(self, parser):
        #命令行参数
        parser.add_argument("--app", type=str, required=True)
        parser.add_argument("--model", type=str, required=False)
        

    def handle(self, *args, **options):
        #实际执行
        app = options['app']
        model = options['model']
        print(args)
        print(options)