# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
    var = input("\n  Enter pipe message and press enter\n")
    value = var.split("|")
    my_output = map(dis, key, value)
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
