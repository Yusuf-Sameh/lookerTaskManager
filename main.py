import streamlit as st


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Create tabs
tabs = ['English', 'Arabic']
tab1, tab2 = st.tabs(tabs)


# Display selected tab
with tab1:
    st.title('Data Analytics Dashboard in Looker Studio & Google Sheet ')
    st.divider()
    
    st.header('About:')
    st.write('By: Youssef Sameh\n\nIn: April 2023\n\ncontact: youssefpasha49@gmail.com')
    st.divider()
    
    st.header('Project Description:')
    st.write('This project aims to develop a dashboard in Looker Studio that displays analytics about data extracted from Google Sheets about manage employees tasks. Users can access this dashboard and filter the data according to various criteria such as status, priority, category, %finished, date, employee, and supervisor. The dashboard also contains a variety of charts that help analyze the data better.\n\n Also JS script used in google sheet to notify manager automatically via email when task is closed\n\nThe dashboard is linked to a Mobile APP')
    st.divider()
    
    st.header('Tech Used:')
    st.write('''1- Looker studio\n\n2- Google Sheet\n\n3- Python\n\n4- Java Script''')
    st.divider()

    st.header('Looker Dashboard')
    st.write('Not an image. You can interact with the dashboard below\n\nUse Full Screen below')
    import looker_sdk
    html = f'<iframe width="600" height="475" src="https://lookerstudio.google.com/embed/reporting/0ab9ee33-6e48-4497-b617-3bb1c5d266ff/page/s30MD" frameborder="0" style="border:0" allowfullscreen></iframe>'
    st.markdown(html, unsafe_allow_html=True)
    st.divider()
    
    st.header('Project Explanation:')
    st.write(''' The data in Google Sheets consists of the following columns:\n\n1- Tasks: This column contains the name of the task being executed.\n\n2- date_start: This column contains the start date of the task.\n\n3- date_end: This column contains the end date of the task.\n\n4- Employee: This column contains the name of the employee who is responsible for executing the task.\n\n5- Supervisor: This column contains the name of the supervisor who is monitoring the task.\n\n6- Status: This column contains the status of the task (completed, in progress, canceled).\n\n7- Priority: This column contains the priority level of the task (low, medium, high).\n\n8- Category: This column contains the category of the task (e.g., marketing, development, management).\n\n9- Finished: This column contains the percentage of completion of the task.\n\n10- expected_end_period_days: This column contains the expected period for completing the task.\n\n11- actual_end_period_days: This column contains the actual period taken to complete the task.\n\n12- Description: This column contains a detailed description of the task.\n\n13- Comments: This column contains comments and notes related to the task.\n\n14- Attachment: This column contains any attachments or files related to the task.''')
    import pandas as pd
    url = 'https://docs.google.com/spreadsheets/d/1HwfvKxMfTKGJVS6RUa6gSdqstuVKWajKxrk4NyHnEv4/export?format=csv&usp==sharing'
    df = pd.read_csv(url)
    df
    st.divider()
    
    st.header('Javascript')
    st.code("""function sendMailEdit(e){
            if (e.range.columnStart != 6 || e.value != "closed") return;
            const rData = e.source.getActiveSheet().getRange(e.range.rowStart,1,1,11).getValues();
            let taskName = rData[0][0];
            let assignedTo = rData[0][3];
            let supervisor = rData[0][4];
            let priority = rData[0][6];
            let msg = "Task ("+taskName+") assigned to ("+assignedTo+"), supervisor ("+supervisor+") is CLOSED NOW"
            MailApp.sendEmail("ManagerMail@any.com", "Task Closed !", msg)
            }""",language='javascript')
    
    
