
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

# Dictionaries for categorical to numerical conversion
OverTime_dict = {"No": 0, "Yes": 1}
BusinessTravel_dict = {"Travel_Rarely": 0, "Travel_Frequently": 1, "Non-Travel": 2}
Department_dict = {"Research & Development": 0, "Sales": 1, "Human Resources": 2}
EducationField_dict = {"Life Sciences": 0, "Medical": 1, "Marketing": 2, "Technical Degree": 3, "Other": 4, "Human Resources": 5}
Gender_dict = {"Male": 0, "Female": 1}
JobRole_dict = {
    "Sales Executive": 0,
    "Research Scientist": 1,
    "Laboratory Technician": 2,
    "Manufacturing Director": 3,
    "Healthcare Representative": 4,
    "Manager": 5,
    "Sales Representative": 6,
    "Research Director": 7,
    "Human Resources": 8
}
MaritalStatus_dict = {"Married": 0, "Single": 1, "Divorced": 2}
Resigned_dict = {"No": 0, "Yes": 1}

# Reverse dictionaries for displaying dropdown options
OverTime_rev_dict = {v: k for k, v in OverTime_dict.items()}
BusinessTravel_rev_dict = {v: k for k, v in BusinessTravel_dict.items()}
Department_rev_dict = {v: k for k, v in Department_dict.items()}
EducationField_rev_dict = {v: k for k, v in EducationField_dict.items()}
Gender_rev_dict = {v: k for k, v in Gender_dict.items()}
JobRole_rev_dict = {v: k for k, v in JobRole_dict.items()}
MaritalStatus_rev_dict = {v: k for k, v in MaritalStatus_dict.items()}
Resigned_rev_dict = {v: k for k, v in Resigned_dict.items()}

# Title and description
st.title("Employee Attrition Prediction App")
st.markdown("This app predicts employee attrition based on various factors.")
col1, col2, col3 = st.columns(3)

# User input form
with st.form("user_input"):
    with col1:
        age = st.number_input('Age', min_value=0, max_value=100)
        daily_rate = st.number_input('DailyRate($)', min_value=0)
        distance_from_home = st.number_input('DistanceFromHome(km)', min_value=0)
        employee_number = st.number_input('EmployeeNumber', min_value=0)
        environment_satisfaction = st.number_input('EnvironmentSatisfaction', min_value=0, max_value=4)
        hourly_rate = st.number_input('HourlyRate', min_value=0)
        job_involvement = st.number_input('JobInvolvement', min_value=0, max_value=5)
        job_level = st.number_input('JobLevel', min_value=0)
        job_satisfaction = st.number_input('JobSatisfaction', min_value=0, max_value=5)
        monthly_income = st.number_input('MonthlyIncome($)', min_value=0)
        monthly_rate = st.number_input('MonthlyRate($)', min_value=0)
    
    with col2:
        
        num_companies_worked = st.number_input('NumCompaniesWorked', min_value=0)
        percent_salary_hike = st.number_input('PercentSalaryHike', min_value=0, max_value=100)
        performance_rating = st.number_input('PerformanceRating', min_value=0, max_value=5)
        relationship_satisfaction = st.number_input('RelationshipSatisfaction', min_value=0, max_value=5)
        standard_hours = st.number_input('StandardHours', min_value=0)
        stock_option_level = st.number_input('StockOptionLevel', min_value=0, max_value=3)
        total_working_years = st.number_input('TotalWorkingYears', min_value=0)
        training_times_last_year = st.number_input('TrainingTimesLastYear', min_value=0)
        work_life_balance = st.number_input('WorkLifeBalance', min_value=0, max_value=5)
        years_at_company = st.number_input('YearsAtCompany', min_value=0)
    
    with col3:
        
        years_in_current_role = st.number_input('YearsInCurrentRole', min_value=0)
        years_since_last_promotion = st.number_input('YearsSinceLastPromotion', min_value=0)
        years_with_curr_manager = st.number_input('YearsWithCurrManager', min_value=0)
        business_travel = st.selectbox('BusinessTravel', options=list(BusinessTravel_rev_dict.keys()), format_func=lambda x: BusinessTravel_rev_dict[x])
        department = st.selectbox('Department', options=list(Department_rev_dict.keys()), format_func=lambda x: Department_rev_dict[x])
        education_field = st.selectbox('EducationField', options=list(EducationField_rev_dict.keys()), format_func=lambda x: EducationField_rev_dict[x])
        gender = st.selectbox('Gender', options=list(Gender_rev_dict.keys()), format_func=lambda x: Gender_rev_dict[x])
        job_role = st.selectbox('JobRole', options=list(JobRole_rev_dict.keys()), format_func=lambda x: JobRole_rev_dict[x])
        marital_status = st.selectbox('MaritalStatus', options=list(MaritalStatus_rev_dict.keys()), format_func=lambda x: MaritalStatus_rev_dict[x])
        over_time = st.selectbox('OverTime', options=list(OverTime_rev_dict.keys()), format_func=lambda x: OverTime_rev_dict[x])
    
    submitted = st.form_submit_button("Predict Demand")
try:
    # Create a DataFrame from the user inputs
    if submitted:
        input_values = {
        "Age": age,
        "BusinessTravel": business_travel,
        "DailyRate($)": daily_rate,
        "Department": department,
        "DistanceFromHome(km)": distance_from_home,
        "EducationField": education_field,
        "EmployeeNumber": employee_number,
        "EnvironmentSatisfaction": environment_satisfaction,
        "Gender": gender,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobRole": job_role,
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital_status,
        "MonthlyIncome($)": monthly_income,
        "MonthlyRate($)": monthly_rate,
        "NumCompaniesWorked": num_companies_worked,
        "OverTime": over_time,
        "PercentSalaryHike": percent_salary_hike,
        "PerformanceRating": performance_rating,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StandardHours": standard_hours,
        "StockOptionLevel": stock_option_level,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": training_times_last_year,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_current_role,
        "YearsSinceLastPromotion": years_since_last_promotion,
        "YearsWithCurrManager": years_with_curr_manager
    }

        df = pd.DataFrame([input_values])
        st.dataframe(df)

        # Scale the DataFrame
        df1 = scaler.transform(df)

        # Predict the result
        result = model.predict(df1)
        
        # Display the prediction result
        # st.write("Prediction:", Resigned_rev_dict[int(result[0])])
        st.success(f'Resignation of Employee :  {Resigned_rev_dict[int(result[0])]}')
except Exception as e:
    st.error('Check the data format', icon="🚨")
    st.write(e)  