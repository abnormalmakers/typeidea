import os
from datetime import datetime

from fabric.api import (
    env, run, prefix, local, settings,
    roles,
)
from fabric.contrib.files import exists, upload_template
from fabric.decorators import task


env.roledefs = {
    'myserver': ['the5fire@127.0.0.1:11022'],
}
env.PROJECT_NAME = 'typeidea'
env.SETTINGS_BASE = 'typeidea/typeidea/settings/base.py'
env.DEPLOY_PATH = '/home/the5fire/venvs/typeidea-env'
env.VENV_ACTIVATE = os.path.join(env.DEPLOY_PATH, 'bin', 'activate')
env.PYPI_HOST = '127.0.0.1'
env.PYPI_INDEX = 'http://127.0.0.1:8080/simple'
env.PROCESS_COUNT = 2
env.PORT_PREFIX = 909


class _Version:
    origin_record = {}

    def replace(self, f, version):
        with open(f, 'r') as fd:
            origin_content = fd.read()
            content = origin_content.replace('${version}', version)

        with open(f, 'w') as fd:
            fd.write(content)

        self.origin_record[f] = origin_content

    def set(self, file_list, version):
        for f in file_list:
            self.replace(f, version)

    def revert(self):
        for f, content in self.origin_record.items():
            with open(f, 'w') as fd:
                fd.write(content)


@task
def build(version=None):
    """ 本地打包并且上传包到pypi上
        1. 配置版本号
        2. 打包并上传
    """
    if not version:
        version = datetime.now().strftime('%m%d%H%M%S')  # 当前时间，月日时分秒

    _version = _Version()
    _version.set(['setup.py', env.SETTINGS_BASE], version)

    with settings(warn_only=True):
        local('python3 setup.py bdist_wheel upload -r internal')

    _version.revert()
