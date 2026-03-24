import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Credit Risk Modelling", page_icon="📊", layout="wide")

# ─── FULL PAGE STYLES + ANIMATED BACKGROUND ────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=Syne:wght@700;800&display=swap');

/* ── Animated gradient background ── */
.stApp {
    background: linear-gradient(-45deg, #0d1b2a, #1b3a4b, #0a2342, #162d3d, #0d2137);
    background-size: 400% 400%;
    animation: gradientShift 12s ease infinite;
    font-family: 'Space Grotesk', sans-serif;
}

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── Floating orbs ── */
.orb-container {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.18;
    animation: floatOrb linear infinite;
}
.orb1 { width: 420px; height: 420px; background: #00d4ff; top: -100px; left: -80px; animation-duration: 20s; }
.orb2 { width: 300px; height: 300px; background: #ff6b35; bottom: 10%; right: -60px; animation-duration: 25s; animation-delay: -8s; }
.orb3 { width: 250px; height: 250px; background: #7c3aed; top: 40%; left: 30%; animation-duration: 18s; animation-delay: -4s; }

@keyframes floatOrb {
    0%   { transform: translateY(0px) scale(1); }
    33%  { transform: translateY(-40px) scale(1.05); }
    66%  { transform: translateY(20px) scale(0.95); }
    100% { transform: translateY(0px) scale(1); }
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; position: relative; z-index: 1; }

/* ── Main title ── */
.main-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    letter-spacing: -1px;
    background: linear-gradient(90deg, #00d4ff, #ffffff, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.2rem;
    animation: titlePulse 4s ease-in-out infinite;
}

@keyframes titlePulse {
    0%, 100% { filter: brightness(1); }
    50%       { filter: brightness(1.15); }
}

.sub-title {
    text-align: center;
    color: rgba(255,255,255,0.5);
    font-size: 0.95rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
}

/* ── Glass card ── */
.glass-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem 2rem 1.5rem;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
    margin-bottom: 1.5rem;
}

.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00d4ff;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #00d4ff33, transparent);
}

/* ── Inputs ── */
.stNumberInput > div > div > input,
.stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: white !important;
    font-family: 'Space Grotesk', sans-serif !important;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.stNumberInput > div > div > input:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 0 3px rgba(0,212,255,0.15) !important;
    outline: none !important;
}
.stSelectbox > div > div:hover {
    border-color: #00d4ff !important;
}

/* Labels */
label, .stNumberInput label, .stSelectbox label {
    color: rgba(255,255,255,0.75) !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
}

/* ── Predict button ── */
.stButton > button {
    background: linear-gradient(135deg, #00d4ff, #0099cc) !important;
    color: #0d1b2a !important;
    border: none !important;
    border-radius: 14px !important;
    height: 56px !important;
    width: 100% !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    font-family: 'Syne', sans-serif !important;
    letter-spacing: 1px !important;
    cursor: pointer !important;
    box-shadow: 0 4px 24px rgba(0,212,255,0.35) !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #33ddff, #00bbee) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(0,212,255,0.5) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Result panels ── */
.result-low {
    background: linear-gradient(135deg, rgba(16,185,129,0.2), rgba(5,150,105,0.1));
    border: 1.5px solid rgba(16,185,129,0.5);
    border-radius: 18px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 40px rgba(16,185,129,0.15);
    animation: resultFadeIn 0.6s ease forwards;
}
.result-high {
    background: linear-gradient(135deg, rgba(239,68,68,0.2), rgba(185,28,28,0.1));
    border: 1.5px solid rgba(239,68,68,0.5);
    border-radius: 18px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 40px rgba(239,68,68,0.15);
    animation: resultFadeIn 0.6s ease forwards;
}
.result-medium {
    background: linear-gradient(135deg, rgba(245,158,11,0.2), rgba(180,83,9,0.1));
    border: 1.5px solid rgba(245,158,11,0.5);
    border-radius: 18px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 40px rgba(245,158,11,0.15);
    animation: resultFadeIn 0.6s ease forwards;
}

@keyframes resultFadeIn {
    from { opacity: 0; transform: translateY(20px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}

.result-icon { font-size: 3.5rem; margin-bottom: 0.5rem; }
.result-label {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 0.4rem;
}
.result-prob {
    font-size: 2.5rem;
    font-weight: 700;
    letter-spacing: -1px;
}
.result-desc {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.6);
    margin-top: 0.5rem;
}

/* ── Score bar ── */
.score-bar-wrap {
    margin: 1.2rem auto 0;
    max-width: 340px;
}
.score-bar-track {
    background: rgba(255,255,255,0.1);
    border-radius: 50px;
    height: 10px;
    overflow: hidden;
}
.score-bar-fill {
    height: 100%;
    border-radius: 50px;
    transition: width 1s ease;
    animation: barGrow 1s ease forwards;
}

@keyframes barGrow {
    from { width: 0; }
}

/* ── Divider ── */
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    margin: 2rem 0;
}

/* ── Tooltip chips ── */
.chip {
    display: inline-block;
    background: rgba(0,212,255,0.12);
    border: 1px solid rgba(0,212,255,0.25);
    border-radius: 30px;
    padding: 2px 12px;
    font-size: 0.72rem;
    color: #00d4ff;
    margin: 2px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
</style>

<div class="orb-container">
  <div class="orb orb1"></div>
  <div class="orb orb2"></div>
  <div class="orb orb3"></div>
</div>
""", unsafe_allow_html=True)

# ─── TITLE ────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">Credit Risk Modelling</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">⬡ AI-Powered Default Probability Assessment ⬡</div>', unsafe_allow_html=True)

# Create rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the first row with default values
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

# Calculate Loan to Income Ratio and display it
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.markdown(
        f"<p style='color:white; font-size:20px;'> Loan-to-Income Ratio: {loan_to_income_ratio:.2f}</p>",
        unsafe_allow_html=True
    )  # Display as a text field

# Assign inputs to the remaining controls
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)


with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])


# Button to calculate risk
if st.button('Calculate Risk'):
    # Call the predict function from the helper module
    # print((age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
    #                                             delinquency_ratio, credit_utilization_ratio, num_open_accounts,
    #                                             residence_type, loan_purpose, loan_type))
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)

    # Display the results

    # ---------------- PROFESSIONAL METRICS CARDS ----------------
    col1, col2, col3 = st.columns(3, gap="large")

    # Rating colors
    rating_colors = {
        "Excellent": "#00E676",
        "Good": "#4CAF50",
        "Average": "#FFC107",
        "Poor": "#FF9800",
        "Bad": "#FF5252"
    }

    # Default Probability
    with col1:
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 20px;
            text-align: center;
            height: 130px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="color:#e5e7eb; font-size:13px;">📊 DEFAULT PROBABILITY</div>
            <div style="color:white; font-size:26px; font-weight:700;">
                {probability:.2%}
            </div>
            <div style="color:#94a3b8; font-size:11px;">
                Probability of Default
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Credit Score
    with col2:
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 20px;
            text-align: center;
            height: 130px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="color:#e5e7eb; font-size:13px;">💳 CREDIT SCORE</div>
            <div style="
                font-size:28px;
                font-weight:800;
                background: linear-gradient(45deg, #4ade80, #22c55e);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            ">
                {credit_score}
            </div>
            <div style="color:#94a3b8; font-size:11px;">
                Score
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Rating (FIXED)
    rating_color = rating_colors.get(rating, "#FF5252")

    with col3:
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 20px;
            text-align: center;
            height: 130px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="color:#e5e7eb; font-size:13px;">⭐ CREDIT RATING</div>
            <div style="
                font-size:24px;
                font-weight:800;
                color:{rating_color};
                text-shadow: 0 0 10px {rating_color};
            ">
                {rating}
            </div>
            <div style="color:#94a3b8; font-size:11px;">
                Risk Classification
            </div>
        </div>
        """, unsafe_allow_html=True)


