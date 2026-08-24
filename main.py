def welcome():
    print("====================== 🏋️‍♂️ FITNESS CLUB 🏋️‍♀️ ===========================")
    print("                                                    ✨ _Welcomes You")
    print("")
    print("=====================================================================")
    print("")
    print("")

def display_plans():
    print('')
    print('')
    print("📋 --- MEMBERSHIP PLANS & RATES ---")
    print("")
    print("🔹 1 Month Rate          : ₹1500 / month")
    print("🔹 2 to 5 Months Rate    : ₹1200 / month")
    print("🔹 6+ Months Rate        : ₹1000 / month")
    print("🔹 Fixed Admission Fee   : ₹300 (One-time)")
    print("🔹 Personal Trainer      : ₹500 / month (Optional)")
    print("---------------------------------------------------------------")
    print("")
    print("📌 INPUT GUIDELINES:")
    print('')
    print("1. Enter your Name (Text)")
    print("2. Enter Plan Duration (Number of months, e.g. 1, 3, 6)")
    print("3. Personal Trainer (Type 'Y' for Yes, 'N' for No)")
    print("----------------------------------------------------------------")
    print('')
    print('')

def plan_charge(months):
    if months == 1:
        return 1500 + 300
    if months <= 5:
        return months * 1200 + 300
    return months * 1000 + 300


def membership_card(name, months, T, price):
    print("")
    print("")
    print("------------------------- 💳 Membership Crard 💳 ---------------------------")
    print("")
    print("💳 Member : ", name)
    print("")
    print("⏳ Validity :", months, "month(s)")
    print("")
    print("🏋️‍♂️ Personal Trainer :", Trainer(T))
    print("")
    print("💰 Total Amount : ₹", price)
    print("")
    print("                                         ✅ _approved_by_ft._club")
    print("------------------------------------------------------------------------------")


def Trainer(T):
    if T == "Y" or T == "y":
        print("💵 Trainer Charges = 500/month")
        print("")
        return "Yes 🏋️"
    else:
        return "No ❌"

def trainer_charge(T,months):
    if T == "Y" or T == "y":
        return 500 * months
    else:
        return 0


welcome()
display_plans()
print('')
print("")
a = input("👤 YOUR NAME : ")
b = int(input("📅 PLAN DURATION ( In Months ) : "))
T = input("💪 Do You Want Personal Trainer (Y/N) : ")
print("")
print("")
price = plan_charge(b) + trainer_charge(T,b)

membership_card(a, b, T, price)