import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [form, setForm] = useState({
        name: '',
        engagement_score: '',
        claim_count: '',
        payment_history_score: ''
    });
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const response = await axios.post('http://localhost:8000/predict', form);
            setResult(response.data.churn_risk);
        } catch (error) {
            setResult('Error: Could not get prediction');
        }
        setLoading(false);
    };

    return (
        <div style={{ maxWidth: 500, margin: '40px auto', padding: 20, border: '1px solid #eee', borderRadius: 8 }}>
            <h1>Customer Churn Prediction</h1>
            <form onSubmit={handleSubmit}>
                <label>Name:</label>
                <input name="name" value={form.name} onChange={handleChange} required style={{ width: '100%', marginBottom: 10 }} />
                <label>Engagement Score:</label>
                <input name="engagement_score" type="number" value={form.engagement_score} onChange={handleChange} required style={{ width: '100%', marginBottom: 10 }} />
                <label>Claim Count:</label>
                <input name="claim_count" type="number" value={form.claim_count} onChange={handleChange} required style={{ width: '100%', marginBottom: 10 }} />
                <label>Payment History Score:</label>
                <input name="payment_history_score" type="number" value={form.payment_history_score} onChange={handleChange} required style={{ width: '100%', marginBottom: 10 }} />
                <button type="submit" disabled={loading} style={{ width: '100%', padding: 10 }}>
                    {loading ? 'Predicting...' : 'Predict Churn Risk'}
                </button>
            </form>
            {result !== null && (
                <div style={{ marginTop: 20 }}>
                    <h3>Churn Risk Score:</h3>
                    <div style={{ fontSize: 24, color: result > 0.5 ? 'red' : 'green' }}>{result}</div>
                </div>
            )}
        </div>
    );
}

export default App;
