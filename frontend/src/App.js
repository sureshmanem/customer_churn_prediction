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
        <div style={{ minHeight: '100vh', background: 'linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <div style={{ maxWidth: 420, width: '100%', background: '#fff', boxShadow: '0 8px 32px rgba(60, 60, 120, 0.15)', borderRadius: 16, padding: 32 }}>
                <h1 style={{ textAlign: 'center', color: '#2d3a4a', marginBottom: 24 }}>Customer Churn Prediction</h1>
                <form onSubmit={handleSubmit}>
                    <div style={{ marginBottom: 16 }}>
                        <label style={{ fontWeight: 500, color: '#2d3a4a' }}>Name</label>
                        <input name="name" value={form.name} onChange={handleChange} required style={{ width: '100%', padding: 10, borderRadius: 8, border: '1px solid #d1d5db', marginTop: 4 }} />
                    </div>
                    <div style={{ marginBottom: 16 }}>
                        <label style={{ fontWeight: 500, color: '#2d3a4a' }}>Engagement Score</label>
                        <input name="engagement_score" type="number" value={form.engagement_score} onChange={handleChange} required style={{ width: '100%', padding: 10, borderRadius: 8, border: '1px solid #d1d5db', marginTop: 4 }} />
                    </div>
                    <div style={{ marginBottom: 16 }}>
                        <label style={{ fontWeight: 500, color: '#2d3a4a' }}>Claim Count</label>
                        <input name="claim_count" type="number" value={form.claim_count} onChange={handleChange} required style={{ width: '100%', padding: 10, borderRadius: 8, border: '1px solid #d1d5db', marginTop: 4 }} />
                    </div>
                    <div style={{ marginBottom: 24 }}>
                        <label style={{ fontWeight: 500, color: '#2d3a4a' }}>Payment History Score</label>
                        <input name="payment_history_score" type="number" value={form.payment_history_score} onChange={handleChange} required style={{ width: '100%', padding: 10, borderRadius: 8, border: '1px solid #d1d5db', marginTop: 4 }} />
                    </div>
                    <button type="submit" disabled={loading} style={{ width: '100%', padding: 12, borderRadius: 8, background: '#4f8cff', color: '#fff', fontWeight: 600, fontSize: 16, border: 'none', boxShadow: '0 2px 8px rgba(79,140,255,0.12)', cursor: 'pointer', transition: 'background 0.2s' }}>
                        {loading ? 'Predicting...' : 'Predict Churn Risk'}
                    </button>
                </form>
                {result !== null && (
                    <div style={{ marginTop: 32, textAlign: 'center' }}>
                        <h3 style={{ color: '#2d3a4a', marginBottom: 8 }}>Churn Risk Score:</h3>
                        <div style={{ fontSize: 32, fontWeight: 700, color: result > 0.5 ? '#e63946' : '#43aa8b' }}>{result}</div>
                        {/* Inference based on churn score */}
                        <div style={{ marginTop: 16, fontSize: 18, color: '#2d3a4a', fontWeight: 500 }}>
                            {typeof result === 'number' ? (
                                result > 0.8 ? 'High risk: This customer is very likely to churn. Immediate retention action recommended.' :
                                    result > 0.5 ? 'Moderate risk: This customer has a significant chance of churning. Consider engagement strategies.' :
                                        result > 0.3 ? 'Low risk: This customer is unlikely to churn, but periodic engagement is beneficial.' :
                                            'Very low risk: This customer is highly likely to stay.'
                            ) : result}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default App;
