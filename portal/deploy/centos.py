#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Compatibility module Debian > Centos
'''
from os.path import join

from fabric.context_managers import settings

from provy.core import Role
from provy.more.debian.database.mysql import MySQLRole as _MySQLRole
from provy.more.debian.web.nginx import NginxRole as _NginxRole
from provy.more.debian.monitoring.supervisor import SupervisorRole as _Super
from provy.more.centos.package.yum import YumRole
from provy.more.centos.package.pip import PipRole

from jinja2 import FileSystemLoader


class MySQLRole(_MySQLRole):
    def provision(self):
        with self.using(YumRole) as role:
            role.ensure_package_installed('mysql-server')
            role.ensure_package_installed('mysql')
            role.ensure_package_installed('mysql-devel')

            self.execute('chkconfig --add mysqld', sudo=True)
            self.execute('chkconfig mysqld on', sudo=True)

            with settings(warn_only=True):
                status = self.execute('service mysqld status', sudo=True)
            if not 'running' in status:
                self.execute('service mysqld start', sudo=True)


class NginxRole(_NginxRole):
    def provision(self):
        with self.using(YumRole) as role:
            role.ensure_package_installed('nginx')

        self.execute('chkconfig --add nginx', sudo=True)
        self.execute('chkconfig --level 35 nginx on', sudo=True)

        with settings(warn_only=True):
            status = self.execute('service nginx status', sudo=True)

        if not 'running' in status:
            self.execute('service nginx start', sudo=True)

        self.ensure_dir('/etc/nginx/sites-available/', sudo=True)
        self.ensure_dir('/etc/nginx/sites-enabled/', sudo=True)


class SupervisorRole(_Super):
    '''Also change templates to make use of [include] section'''
    def register_fs_template_loader(self, path):
        if path not in self.context['registered_loaders']:
            self.context['loader'].loaders.append(FileSystemLoader(path))
            self.context['registered_loaders'].append(path)

    def provision(self):
        #self.register_template_loader('provy.more.debian.monitoring')
        self.register_fs_template_loader('templates/')

        with self.using(PipRole) as role:
            role.ensure_package_installed('supervisor')

            # TODO: Put the right path in centos templates or fix path
            # with pip options
            ln = lambda p: 'ln -s /usr/bin/{0} /usr/local/bin/{0}'.format(p)
            with settings(warn_only=True):
                self.execute(ln('supervisord'), sudo=True)
                self.execute(ln('supervisorctl'), sudo=True)

    def update_init_script(self, config_file_path):
        options = {'config_file': join(config_file_path, 'supervisord.conf')}
        result = self.update_file(
                'supervisord.init.template', '/etc/init.d/supervisord',
                owner=self.context['owner'], options=options, sudo=True,
            )

        if result:
            self.execute(
                'chmod +x /etc/init.d/supervisord', stdout=False, sudo=True,
            )
            self.execute('chkconfig --add supervisord', sudo=True)
            self.execute('chkconfig supervisord on', sudo=True)
            self.ensure_restart()


class MemcachedRole(Role):
    def provision(self):
        with self.using(YumRole) as role:
            role.ensure_package_installed('memcached')
            self.execute('chkconfig --add mysqld', sudo=True)
            self.execute('chkconfig mysqld on', sudo=True)

            with settings(warn_only=True):
                status = self.execute('service memcached status', sudo=True)
            if not 'running' in status:
                self.execute('service mysqld start', sudo=True)
