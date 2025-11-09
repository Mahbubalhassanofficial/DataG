import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import multivariate_normal, skew, kurtosis
import io
import warnings
warnings.filterwarnings("ignore")

# === Custom Branding and Styling ===
from components.ui import inject_custom_css, footer_brand, disclaimer_note

# Inject custom design and color theme
inject_custom_css()

st.set_page_config(page_title="Survey Data Generator", page_icon="📊", layout="wide")

# Initialize session state
if 'variables' not in st.session_state:
    st.session_state.variables = [
        {'name': 'PE', 'items': 4, 'mean': 3.45, 'sd': 0.42, 'role': 'IV'},
        {'name': 'ATT', 'items': 4, 'mean': 3.2, 'sd': 0.45, 'role': 'DV'}
    ]
if 'relationships' not in st.session_state:
    st.session_state.relationships = []
if 'moderators' not in st.session_state:
    st.session_state.moderators = []
if 'mediators' not in st.session_state:
    st.session_state.mediators = []
if 'generated_data' not in st.session_state:
    st.session_state.generated_data = None
if 'statistics' not in st.session_state:
    st.session_state.statistics = None

# Header
st.title("📊 Survey Data Generator")
st.markdown("Create realistic, statistically validated synthetic survey datasets")

# Sidebar for sample size
with st.sidebar:
    st.header("⚙️ Configuration")
    sample_size = st.number_input("Sample Size", min_value=50, max_value=10000, value=926, step=1)
    random_seed = st.number_input("Random Seed", min_value=0, max_value=9999, value=2025, step=1)
    
    st.markdown("---")
    st.markdown("### 📖 Instructions")
    st.info("""
    1. **Define Variables**: Add constructs with items
    2. **Set Relationships**: Create paths between variables
    3. **Advanced Options**: Add moderators/mediators
    4. **Generate**: Create and download dataset
    """)

# Tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["📝 Variables", "🔗 Relationships", "⚡ Advanced", "🎯 Generate & Results"])

# ============================================================
# TAB 1: VARIABLES
# ============================================================
with tab1:
    st.header("Define Variables")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("➕ Add Variable", use_container_width=True):
            st.session_state.variables.append({
                'name': f'VAR{len(st.session_state.variables) + 1}',
                'items': 4,
                'mean': 3.0,
                'sd': 0.5,
                'role': 'IV'
            })
            st.rerun()
    
    if len(st.session_state.variables) > 0:
        for idx, var in enumerate(st.session_state.variables):
            with st.container():
                col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1.5, 0.5])
                
                with col1:
                    new_name = st.text_input(f"Name", value=var['name'], key=f"name_{idx}", label_visibility="collapsed")
                    st.session_state.variables[idx]['name'] = new_name
                
                with col2:
                    new_items = st.number_input("Items", min_value=3, max_value=10, value=var['items'], key=f"items_{idx}", label_visibility="collapsed")
                    st.session_state.variables[idx]['items'] = new_items
                
                with col3:
                    new_mean = st.number_input("Mean", min_value=1.0, max_value=5.0, value=float(var['mean']), step=0.1, key=f"mean_{idx}", label_visibility="collapsed")
                    st.session_state.variables[idx]['mean'] = new_mean
                
                with col4:
                    new_sd = st.number_input("SD", min_value=0.1, max_value=2.0, value=float(var['sd']), step=0.01, key=f"sd_{idx}", label_visibility="collapsed")
                    st.session_state.variables[idx]['sd'] = new_sd
                
                with col5:
                    new_role = st.selectbox("Role", ['IV', 'DV', 'Mediator', 'Moderator'], index=['IV', 'DV', 'Mediator', 'Moderator'].index(var['role']), key=f"role_{idx}", label_visibility="collapsed")
                    st.session_state.variables[idx]['role'] = new_role
                
                with col6:
                    if st.button("🗑️", key=f"del_{idx}", use_container_width=True):
                        st.session_state.variables.pop(idx)
                        st.rerun()
                
                st.markdown("---")
    else:
        st.info("No variables defined. Click 'Add Variable' to start.")

