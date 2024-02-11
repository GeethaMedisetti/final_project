import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/DELL/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/DELL/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))

cancer_model = pickle.load(open('C:/Users/DELL/Desktop/Multiple Disease Prediction System/saved models/cancer_model.sav','rb'))

lung_cancer_model = pickle.load(open('C:/Users/DELL/Desktop/Multiple Disease Prediction System/saved models/lung_cancer_model.sav', 'rb'))
# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Breast Cancer Prediction', 
                           'Lung Cancer Prediction'],
                          icons=['activity','heart','person-arms-up','apple'],
                          default_index=0)
    
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


    # Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = st.text_input('Radius Mean')
        
    with col2:
        texture_mean = st.text_input('Texture Mean')
    
    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')
    
    with col1:
        area_mean = st.text_input('Area Mean')
    
    with col2:
        smoothness_mean = st.text_input('Smoothness Mean')
    
    with col3:
       compactness_mean  = st.text_input('Compactness Mean')
    
    with col1:
        concavity_mean = st.text_input('Concavity Mean')
    
    with col2:
        concave_points_mean = st.text_input('Concave Points Mean')
        
    with col3:
        symmetry_mean = st.text_input('Symmetry Mean')
    
    with col1:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')
    
    with col2:
        radius_se = st.text_input('Radius SE')
    
    with col3:
        texture_se = st.text_input('Texture SE')
    
    with col1:
        perimeter_se = st.text_input('Perimeter SE')
    
    with col2:
        area_se = st.text_input('Area SE')
    
    with col3:
        smoothness_se = st.text_input('Smoothness SE')

    with col1:
       compactness_se  = st.text_input('Compactness SE')
    
    with col2:
        concavity_se = st.text_input('Concavity SE')
    
    with col3:
        concave_points_se = st.text_input('Concave Points SE')
        
    with col1:
        symmetry_se = st.text_input('Symmetry SE')
    
    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')
    
    with col3:
        radius_worst = st.text_input('Radius Worst')
    
    with col1:
        texture_worst = st.text_input('Texture Worst')
    
    with col2:
        perimeter_worst  = st.text_input('Perimeter Worst')
    
    with col3:
        area_worst  = st.text_input('Area Worst')
    
    with col1:
        smoothness_worst  = st.text_input('Smoothness Worst')

    with col2:
       compactness_worst   = st.text_input('Compactness Worst')
    
    with col3:
        concavity_worst = st.text_input('Concavity Worst')
    
    with col1:
        concave_points_worst  = st.text_input('Concave Points Worst')
        
    with col2:
        symmetry_worst  = st.text_input('Symmetry Worst')
    
    with col3:
        fractal_dimension_worst  = st.text_input('Fractal Dimension Worst')
    
    
    # code for Prediction
    cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        cancer_prediction = cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        
        if (cancer_prediction[0] == 1):
          cancer_diagnosis = 'The person have Cancer'
        else:
          cancer_diagnosis = 'The person donot have Cancer'
        
    st.success(cancer_diagnosis)
    
if(selected == "Lung Cancer Prediction"):
    
    #page title
    st.title("Lung Cancer Prediction using Machine Learning")



# getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        GENDER = st.text_input("GENDER")
        
    with col2:
        AGE = st.text_input("AGE")
    
    with col3:
        SMOKING = st.text_input("SMOKING")
    
    with col4:
        YELLOW_FINGERS = st.text_input("YELLOW_FINGERS")
    
    with col1:
        ANXIETY = st.text_input("ANXIETY")
    
    with col2:
        PEER_PRESSURE = st.text_input("PEER_PRESSURE")
    
    with col3:
        CHRONIC_DISEASE = st.text_input("CHRONIC DISEASE")
    
    with col4:
        FATIGUE = st.text_input("FATIGUE")
    
    with col1:
        ALLERGY = st.text_input("ALLERGY")
    
    with col2:
        WHEEZING = st.text_input("WHEEZING")
    
    with col3:
        ALCOHOL_CONSUMING = st.text_input("ALCOHOL CONSUMING")
    
    with col4:
        COUGHING = st.text_input("COUGHING")
    
    with col1:
        SHORTNESS_OF_BREATH = st.text_input("SHORTNESS OF BREATH")
    
    with col2:
        SWALLOWING_DIFFICULTY = st.text_input("SWALLOWING DIFFICULTY")
    
    with col3:
        CHEST_PAIN = st.text_input("CHEST PAIN")
    


# code for Prediction
    lung_cancer_result = " "
    
    # creating a button for Prediction
    
    if st.button("Lung Cancer Test Result"):
        lung_cancer_report = lung_cancer_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        
        if (lung_cancer_report[0] == 0):
          lung_cancer_result = "Hurrah! You have no Lung Cancer."
        else:
          lung_cancer_result = "Sorry! You have Lung Cancer."
        
    st.success(lung_cancer_result)
 