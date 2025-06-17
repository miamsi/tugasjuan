dset = pd.read_csv("data.csv", header=0, sep=',', low_memory=False)
dset = dset.astype(object)
coltodrop = ['province_id', 'city_id', 'district_id', 'npsn', 'street_name', 'lat', 'long']
dset.drop(columns=coltodrop, inplace=True)

#Header
st.title('Data Jumlah Sekolah di Indonesia')

# Use segmented control for multi-select columns
group_cols = st.segmented_control(
    "Select columns to display:",
    options=dset.columns.tolist(),
    selection_mode="multi"
)


#display the filtered
if group_cols:
    # Group by selected columns and get group sizes
    grouped = dset.groupby(group_cols).size().reset_index(name='Jumlah')
    st.dataframe(grouped, hide_index=True)
    
else:
    st.dataframe(dset, hide_index=True)
 