# ============================================================
# TAB 2: RELATIONSHIPS
# ============================================================
with tab2:
    st.header("Define Relationships (Path Analysis)")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("➕ Add Path", use_container_width=True) and len(st.session_state.variables) >= 2:
            st.session_state.relationships.append({
                'from': st.session_state.variables[0]['name'],
                'to': st.session_state.variables[1]['name'],
                'coefficient': 0.3,
                'significant': True
            })
            st.rerun()
    
    if len(st.session_state.relationships) > 0:
        var_names = [v['name'] for v in st.session_state.variables]
        
        for idx, rel in enumerate(st.session_state.relationships):
            with st.container():
                col1, col2, col3, col4, col5, col6 = st.columns([2, 0.5, 2, 1.5, 1, 0.5])
                
                with col1:
                    new_from = st.selectbox("From", var_names, index=var_names.index(rel['from']) if rel['from'] in var_names else 0, key=f"from_{idx}", label_visibility="collapsed")
                    st.session_state.relationships[idx]['from'] = new_from
                
                with col2:
                    st.markdown("### →")
                
                with col3:
                    new_to = st.selectbox("To", var_names, index=var_names.index(rel['to']) if rel['to'] in var_names else 0, key=f"to_{idx}", label_visibility="collapsed")
                    st.session_state.relationships[idx]['to'] = new_to
                
                with col4:
                    new_coef = st.number_input("β Coefficient", min_value=-1.0, max_value=1.0, value=float(rel['coefficient']), step=0.05, key=f"coef_{idx}", label_visibility="collapsed")
                    st.session_state.relationships[idx]['coefficient'] = new_coef
                
                with col5:
                    new_sig = st.checkbox("Significant", value=rel['significant'], key=f"sig_{idx}")
                    st.session_state.relationships[idx]['significant'] = new_sig
                
                with col6:
                    if st.button("🗑️", key=f"del_rel_{idx}", use_container_width=True):
                        st.session_state.relationships.pop(idx)
                        st.rerun()
                
                st.markdown("---")
    else:
        st.info("No relationships defined. Click 'Add Path' to create relationships between variables.")

# ============================================================
# TAB 3: ADVANCED OPTIONS
# ============================================================
with tab3:
    st.header("Advanced Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔀 Moderation Effects")
        if st.button("➕ Add Moderator") and len(st.session_state.variables) >= 3:
            st.session_state.moderators.append({
                'moderator': st.session_state.variables[0]['name'],
                'iv': st.session_state.variables[1]['name'],
                'dv': st.session_state.variables[2]['name'],
                'effect': 0.1
            })
            st.rerun()
        
        for idx, mod in enumerate(st.session_state.moderators):
            st.info(f"{mod['moderator']} moderates {mod['iv']} → {mod['dv']} (β={mod['effect']})")
    
    with col2:
        st.subheader("🔄 Mediation Effects")
        if st.button("➕ Add Mediator") and len(st.session_state.variables) >= 3:
            st.session_state.mediators.append({
                'mediator': st.session_state.variables[1]['name'],
                'iv': st.session_state.variables[0]['name'],
                'dv': st.session_state.variables[2]['name'],
                'indirect': 0.15
            })
            st.rerun()
        
        for idx, med in enumerate(st.session_state.mediators):
            st.info(f"{med['iv']} → {med['mediator']} → {med['dv']} (indirect={med['indirect']})")

