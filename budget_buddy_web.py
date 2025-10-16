import streamlit as st

st.title("🚀 Simple Budget Buddy")
st.write("Enter your details below to analyze your spending trends and get a 3-month projection!")

st.sidebar.header("Your Inputs")
budget = st.sidebar.number_input("Monthly Budget ($)", min_value=0.0, value=3000.0, step=100.0)
num_months = st.sidebar.slider("Number of Past Months to Analyze", min_value=1, max_value=12, value=3)

expenses = []
for i in range(1, num_months + 1):
    expense = st.sidebar.number_input(f"Month {i} Spending ($)", min_value=0.0, value=2500.0, step=50.0)
    expenses.append(expense)

if st.sidebar.button("Run Analysis! 📊"):
    if all(e >= 0 for e in expenses) and budget > 0:
        total_spent = sum(expenses)
        avg_monthly_spend = total_spent / len(expenses)

        col1, col2, col3 = st.columns(3)
        col1.metric("Monthly Budget", f"${budget:,.2f}")
        col2.metric("Avg. Monthly Spend", f"${avg_monthly_spend:,.2f}")
        col3.metric("Total Spent (Past Months)", f"${total_spent:,.2f}")

        if avg_monthly_spend < budget:
            status = "✅ You're under budget—great job!"
            savings_per_month = budget - avg_monthly_spend
            color = "green"
        elif avg_monthly_spend == budget:
            status = "⚖️ Breaking even—steady!"
            savings_per_month = 0
            color = "blue"
        else:
            status = "⚠️ Over budget—time to adjust!"
            savings_per_month = budget - avg_monthly_spend
            color = "red"

        st.success(status) 
        st.write(f"**Avg. Monthly Savings/Deficit:** ${savings_per_month:,.2f}")

        st.header("🔮 3-Month Projection")
        projection_months = 3
        projected_total = total_spent + (avg_monthly_spend * projection_months)
        projected_budget_total = budget * (len(expenses) + projection_months)
        projected_savings = projected_budget_total - projected_total

        col4, col5, col6 = st.columns(3)
        col4.metric("Projected Spending", f"${projected_total:,.2f}")
        col5.metric("Projected Budget", f"${projected_budget_total:,.2f}")
        col6.metric("Projected Net", f"${projected_savings:,.2f}")

        if projected_savings > 0:
            st.balloons()
            st.success("Future: Building savings! 💰 Keep it up!")
        elif projected_savings == 0:
            st.info("Future: Balanced—nice! ⚖️")
        else:
            st.warning("Future: Shortfall ahead—cut back! ⚠️")

    else:
        st.error("Please enter positive values for budget and expenses.")

st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ in Python & Streamlit")
