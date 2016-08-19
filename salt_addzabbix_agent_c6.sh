salt $1 state.sls zabbix.agent
salt $1 cmd.run '/usr/sbin/zabbix_agentd'
