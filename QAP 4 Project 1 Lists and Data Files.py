# Program description: This is a program designed to help the One Stop Insurance Company enter and calculate new insurance policy information for its customers.
# Written by: Ethan Miller
# Date written: July-17-2023 - July-20-2023

# Imports

import datetime
from tqdm import tqdm
from time import sleep
import FormatValues as FV

f = open('OSICDef.dat', 'r')
NEX_POLICY_NUM = int(f.readline())
BASI_PREM = float(f.readline())
DIS_FOR_ADD_CARS = float(f.readline())
COST_OF_EXT_LIA_COV = float(f.readline())
COST_OF_GLA_COV = float(f.readline())
COST_FOR_LOAN_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
PRO_FEE_FOR_MONT_PAY = float(f.readline())
f.close()

# Program inputs

while True:
    invoiceDate = datetime.datetime.now()
    nextPaymentDate = input("Enter the next payment date (YYYY-MM-DD) (First day of the next month) (Type End to stop the program): ")
    if nextPaymentDate == "End":
        break
    nextPaymentDate = datetime.datetime.strptime(nextPaymentDate, "%Y-%m-%d")

    custFirst = input("Enter the customer's first name: ").title()

    custLast = input("Enter the customer's last name: ").title()
    stAdd = input("Enter the street address: ")
    City = input("Enter the city: ").title()
    while True:
        provList = ["NL", "SA", "UK", "NU"]
        Province = input("Enter the province: ")
        if Province not in provList:
            print("Error - a valid province must be entered.")
        else:
            break
    postCode = input("Enter the postal code: ")
    phoNum = input("Enter the phone number: ")
    numCars = int(input("Enter the number of cars being insured: "))
    deciOptExt = input("Enter the decision for extra liability up to 1,000,000 (Y/N): ").upper()
    if deciOptExt != "Y" and deciOptExt != "N":
        print("Error - the choice must be entered as Y or N.")

    deciOptGlaCov = input("Enter the choice for optional glass coverage (Y/N): ").upper()
    if deciOptGlaCov != "Y" and deciOptGlaCov != "N":
        print("Error - the choice has to be entered as Y or N.")
    deciOptLoanCar = input("Enter the decision for the optional loaner car (Y/N): ").upper()
    if deciOptLoanCar != "Y" and deciOptLoanCar != "N":
        print("Error - the decision must be entered as Y or N.")
    while True:
        typeList = ["Full", "Monthly"]
        typePay = input("Enter the decision on paying full or monthly (Full or Monthly): ").title()
        if typePay not in typeList:
            print("Error - a valid payment method must be entered.")
        else:
            break

    # Program calculations/processing

    insPrem = 869.00 * numCars * 0.25
    OptionsExt = 130.00
    OptionsGlaCov = 86.00
    OptionsLoanCar = 58.00
    if deciOptExt == "Y" or deciOptGlaCov == "Y" or deciOptLoanCar == "Y":
        OptionsExt = 130.00
        OptionsGlaCov = 86.00
        OptionsLoanCar = 58.00
    totExt = OptionsExt + OptionsGlaCov + OptionsLoanCar
    totInsPrem = insPrem + totExt
    HST = totInsPrem * 0.15
    totCost = totInsPrem + HST
    montPay = 39.99 + totCost / 8

    # Program outputs
    print()
    print("One Stop Insurance Company")
    print("Insurance Policy Information Receipt")
    print("=" * 41)
    print(FV.FDateS(invoiceDate))
    print(FV.FDateS(nextPaymentDate))
    print(custFirst)
    print(custLast)
    print(stAdd)
    print(City)
    print(Province)
    print(postCode)
    print(phoNum)
    print(numCars)
    print(deciOptExt)
    print(deciOptGlaCov)
    print(deciOptLoanCar)
    if deciOptExt == "Y" or deciOptGlaCov == "Y" or deciOptLoanCar == "Y":
        print(f"{FV.FDollar2(OptionsExt)}")
        print(f"{FV.FDollar2(OptionsGlaCov)}")
        print(f"{FV.FDollar2(OptionsLoanCar)}")
    print(typePay)
    print(f"{FV.FDollar2(insPrem)}")
    print(f"{FV.FDollar2(totExt)}")
    print(f"{FV.FDollar2(totInsPrem)}")
    print(f"{FV.FDollar2(HST)}")
    print(f"{FV.FDollar2(totCost)}")
    print(f"{FV.FDollar2(montPay)}")
    print("=" * 41)

    # Doing stuff with the Policies.dat and OSICDef.dat files.

    print()
    print("Saving data for " + str(NEX_POLICY_NUM) + ".  Please wait a moment...")
    f = open("Policies.dat", "a")
    f.write(f"{str(NEX_POLICY_NUM)},")
    f.write(f"{(FV.FDateS(invoiceDate))},")
    f.write(f"{custFirst},")
    f.write(f"{custLast},")
    f.write(f"{stAdd},")
    f.write(f"{City},")
    f.write(f"{Province},")
    f.write(f"{postCode},")
    f.write(f"{phoNum},")
    f.write(f"{str(numCars)},")
    f.write(f"{deciOptExt},")
    f.write(f"{deciOptGlaCov},")
    f.write(f"{deciOptLoanCar},")
    f.write(f"{typePay},")
    f.write(f"{str(totInsPrem)}\n")
    f.close()
    print()
    for bar in tqdm(range(100)):
        sleep(0.02)
    print()
    print("Policy information processed and saved.")

    NEX_POLICY_NUM += 1

    f = open('OSICDef.dat', 'a')
    f.write(f"{str(NEX_POLICY_NUM)}\n")
    f.write(f"{str(FV.FComma2(BASI_PREM))}\n")
    f.write(f"{str(DIS_FOR_ADD_CARS)}\n")
    f.write(f"{str(FV.FComma2(COST_OF_EXT_LIA_COV))}\n")
    f.write(f"{str(FV.FComma2(COST_OF_GLA_COV))}\n")
    f.write(f"{str(FV.FComma2(COST_FOR_LOAN_CAR_COV))}\n")
    f.write(f"{str(HST_RATE)}\n")
    f.write(f"{str(PRO_FEE_FOR_MONT_PAY)}\n")
    f.close()






