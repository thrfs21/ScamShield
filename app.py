
import streamlit as st
import joblib

st.set_page_config(
    page_title="ScamShield",
    page_icon="🛡️",
    layout="centered"
)


@st.cache_resource
def load_model():
    return joblib.load("scamshield_model.joblib")


model = load_model()

st.title("🛡️ ScamShield")
st.subheader("Internship & Job Listing Risk Checker")

st.write(
    "Paste a job advertisement to check whether its content "
    "resembles postings labelled as fraudulent in our training data."
)

title = st.text_input("Job title")
company = st.text_area("Company profile or company details")
description = st.text_area("Job description")
requirements = st.text_area("Requirements")
benefits = st.text_area("Benefits and compensation")


if st.button("Analyse listing", type="primary"):

    combined_text = " ".join([
        title,
        company,
        description,
        requirements,
        benefits
    ]).strip()

    if not combined_text:
        st.warning("Please enter some job listing details.")

    else:
        # Machine learning prediction
        prediction = int(model.predict([combined_text])[0])

        st.markdown("### Machine Learning Prediction")

        if prediction == 1:
            st.error(
                "Potentially fraudulent — review carefully"
            )
        else:
            st.success(
                "Likely legitimate according to the model"
            )

        # Transparent text-based warning indicators
        warning_rules = {
            "Upfront payment request": [
                "registration fee",
                "training fee",
                "security deposit",
                "pay to apply",
                "payment required",
                "pay to secure",
                "immediate payment",
                "pay a fee",
                "processing fee",
                "application fee",
                "deposit required",
                "pay before joining"
            ],

            "Guaranteed outcome claims": [
                "guaranteed job",
                "guaranteed placement",
                "guaranteed income",
                "guaranteed selection",
                "100% placement",
                "guaranteed employment"
            ],

            "Urgency and pressure": [
                "apply immediately",
                "limited seats",
                "immediate confirmation",
                "act now",
                "urgent payment",
                "limited time",
                "hurry up"
            ]
        }

        text_lower = combined_text.lower()
        detected_warnings = []

        for category, phrases in warning_rules.items():

            matched = [
                phrase for phrase in phrases
                if phrase in text_lower
            ]

            if matched:
                detected_warnings.append({
                    "category": category,
                    "phrases": matched
                })

        st.markdown("### Risk Warning Indicators")

        if detected_warnings:
            for warning in detected_warnings:
                st.warning(
                    f"**{warning['category']}**: "
                    + ", ".join(warning["phrases"])
                )
        else:
            st.info(
                "No configured warning phrases were detected. "
                "This does not establish that the listing is safe."
            )

        # Final guidance
        st.markdown("### Safety Recommendation")

        if detected_warnings or prediction == 1:
            st.write(
                "Review the listing carefully. Verify the employer "
                "through its official website and independently "
                "confirm the contact details before proceeding."
            )
        else:
            st.write(
                "No configured warning indicators were detected, "
                "and the model did not classify the listing as "
                "fraudulent. Still verify the employer independently."
            )

        st.caption(
            "ScamShield is an educational screening tool. "
            "Its predictions and warning indicators are not proof "
            "of fraud or legitimacy. It cannot verify a company "
            "or replace independent checks."
        )
