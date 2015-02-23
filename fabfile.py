""" Kalien.net Management Commands """

from datetime import datetime
from fabric.api import abort, env, get, lcd, local, run, task
from fabric.contrib.project import rsync_project
import fabhelper as lfh


env.use_ssh_config = True

BACKUP_DIR = 'backups'
GIT_REPO = 'git@github.com:meganlkm/kalien.net.git'
PROJECT_BUILD = 'project-build'
APP_DIR = 'main-app'


def get_app_build_dir():
    return lfh.joinpath(lfh.cwd(), PROJECT_BUILD, APP_DIR)


def clone(branch, dest=PROJECT_BUILD):
    """ clone the repo """
    if lfh.exists(dest):
        # change this to prompt for y/n to continue
        abort('Build directory [{0}] already exists'.format(dest))
    local("git clone -b {0} {1} {2}".format(branch, GIT_REPO, dest))


def composer_install(options=''):
    """ run composer install command """
    with lcd(get_app_build_dir()):
        local('composer install {0}'.format(options))


def deploy_local():
    print "deploying local..."


def deploy_dev(branch):
    print "deploying dev..."
    clone(branch)
    composer_install('--no-dev')
    rsync_project('~/dev/', local_dir='{0}/'.format(PROJECT_BUILD), delete=True, upload=True,
                  exclude=lfh.file2list(lfh.joinpath(lfh.cwd(), PROJECT_BUILD, '.build-exclude')))
    lfh.rm(PROJECT_BUILD)


@task(alias='b')
def backup(siteenv='production'):
    """
    back stuff up and download it

    Options:
        production (default) - backup/download ./APP_DIR and ./public_html
        dev - backup/download ./dev
        all - backup/download ./
    """
    tar_file = 'kalien-{0}-{1}.tar.gz'.format(siteenv, int(datetime.utcnow().strftime('%Y%m%d%H%M%S')))
    if siteenv == 'production':
        path = '{0} public_html'.format(APP_DIR)
    elif siteenv == 'dev':
        path = 'dev'
    elif siteenv == 'all':
        path = '.'
    else:
        abort('Invalid option: {0}'.format(siteenv))
    run('tar czf {0} {1}'.format(tar_file, path))
    get(tar_file, lfh.joinpath(BACKUP_DIR, tar_file))
    run('rm {0}'.format(tar_file))


@task(alias='d')
def deploy(deployenv='local', branch='master'):
    """ deploy :branch to :environment """
    if deployenv == 'local':
        deploy_local()
        return
    elif deployenv == 'dev':
        backup('dev')
        deploy_dev(branch)
        return
    else:
        abort("Environment: {0} does not exist".format(deployenv))


@task()
def ls(path='.'):
    run('ls -al {0}'.format(path))