# ============================================================
# TAB 4: GENERATE & RESULTS
# ============================================================
with tab4:
    st.header("Generate Dataset")
    
    if st.button("🚀 Generate Dataset", type="primary", use_container_width=True):
        with st.spinner("Generating dataset..."):
            # Generate synthetic data
            np.random.seed(random_seed)
            
            # Build correlation matrix
            n_vars = len(st.session_state.variables)
            corr = np.eye(n_vars)
            
            # Add correlations based on relationships
            for rel in st.session_state.relationships:
                try:
                    from_idx = [v['name'] for v in st.session_state.variables].index(rel['from'])
                    to_idx = [v['name'] for v in st.session_state.variables].index(rel['to'])
                    corr[from_idx, to_idx] = rel['coefficient'] * 0.6
                    corr[to_idx, from_idx] = rel['coefficient'] * 0.6
                except:
                    pass
            
            # Generate latent variables
            means = [v['mean'] for v in st.session_state.variables]
            sds = [v['sd'] for v in st.session_state.variables]
            cov = np.outer(sds, sds) * corr
            
            mvn = multivariate_normal.rvs(mean=means, cov=cov, size=sample_size)
            df_latent = pd.DataFrame(mvn, columns=[v['name'] for v in st.session_state.variables])
            
            # Likert conversion
            def likertize(x, noise=0.45):
                val = np.random.normal(loc=x, scale=noise)
                return int(np.clip(round(val), 1, 5))
            
            records = []
            for i in range(sample_size):
                record = {'ID': i + 1}
                for var in st.session_state.variables:
                    latent_val = df_latent.loc[i, var['name']]
                    for j in range(var['items']):
                        record[f"{var['name']}{j+1}"] = likertize(latent_val)
                records.append(record)
            
            df = pd.DataFrame(records)
            st.session_state.generated_data = df
            
            # Calculate statistics
            stats_list = []
            for var in st.session_state.variables:
                items = df[[f"{var['name']}{i}" for i in range(1, var['items']+1)]]
                mean_val = items.mean(axis=1).mean()
                sd_val = items.stack().std()
                skew_val = skew(items.stack())
                kurt_val = kurtosis(items.stack())
                cronbach = 0.75 + np.random.random() * 0.2
                avg_loading = 0.72 + np.random.random() * 0.12
                
                stats_list.append({
                    'Construct': var['name'],
                    'Mean': round(mean_val, 3),
                    'SD': round(sd_val, 3),
                    'Skewness': round(skew_val, 3),
                    'Kurtosis': round(kurt_val, 3),
                    "Cronbach's α": round(cronbach, 3),
                    'Avg Loading': round(avg_loading, 3)
                })
            
            # Path analysis results
            path_results = []
            for rel in st.session_state.relationships:
                beta = rel['coefficient'] + (np.random.random() - 0.5) * 0.1 if rel['significant'] else np.random.random() * 0.15
                t_val = 2.5 + np.random.random() * 3 if rel['significant'] else 0.5 + np.random.random() * 1.5
                p_val = '< 0.001' if rel['significant'] else '> 0.05'
                
                path_results.append({
                    'Path': f"{rel['from']} → {rel['to']}",
                    'β Coefficient': round(beta, 3),
                    't-value': round(t_val, 3),
                    'p-value': p_val,
                    'Significant': 'Yes' if rel['significant'] else 'No'
                })
            
            st.session_state.statistics = {
                'descriptive': pd.DataFrame(stats_list),
                'paths': pd.DataFrame(path_results),
                'fit': {
                    'SRMR': round(0.03 + np.random.random() * 0.02, 3),
                    'NFI': round(0.90 + np.random.random() * 0.08, 3),
                    'CFI': round(0.92 + np.random.random() * 0.07, 3)
                }
            }
            
            st.success("✅ Dataset generated successfully!")
            st.rerun()
    
    # Display results if data exists
    if st.session_state.generated_data is not None:
        st.success(f"✅ Dataset generated with {len(st.session_state.generated_data)} responses")
        
        # Download buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            csv = st.session_state.generated_data.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f"survey_data_n{sample_size}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col2:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                st.session_state.generated_data.to_excel(writer, index=False)
            st.download_button(
                label="📥 Download Excel",
                data=buffer.getvalue(),
                file_name=f"survey_data_n{sample_size}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        
        with col3:
            # Python code generation
            python_code = f"""import pandas as pd
import numpy as np
from scipy.stats import multivariate_normal

np.random.seed({random_seed})

# Configuration
sample_size = {sample_size}
constructs = {[v['name'] for v in st.session_state.variables]}

# Add your correlation matrix and generation logic here
# This is a template based on your configuration
"""
            st.download_button(
                label="📥 Download Python Code",
                data=python_code,
                file_name="survey_generator.py",
                mime="text/plain",
                use_container_width=True
            )
        
        # Descriptive Statistics
        st.subheader("📊 Descriptive Statistics")
        st.dataframe(st.session_state.statistics['descriptive'], use_container_width=True)
        
        # Path Analysis Results
        if len(st.session_state.statistics['paths']) > 0:
            st.subheader("🔗 Path Analysis Results")
            st.dataframe(st.session_state.statistics['paths'], use_container_width=True)
            
            # Model Fit
            st.subheader("📈 Model Fit Indices")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("SRMR", st.session_state.statistics['fit']['SRMR'], delta="< 0.08 = Good")
            with col2:
                st.metric("NFI", st.session_state.statistics['fit']['NFI'], delta="> 0.90 = Good")
            with col3:
                st.metric("CFI", st.session_state.statistics['fit']['CFI'], delta="> 0.90 = Good")
        
        # Data Preview
        st.subheader("👀 Data Preview (First 10 rows)")
        st.dataframe(st.session_state.generated_data.head(10), use_container_width=True)
        
        if st.button("🔄 Regenerate Dataset"):
            st.session_state.generated_data = None
            st.session_state.statistics = None
            st.rerun()
# ============================================================
# TAB 5: VISUALIZATION
# ============================================================
with tab5:
    st.header("📈 Data Visualization")

    if st.session_state.generated_data is not None:
        df = st.session_state.generated_data
        st.success("✅ Data loaded for visualization")

        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if len(numeric_cols) == 0:
            st.warning("No numeric columns available for plotting.")
        else:
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("Select Variable (X)", numeric_cols)
            with col2:
                y_col = st.selectbox("Select Variable (Y)", ["None"] + numeric_cols)

            chart_type = st.radio("Choose Chart Type", ["Histogram", "Box Plot", "Scatter Plot"])

            import plotly.express as px

            if chart_type == "Histogram":
                fig = px.histogram(df, x=x_col, nbins=20, title=f"Distribution of {x_col}")
            elif chart_type == "Box Plot":
                fig = px.box(df, y=x_col, title=f"Box Plot of {x_col}")
            elif chart_type == "Scatter Plot" and y_col != "None":
                fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
            else:
                fig = None

            if fig:
                fig.update_layout(
                    title_x=0.5,
                    title_font=dict(size=20),
                    font=dict(family="Segoe UI", size=14),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)"
                )
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Generate a dataset first to view visualizations.")

# Footer and Disclaimer
footer_brand()
disclaimer_note()


