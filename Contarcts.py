else:
    st.subheader('Accommodations ')
    Acc=st.selectbox(label='Select location', options=List_Acc)

    if Acc == 'Olaya':
        st.write('Contract amount 32,500 SAR')
        st.write('period of 01 year from 6/18/2020 - 6/18/2021')
        st.write('Total 01 installments')
        st.warning('Valid Contract')
        st.sidebar.subheader('Owner info:')
        st.sidebar.info('Name: Farag bin Masoud Al Dosary     Tel: 0112015092')
        st.subheader('Balance')
        source9 = 'C:/Users/Fawaz Almutairi/Desktop/KCS Data Base/OlayaAcc.xlsx'
        df9 = pd.read_excel(source9, usecols='A:E', header=0)
        st.write('Payment progress')
        st.progress(100)
        st.table(df9)

    if Acc == 'Qurtuba 1':
        st.write('Contract amount 60,000 SAR')
        st.write('period of 01 year')
        st.write('Total 01 installments')
        st.warning('Valid Contract')
        st.sidebar.subheader('Owner info:')
        st.sidebar.info('Name: Abdulmajeed Gzay AlMutairi    Phone: 0531181688')
        st.subheader('Balance')
        source10 = 'C:/Users/Fawaz Almutairi/Desktop/KCS Data Base/QurtubaAcc1.xlsx'
        df10 = pd.read_excel(source10, usecols='A:E', header=0)
        st.write('Payment progress')
        st.progress(100)
        st.table(df10)

    if Acc == 'Qurtuba 2':
        st.write('Contract amount 23,000 SAR')
        st.write('period of 01 year')
        st.write('Total 01 installments')
        st.warning('Valid Contract')
        st.sidebar.subheader('Owner info:')
        st.sidebar.info('Name: Abdulmajeed Gzay AlMutairi    Phone: 0531181688')
        st.subheader('Balance')
        source16 = 'C:/Users/Fawaz Almutairi/Desktop/KCS Data Base/QurtubaAcc2.xlsx'
        df16 = pd.read_excel(source16, usecols='A:E', header=0)
        st.write('Payment progress')
        st.progress(100)
        st.table(df16)

    if Acc == 'AlMalqa':
        st.write('Contract amount 34,000 SAR')
        st.write('period of 01 year  from 10/18/2020 - 10/17/2021')
        st.write('Total 01 installments ')
        st.warning('Not Valid Contract')
        st.sidebar.subheader('Owner info:')
        st.sidebar.info('Name: Khaled Haza Gari AlQahtani   Phone: 0531181688')
        st.subheader('Balance')
        source11 = 'C:/Users/Fawaz Almutairi/Desktop/KCS Data Base/MalqaAcc.xlsx'
        df11 = pd.read_excel(source11, usecols='A:E', header=0)
        st.write('Payment progress')
        st.progress(100)
        st.table(df11)

    if Acc == 'Sawaidi':
        st.write('Contract amount 15,000 SAR')
        st.write('period of 01 year from 10/18/2020 - 10/6/2021')
        st.write('Total 01 installments')
        st.warning('Not Valid Contract')
        st.subheader('Balance')
        st.sidebar.subheader('Owner info:')
        st.sidebar.info('Name: Badrya  Sulaiman AlSaif      Phone: 0595619000')
        source14 = 'C:/Users/Fawaz Almutairi/Desktop/KCS Data Base/SawaidiAcc.xlsx'
        df14 = pd.read_excel(source14, usecols='A:E', header=0)
        st.write('Payment progress')
        st.progress(100)
        st.table(df14)
    if Acc == 'Head Office':
        st.write('Contract amount 514,560 SAR')
        st.write('period of 01 year from 1/1/2021 - 12/31/2022')
        st.write(' Total 04 installments')
        st.warning('Valid Contract')
        st.sidebar.subheader('Owner info:')
        st.sidebar.info('Name: Abdulmalik Mohamed almasri   Phone: 0505456116')
        st.subheader('Balance')
        source6 = 'C:/Users/Fawaz Almutairi/Desktop/KCS Data Base/Head.xlsx'
        df6 = pd.read_excel(source6, usecols='A:E', header=0)
        st.write('Payment progress')
        st.progress(25)
        st.table(df6)








