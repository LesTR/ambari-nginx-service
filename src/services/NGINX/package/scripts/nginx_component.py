#!/usr/bin/env python
from resource_management import Script
from resource_management.core.logger import Logger
from resource_management.core.resources.system import Execute

class nginx_component(Script):
    def configure(self,env):
        pass
    def install(self,env):
        Logger.info("Installing packages")
        self.install_packages(env)
        Logger.info("Installing packages - Done")
    def start(self,env):
        Logger.info("Starting nginx service")
        Execute("service nginx start")
        Logger.info("Starting nginx service - Done")
    def stop(self,env):
        Logger.info("Stopping nginx service")
        Execute("service nginx stop")
        Logger.info("Stopping nginx service - Done")
    def status(self,env):
        Logger.info("Checking status nginx service")
        try:
            Execute("service nginx status")
        except Fail:
            raise ComponentIsNotRunning()
        Logger.info("Checking status nginx service - Done")

if __name__ == "__main__":
    nginx_component().execute()
