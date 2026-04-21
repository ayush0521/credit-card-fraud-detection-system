<h1 align="center">💳 Real-Time Credit Card Fraud Detection System</h1>

<p align="center">
  <b>Machine Learning • FastAPI • Streamlit • Explainable AI (SHAP)</b>
</p>

<hr>

<h2>📌 Project Overview</h2>
<p>
This project is an <b>end-to-end real-time fraud detection system</b> designed to identify fraudulent credit card transactions.
It simulates real-world transaction flow, processes data using a machine learning model, and provides predictions along with <b>explainable insights</b>.
</p>

<hr>

<h2>🚀 Key Features</h2>
<ul>
  <li>⚡ Real-time transaction simulation</li>
  <li>🤖 Machine Learning-based fraud detection</li>
  <li>🔌 FastAPI backend for prediction services</li>
  <li>📊 Interactive Streamlit dashboard</li>
  <li>🧠 Explainable AI using SHAP</li>
  <li>🚨 Fraud alerts and risk scoring</li>
</ul>

<hr>

<h2>🏗️ System Architecture</h2>
<pre>
Transaction Generator
        ↓
FastAPI Backend
        ↓
ML Model (XGBoost)
        ↓
SHAP Explainability
        ↓
Streamlit Dashboard
        ↓
Fraud Alerts
</pre>

<hr>

<h2>🛠️ Tech Stack</h2>

<table>
  <tr>
    <th>Layer</th>
    <th>Technology</th>
  </tr>
  <tr>
    <td>Machine Learning</td>
    <td>Scikit-learn, XGBoost</td>
  </tr>
  <tr>
    <td>Backend</td>
    <td>FastAPI</td>
  </tr>
  <tr>
    <td>Frontend</td>
    <td>Streamlit</td>
  </tr>
  <tr>
    <td>Data Processing</td>
    <td>Pandas, NumPy</td>
  </tr>
  <tr>
    <td>Explainability</td>
    <td>SHAP</td>
  </tr>
</table>

<hr>

<h2>📂 Project Structure</h2>

<pre>
credit-card-fraud-detection-system/
│
├── data/
├── notebooks/
├── models/
├── backend/
├── frontend/
├── simulation/
├── utils/
├── README.md
└── requirements.txt
</pre>

<hr>

<h2>⚙️ Installation</h2>

<pre>
git clone https://github.com/ayush0521/credit-card-fraud-detection-system.git
cd credit-card-fraud-detection-system
pip install -r requirements.txt
</pre>

<hr>

<h2>▶️ Usage</h2>

<p><b>Start Backend API:</b></p>
<pre>
uvicorn backend.app:app --reload
</pre>

<p><b>Start Frontend Dashboard:</b></p>
<pre>
streamlit run frontend/app.py
</pre>

<hr>

<h2>📊 Results & Metrics</h2>
<ul>
  <li>Precision & Recall optimized for fraud detection</li>
  <li>ROC-AUC evaluation</li>
  <li>Imbalanced data handling</li>
</ul>

<hr>

<h2>🔥 Unique Highlights</h2>
<ul>
  <li>End-to-end system (not just ML model)</li>
  <li>Real-time simulation of transactions</li>
  <li>Explainable predictions using SHAP</li>
  <li>API-based architecture</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>
<ul>
  <li>Kafka-based real-time streaming</li>
  <li>Cloud deployment (AWS/GCP)</li>
  <li>User authentication system</li>
  <li>Advanced anomaly detection models</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p>
Ayush Padmawar<br>
Machine Learning | Data Science | AI Enthusiast
</p>

<hr>

<p align="center">
⭐ If you like this project, consider giving it a star!
</p>
