#!/usr/bin/python
# -*- coding: utf-8 -*-
from fabric.context_managers import settings

from provy.core import Role, AskFor
from provy.more.centos import YumRole, UserRole, PipRole
from provy.more.centos import HostNameRole, RabbitMqRole, GitRole

from centos import MySQLRole, NginxRole, SupervisorRole, MemcachedRole


class PreSetupRole(Role):
    def provision(self):
        new_user = self.context['new_user']

        self.execute('yum install -y sudo', stdout=False, sudo=True)
        # TODO: Pacote especial para sudo
        #with self.using(YumRole) as role:
        #    role.ensure_package('sudo')

        with self.using(UserRole) as role:
            role.ensure_group('admin')
            self.ensure_line('%admin  ALL=(ALL) NOPASSWD: ALL', '/etc/sudoers',
                             sudo=True)
            role.ensure_user(new_user, is_admin=True)

        # TODO: Melhorar
        self.ensure_dir('/home/{0}/.ssh/'.format(new_user), owner=new_user)
        self.change_dir_mode('/home/{0}/.ssh/'.format(new_user), 700)

        authorized_keys = '/home/{0}/.ssh/authorized_keys'.format(new_user)

        cmd = 'cat /root/.ssh/authorized_keys >> {0}'.format(authorized_keys)
        self.execute(cmd, sudo=True)

        self.change_file_owner(authorized_keys, new_user)
        self.change_file_mode(authorized_keys, 600)
        # TODO: Disable root login


class MainServer(Role):
    def provision(self):
        with settings(warn_only=True):
            self.execute('rpm -ivh http://download.fedoraproject.org/pub/epel'
                     '/6/i386/epel-release-6-5.noarch.rpm', sudo=True)

        with self.using(HostNameRole) as role:
            role.ensure_hostname('pug.pe')

        self.log('Starting MySQLRole')
        with self.using(MySQLRole) as role:
            role.ensure_user(
                username=self.context['mysql_user'], login_from="localhost",
                identified_by=self.context['mysql_password'],
            )

            role.ensure_database(self.context['mysql_database'])

            role.ensure_grant(
                'ALL PRIVILEGES', on=self.context['mysql_database'],
                username=self.context['mysql_user'], login_from='localhost',
            )

        self.log('Starting NginxRole')
        with self.using(NginxRole) as role:
            role.ensure_conf(conf_template='nginx.conf')
            role.ensure_site_disabled('default')

            role.create_site(
                site=self.context['site'],
                template=self.context['template'],
            )
            role.ensure_site_enabled(self.context['site'])

        self.log('Starting MemcachedRole')
        self.provision_role(MemcachedRole)

        self.log('Starting SupervisorRole')
        with self.using(SupervisorRole) as role:
            self.ensure_dir('/var/log/supervisor', sudo=True)
            self.ensure_dir(self.context['include_dir'], sudo=True)

            role.config(
                config_file_directory='/etc/',
                log_folder='/var/log/supervisor',
                user='root',
            )
            include = self.context['include']
            # Should config have kwargs?
            role.context['supervisor-config']['include'] = include
            role.restart()

        self.log('Starting GitRole')
        with self.using(GitRole) as role:
            role.ensure_repository(
                self.context['repo'], self.context['base_path'],
                self.context['owner']
            )

        self.log('Starting Virtualenv')
        with self.using(PipRole) as role:
            role.ensure_package_installed('virtualenv')

        self.log('Starting deps')
        with self.using(YumRole) as role:
            # Deps for PIL
            role.ensure_package_installed('zlib-devel')
            role.ensure_package_installed('libjpeg-devel')
            role.ensure_package_installed('freetype-devel')

            # Deps for Mysql (driver)
            role.ensure_package_installed('mysql-devel')


address = '23.21.186.244'

servers = {
    'pre_setup': {
        'address': address,
        'user': 'root',
        'roles': [
            PreSetupRole,
        ],
        'options': {
            'new_user': 'pugpe',
        }
    },

    'frontend': {
        'address': address,
        'user': 'pugpe',
        'roles': [
            MainServer
        ],
        'options': {
            # mysql
            'mysql_user': 'pugpe',
            'mysql_password': AskFor('mysql_password', 'Mysql password'),
            'mysql_database': 'pugpe',

            # supervisord
            'include_dir': '/etc/supervisor/conf.d/',
            'include': '/etc/supervisor/conf.d/*.conf',

            # Project specific
            'site': 'pugpe',
            'template': 'pugpe',

            'repo': 'git://github.com/pugpe/pugpe_portal.git',
            'base_path' : '/srv/pugpe/',
            'project_path': '/srv/pugpe/portal/',
        }
    }
}
