from fabric.api import *
from contextlib import nested 
from fabric.context_managers import *


env.roledefs = {
    'test' : ['localhost']
    }

def activate():
#    with prefix('WORKON_HOME=$HOME/.virtualenvs'):
#        with prefix('source /usr/bin/virtualenvwrapper.sh'):
    with nested(cd('home/aregee/workspace/sugar_labs/moksaya'),prefix('workon gsoc')):
                    run('./manage.py runserver')
