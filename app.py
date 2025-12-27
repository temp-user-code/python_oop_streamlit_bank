import streamlit as st
from bank_account import BankAccount

st.title("Simple Bank Management System")

if "bank_accounts" not in st.session_state:
    st.session_state.bank_accounts = []


menu_choice = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Account",
        "Access Account (Deposit/Withdraw)",
        "Delete Account",
        "View All Accounts",
    ],
)

if menu_choice == "Create Account":
    st.header("Create New Account")
    name_input = st.text_input("Enter Account Holder Name")
    balance_input = st.number_input("Enter Initial Balance", min_value=0 , step=1)

    if st.button("Create Account"):
        if name_input:
            new_acc = BankAccount(name_input, balance_input)
            st.session_state.bank_accounts.append(new_acc)

            st.success(
                f"Account Created! Name: {new_acc.account_holder}, Number: {new_acc.account_number}"
            )
        else:
            st.error("Please enter a name.")

elif menu_choice == "Access Account (Deposit/Withdraw)":
    st.header("Login to Account")
    acc_num_input = st.text_input("Enter Account Number to Login")

    account_found = BankAccount.find_account(
        acc_num_input, st.session_state.bank_accounts
    )

    if account_found:
        st.info(f"Welcome, {account_found.account_holder}!")

        tab1, tab2, tab3 = st.tabs(["Deposit", "Withdraw", "Check Balance"])

        with tab1:
            dep_amount = st.number_input("Amount to Deposit", min_value=0, step=1, key="dep")
            if st.button("Deposit Money"):
                message = account_found.deposit(dep_amount)
                st.success(message)

        with tab2:
            wid_amount = st.number_input("Amount to Withdraw", min_value=0, step=1, key="wid")
            if st.button("Withdraw Money"):
                message = account_found.withdraw(wid_amount)
                if message.startswith("In"):
                    st.error(message)
                else:
                    st.success(message)

        with tab3:
            st.write(account_found.check_balance())

    elif acc_num_input:
        st.error("Account not found.")

elif menu_choice == "Delete Account":
    st.header("Delete Account")
    del_acc_num = st.text_input("Enter Account Number to Delete")

    if st.button("Delete Permanently"):
        account_to_delete = BankAccount.find_account(
            del_acc_num, st.session_state.bank_accounts
        )

        if account_to_delete:
            st.session_state.bank_accounts.remove(account_to_delete)
            st.success("Account Deleted Successfully.")
        else:
            st.error("Account not found.")

elif menu_choice == "View All Accounts":
    st.header("Admin: All Accounts")
    if st.session_state.bank_accounts:
        for acc in st.session_state.bank_accounts:
            st.write(acc.get_details())
    else:
        st.warning("No accounts in system yet.")
