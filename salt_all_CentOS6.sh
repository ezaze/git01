echo 需要传参－－服务器ID名
/usr/bin/bash salt_addbashrc.sh $1
/usr/bin/bash salt_addkey.sh $1
/usr/bin/bash salt_addzabbix_agent_c6.sh $1
