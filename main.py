import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data from Excel
@st.cache_data
def load_data(uploaded_file):
    return pd.read_excel(uploaded_file, engine='openpyxl')

# Function to generate charts
def generate_chart(data, chart_type, x_column, y_column=None):
    plt.figure(figsize=(10, 6))
    if chart_type == 'Bar Chart':
        if x_column in data.columns and y_column in data.columns:
            sns.barplot(data=data, x=x_column, y=y_column)
            plt.xticks(rotation=45)
        else:
            st.error(f"Selected columns '{x_column}' or '{y_column}' do not exist in the data.")
    elif chart_type == 'Line Chart':
        if x_column in data.columns and y_column in data.columns:
            sns.lineplot(data=data, x=x_column, y=y_column)
            plt.xticks(rotation=45)
        else:
            st.error(f"Selected columns '{x_column}' or '{y_column}' do not exist in the data.")
    elif chart_type == 'Pie Chart':
        if x_column in data.columns:
            data[x_column].value_counts().plot.pie(autopct='%1.1f%%')
            plt.ylabel('')
            plt.title(f'{x_column} Distribution')
        else:
            st.error(f"Selected column '{x_column}' does not exist in the data.")
    st.pyplot(plt)

# Streamlit App
st.title("Skymod Linkedin Veri Analizi")

uploaded_file = st.file_uploader("Upload Excel File", type=["xls", "xlsx"])

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("Data Preview:")
    st.write(data)

    visitor_numeric_columns = [
    'Sayfa görüntülemeleri genel bakış (toplam)',
    'Tekil ziyaretçiler genel bakış (toplam)',
    'İş ilanları sayfası görüntülemeleri (toplam)',
    'İş ilanları tekil ziyaretçiler (toplam)',
    'Toplam sayfa görüntülemeleri (toplam)',
    'Toplam tekil ziyaretçiler (toplam)',
    'Toplam görüntülemeler (Konum)',
    'Toplam görüntülemeler (İş_alanı)',
    'Toplam görüntülemeler (Kıdem)',
    'Toplam görüntülemeler Sektör (Şirket büyüklüğü)'
]

    visitor_categorical_columns = [
    'Konum',
    'İş alanı',
    'Kıdem',
    'Sektör',
    'Şirket büyüklüğü'
]

    follower_numeric_columns = [
    'Tarih',
    'Toplam Takipçi',
    'Toplam takipçi (Konum)',
    'Toplam takipçi (İş alanı)',
    'Toplam takipçi (Kıdem)',
    'Toplam takipçi (Sektör)',
    'Toplam takipçi (Şirket büyüklüğü)'
    ]
    follower_categorical_columns = [
    'Konum',
    'Toplam görüntülemeler Konum',
    'İş alanı',
    'Kıdem',
    'Sektör',
    'Şirket büyüklüğü'
    ]

    content_stats_columns = [
        'Tarih',
        'Görüntülenmeler (toplam)',
        'Tıklamalar (toplam)',
        'Reaksiyonlar (toplam)',
        'Yorumlar (toplam)',
        'Yeniden yayınlamalar (toplam)',
        'Sitede kalma oranı (toplam)'
    ]
    content_title_column = 'Gönderi başlığı'

    content_numeric_columns = [
    'Görüntülenme',
    'Tıklama Oranı (CTR)',
    'Beğenmeler',
    'Yorumlar',
    'Yeniden paylaşımlar',
    'Etkileşim oranı'
    ]
    content_categorical_columns = [
    'İçerik Türü'
    ]

    # Determine insight type based on columns present in uploaded file
    columns_lower = [col.lower() for col in data.columns]

    if any('toplam takipçi' in col for col in columns_lower):
        insight_type = "Follower Insights"
        numeric_columns = follower_numeric_columns
        categorical_columns = follower_categorical_columns
    elif any('toplam görüntülemeler' in col for col in columns_lower):
        insight_type = "Visitor Insights"
        numeric_columns = visitor_numeric_columns
        categorical_columns = visitor_categorical_columns
    else:
        insight_type = "Content Insights"
        numeric_columns = content_numeric_columns
        categorical_columns = content_categorical_columns

    # Select Chart Type
    chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])

    # Select Numeric and Categorical Columns
    numeric_column = st.selectbox("Select Numeric Column", numeric_columns)
    categorical_column = st.selectbox("Select Categorical Column", categorical_columns)

    # Generate and Display Chart
    if st.button("Generate Chart"):
        if chart_type == 'Bar Chart' or chart_type == 'Line Chart':
            generate_chart(data, chart_type, x_column=categorical_column, y_column=numeric_column)
        elif chart_type == 'Pie Chart':
            generate_chart(data, chart_type, x_column=categorical_column)

    # Allow user to download analysis
    st.download_button(
        label="Download Data as CSV",
        data=data.to_csv(index=False).encode('utf-8'),
        file_name=f'{insight_type.lower().replace(" ", "_")}_insights_analysis.csv',
        mime='text/csv',
    )
