def dis(a, b):
    return format(a, '-<60') + b


def call():
    print(" Press 1:  To enter another pipe message again")
    print(" Press 0:  To exit from this application\n")
    var1 = input("  Enter your choice\n")
    if var1.isdigit():
        var1 = int(var1)
    if var1 == 1:
        myfun()
    elif var1 == 0:
        exit()
    else:
        print(" Invalid argument Please enter valid argument as per instruction")
        call()


def myfun():
    # Use a breakpoint in the code line below to debug your script.
    key = ['u', '<vers>=19', '<msgId>', '<stationId>', '<timespec>', '<outlet>', '<msghdrversion>',
           '<sesstag>', '<sessId>', '<energyinkwh>', '<transTime>', '<flagFinalSummary>', '<endReason>',
           '<trans_start_time>', '<trans_end_time>', '<temperature>', '<chargingTime>', '<powerinkw>',
           '<chrgState>', 'faultState', '<SessStartTimeSynced>', '<SessEndTimeSynced>', '<cardtype>',
           '<sesstag_enc>', 'PricingVersion', 'timeOffset', 'GroupID', 'PlanID#PlanVersion#PolicyID#PolicyVersion',
           'lineItemVersion', 'TotalPrice', 'lineItem1#lineItem2#..LineItem N', 'CCAuthToken', 'ReservID',
           'VoilationFee', 'PrimeDirectiveInd', 'AuthLatency', 'FragNum', 'DataFormatVersion', 'LastFragment',
           'NumTuples', '<tuples-list>', 'rmsVoltage', 'rmsCurrent', 'ActiveChargingTime', 'ActiveNotChargingTime',
           'ActiveTransientTime', 'dibId', 'chgmode', 'soc', 'rct', 'touSchedChrgSessByDblPmp', 'startWattHour',
           'endWattHour', '<convenience_fee>', 'allowedPower', '', '', '', 'numOffTuples', '<offline-tupple-list>', 'u']

    key_1 = ['aur', '<vers>', '<msgId>', '<stationId>', '<timespec>', '<outlet>', '<msghdrversion>', '<sessTag>',
             '<time>', '<authStatus>', '<sessionsPending>', '<subscrType>', '<failureCode>', 'token', 'sessId',
             'mode1QueueSize', 'touAclGroup^PRICING#touPricingGroup', 'failure_msg', 'chth', 'aur']

    key_2 = ['br', 'version', 'msgId', 'smartletid', '<timespec>', '<outlet>', '<msghdrversion>', 'seqNum',
             'epochbootcnt', 'sw version', 'hw model', 'bootreason', 'lastbootstate', 'bank', '<md5sumBankA>',
             '<md5sumBankB>', '<bootuptime>', 'uptime_before_boot', 'redundant_bank_id', 'redundant_bank_release',
             'where', 'who', 'what', 'when', 'sfd', '', '', '', 'hashAlgorithm', 'br']

    var = input("\n  Enter pipe message and press enter\n")
    value = "nothing"
    if "|" in var:
        value = var.split("|")
    else:
        print(" Invalid argument Please enter valid argument as per instruction")
        call()
    my_output = "nothing"
    if value[0] == "u" and value[1] == "19":
        my_output = map(dis, key, value)
    elif value[0] == "aur" and value[1] == "11":
        my_output = map(dis, key_1, value)
    elif value[0].replace(" ", "") == 'br' and value[1] == '6':
        my_output = map(dis, key_2, value)
    else:
        print("     " + value[0] + " with version " + value[1] + "  is not supported right now it is coming soon\n")
        call()
    arr = list(my_output)
    for i in arr:
        print("     " + i)

    print("\n\n")
    call()
    # print(value[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myfun()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
