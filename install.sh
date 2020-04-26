#! /bin/bash

installSoftware() {
    apt -qq -y install python3-flask uwsgi-plugin-python3 nginx
}

installSimpleDataAnalysis() {
    mkdir -p /var/log/uwsgi
    curl -Lo- https://github.com/sunshineplan/SimpleDataAnalysis/archive/v1.0.tar.gz | tar zxC /var/www
    mv /var/www/SimpleDataAnalysis* /var/www/sda
}

setupsystemd() {
    cp -s /var/www/sda/sda.service /etc/systemd/system
    systemctl enable sda
    service sda start
}

writeLogrotateScrip() {
    if [ ! -f '/etc/logrotate.d/uwsgi' ]; then
        cat >/etc/logrotate.d/uwsgi <<-EOF
		/var/log/uwsgi/*.log {
		    copytruncate
		    rotate 12
		    compress
		    delaycompress
		    missingok
		    notifempty
		}
		EOF
    fi
}

setupNGINX() {
    cp -s /var/www/sda/SimpleDataAnalysis.conf /etc/nginx/conf.d
    sed -i "s/\$domain/$domain/" /var/www/sda/SimpleDataAnalysis.conf
    service nginx reload
}

main() {
    read -p 'Please enter domain:' domain
    installSoftware
    installSimpleDataAnalysis
    setupsystemd
    writeLogrotateScrip
    setupNGINX
}

main