with tab2:
    st.header('حول:')
    st.write('بواسطة: يوسف سامح\n\nفي: أبريل 2023\n\nالاتصال: youssefpasha49@gmail.com')
    st.divider()

    st.header('وصف المشروع:')
    st.write('هدف هذا المشروع هو تطوير لوحة تحكم في Looker Studio تعرض تحليلات حول البيانات المستخرجة من Google Sheets حول إدارة مهام الموظفين. يمكن للمستخدمين الوصول إلى هذه اللوحة وتصفية البيانات وفقًا لمعايير مختلفة مثل الحالة والأولوية والفئة والانتهاء بنسبة %، التاريخ والموظف والمشرف. كما تحتوي اللوحة على مجموعة متنوعة من الرسوم البيانية التي تساعد على تحليل البيانات بشكل أفضل. \n\n يتم استخدام نص جافا سكريبت في جوجل شيت لإخطار المدير تلقائيًا عبر البريد الإلكتروني عند إغلاق المهمة\n\nاللوحة مرتبطة بتطبيق الجوال')
    st.divider()

    st.header('التقنيات المستخدمة:')
    st.write('''1- Looker studio\n\n2- Google Sheet\n\n3- Python\n\n4- Java Script''')
    st.divider()

    st.header('لوحة تحكم Looker')
    st.write('ليست صورة. يمكنك التفاعل مع اللوحة أدناه\n\nاستخدم الشاشة الكاملة أدناه')
    import looker_sdk
    html = f'<iframe width="600" height="475" src="https://lookerstudio.google.com/embed/reporting/0ab9ee33-6e48-4497-b617-3bb1c5d266ff/page/s30MD" frameborder="0" style="border:0" allowfullscreen></iframe>'
    st.markdown(html, unsafe_allow_html=True)
    st.divider()

    st.header('شرح المشروع:')
    st.write(''' البيانات في جوجل شيت تتكون من الأعمدة التالية:\n\n1- المهام: تحتوي هذه العمود على اسم المهمة التي يتم تنفيذها.\n\n2- تاريخ البدء: يحتوي هذا العمود على تاريخ بدء المهمة.\n\n3- تاريخ الانتهاء: يحتوي هذا العمود على تاريخ انتهاء المهمة.\n\n4- الموظف: يحتوي هذا العمود على اسم الموظف المسؤول عن تنفيذ المهمة.\n\n5- المشرف: يحتوي هذا العمود على اسم المشرف الذي يراقب المهمة.\n\n6- الحالة: يحتوي هذا العمود على حالة المهمة (مكتملة، قيد التنفيذ، ملغاة).\n\n7- الأولوية: يحتوي هذا العمود على مستوى الأولوية للمهمة (منخفضة، متوسطة، عالعالية).\n\n8- الفئة: يحتوي هذا العمود على فئة المهمة (على سبيل المثال، التسويق، التطوير، الإدارة).\n\n9- الانتهاء: يحتوي هذا العمود على نسبة الانتهاء من المهمة.\n\n10- المدة المتوقعة للانتهاء: يحتوي هذا العمود على المدة المتوقعة لإنجاز المهمة.\n\n11- المدة الفعلية للانتهاء: يحتوي هذا العمود على المدة الفعلية التي استغرقت لإنجاز المهمة.\n\n12- الوصف: يحتوي هذا العمود على وصف مفصل للمهمة.\n\n13- التعليقات: يحتوي هذا العمود على تعليقات وملاحظات متعلقة بالمهمة.\n\n14- المرفقات: يحتوي هذا العمود على أي مرفقات أو ملفات متعلقة بالمهمة.''')
    import pandas as pd
    url = 'https://docs.google.com/spreadsheets/d/1HwfvKxMfTKGJVS6RUa6gSdqstuVKWajKxrk4NyHnEv4/export?format=csv&usp==sharing'
    df = pd.read_csv(url)
    df
    st.divider()
    
    st.header('Javascript')
    st.code("""function sendMailEdit(e){
            if (e.range.columnStart != 6 || e.value != "closed") return;
            const rData = e.source.getActiveSheet().getRange(e.range.rowStart,1,1,11).getValues();
            let taskName = rData[0][0];
            let assignedTo = rData[0][3];
            let supervisor = rData[0][4];
            let priority = rData[0][6];
            let msg = "Task ("+taskName+") assigned to ("+assignedTo+"), supervisor ("+supervisor+") is CLOSED NOW"
            MailApp.sendEmail("ManagerMail@any.com", "Task Closed !", msg)
            }""",language='javascript')
