#!/usr/bin/env python3
"""Run the retained Gradle with the cloud HTTPS proxy and system TLS trust."""
import os
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlsplit

root = Path(__file__).resolve().parents[1]
environment = os.environ.copy()
environment.setdefault('JAVA_HOME', '/workspace/toolchains/jdk-21.0.8+9')
environment.setdefault('GRADLE_USER_HOME', '/workspace/.gradle-cache')
options = ['-Djavax.net.ssl.trustStore=/etc/ssl/certs/java/cacerts']
proxy = urlsplit(environment.get('HTTPS_PROXY', environment.get('https_proxy', '')))
if proxy.hostname:
    for scheme in ('http', 'https'):
        options.extend([f'-D{scheme}.proxyHost={proxy.hostname}',
                        f'-D{scheme}.proxyPort={proxy.port or 80}'])
    options.append('-Dhttp.nonProxyHosts=localhost|127.*|[::1]')
command = ['/workspace/toolchains/gradle-9.7.1/bin/gradle', '--no-daemon', *options, *sys.argv[1:]]
sys.exit(subprocess.call(command, cwd=root, env=environment))
