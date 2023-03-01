
#value = "br|version|msgId|smartletid|<timespec>|<outlet>|<msghdrversion>|seqNum|epochbootcnt|sw version|hw model|bootreason|lastbootstate|bank|<md5sumBankA>|<md5sumBankB>|<bootuptime>|uptime_before_boot|redundant_bank_id|redundant_bank_release|where|who|what|when|sfd|||hashAlgorithm|br".split("|")
var1 = "    br|6|3401|FA3E0000C1B06144|1677662304|0|1|0|5|5.20.0+2023.01.00.63-alpha|CPF50-GW-LTE-L23-USA|RESET/WATCHDOG|RESET/WATCHDOG|A|NA|NA|1677648968|65493|NA|NA|||||0|0|||CA3-3-1|br".split("|")
#print(value)
#print(len(value))
print(var1)
print(len(var1))
print(var1[0].replace(" ", ""))