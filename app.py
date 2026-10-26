
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
    "Check a job or internship listing for potential fraud indicators."
)

# Sample listings for quick testing
samples = {
    "Select a sample...": {
        "title": "",
        "company": "",
        "description": "",
        "requirements": "",
        "benefits": ""
    },
    "Test 1 — Software Internship": {
        "title": "Software Development Intern",
        "company": "ABC Technologies is a software development company.",
        "description": (
            "Work with our engineering team to build web applications, "
            "write code, test features, and collaborate with developers."
        ),
        "requirements": (
            "Knowledge of Python, JavaScript, Git, and basic data structures."
        ),
        "benefits": "Mentorship, project experience, and a completion certificate."
    },
    "Test 2 — Upfront Payment": {
        "title": "Work From Home Internship",
        "company": "Online Career Solutions",
        "description": (
            "Pay a registration fee and security deposit to secure your "
            "internship position. Immediate payment is required."
        ),
        "requirements": "No experience required.",
        "benefits": "Guaranteed job after training."
    },
    "Test 3 — Vague Company Details": {
        "title": "Online Data Entry Executive",
        "company": "Best Company International",
        "description": (
            "Easy online work with high earnings. Apply now for this "
            "excellent opportunity. Details will be shared after selection."
        ),
        "requirements": "Anyone can apply.",
        "benefits": "High income and flexible working hours."
    },
    "Test 4 — Professional Listing": {
        "title": "Frontend Developer Intern",
        "company": (
            "We are a product development team building web applications "
            "for business customers."
        ),
        "description": (
            "Assist with React components, fix UI bugs, write tests, "
            "and participate in code reviews with senior developers."
        ),
        "requirements": (
            "Basic JavaScript, HTML, CSS, React fundamentals, and Git."
        ),
        "benefits": (
            "Mentorship, practical project experience, and regular feedback."
        )
    },
    "Test 5 — Training Fee and Guaranteed Placement": {
        "title": "Guaranteed Placement Training Internship",
        "company": "Future Career Academy",
        "description": (
            "Pay a training fee to secure your position. Guaranteed "
            "placement after training. Immediate payment is required "
            "to confirm your seat."
        ),
        "requirements": "Freshers can apply.",
        "benefits": "Guaranteed placement after paid training."
    }
}

# Select and load a sample
selected_sample = st.selectbox(
    "Quick test: choose a sample listing",
    list(samples.keys())
)

sample = samples[selected_sample]

title = st.text_input(
    "Job title",
    value=sample["title"],
    key=f"title_{selected_sample}"
)

company = st.text_area(
    "Company profile or company details",
    value=sample["company"],
    key=f"company_{selected_sample}"
)

description = st.text_area(
    "Job description",
    value=sample["description"],
    key=f"description_{selected_sample}"
)

requirements = st.text_area(
    "Requirements",
    value=sample["requirements"],
    key=f"requirements_{selected_sample}"
)

benefits = st.text_area(
    "Benefits and compensation",
    value=sample["benefits"],
    key=f"benefits_{selected_sample}"
)

if st.button("Analyse listing", type="primary"):

    combined_text = " ".join([
        title, company, description, requirements, benefits
    ]).strip()

    if not combined_text:
        st.warning("Please select a sample or enter listing details.")

    else:
        prediction = int(model.predict([combined_text])[0])

        st.markdown("### Machine Learning Prediction")

        if prediction == 1:
            st.error("Potentially fraudulent — review carefully")
        else:
            st.success("Likely legitimate according to the model")

        warning_rules = {
            "Upfront payment request": [
                "registration fee", "training fee", "security deposit",
                "pay to apply", "payment required", "pay to secure",
                "immediate payment", "pay a fee", "processing fee",
                "application fee", "deposit required", "pay before joining"
            ],
            "Guaranteed outcome claims": [
                "guaranteed job", "guaranteed placement",
                "guaranteed income", "guaranteed selection",
                "100% placement", "guaranteed employment"
            ],
            "Urgency and pressure": [
                "apply immediately", "limited seats",
                "immediate confirmation", "act now",
                "urgent payment", "limited time", "hurry up"
            ]
        }

        text_lower = combined_text.lower()
        detected_warnings = []

        for category, phrases in warning_rules.items():
            matched = [
                phrase for phrase in phrases if phrase in text_lower
            ]
            if matched:
                detected_warnings.append((category, matched))

        st.markdown("### Risk Warning Indicators")

        if detected_warnings:
            for category, phrases in detected_warnings:
                st.warning(f"**{category}:** " + ", ".join(phrases))
        else:
            st.info(
                "No configured warning phrases were detected. "
                "This does not mean the listing is safe."
            )

        st.markdown("### Safety Recommendation")

        if detected_warnings or prediction == 1:
            st.write(
                "Review this listing carefully. Verify the employer "
                "through its official website before proceeding."
            )
        else:
            st.write(
                "No configured warning indicators were detected, and "
                "the model did not classify this listing as fraudulent. "
                "Verify the employer independently."
            )

        st.caption(
            "Educational screening only. Predictions and warning "
            "indicators are not proof of fraud or legitimacy."
        )
