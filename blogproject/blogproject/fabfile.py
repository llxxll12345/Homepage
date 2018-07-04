blogproject/fabfile.py

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/llxxll12345/Homepage.git'

env.user = 'llx'
env.password = '11280910'

env.hosts = ['45.76.62.5']

env.port = '22'


def deploy():
    source_folder = '/home/llx/sites/www.llxxll12345.tech/Homepage/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-demo.zmrenwu.com') 
    sudo('service nginx reload')