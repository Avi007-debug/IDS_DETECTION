import React, { useState, useEffect } from 'react';
import { Shield, Activity, Share2, AlertTriangle, CheckCircle2, Server, Terminal } from 'lucide-react';
import Threats from './Threats';
import './App.css';

const API_BASE = 'http://127.0.0.1:8000';

function App() {
  const [currentPage, setCurrentPage] = useState('dashboard');
  const [detections, setDetections] = useState([]);
  const [stats, setStats] = useState({
    totalPackets: 0,
    attacksDetected: 0,
    health: 100
  });

  const fetchDetections = async () => {
    try {
      const response = await fetch(`${API_BASE}/detections`);
      const data = await response.json();
      setDetections(data.reverse()); // Newest first

      const attacks = data.filter(d => d.is_attack).length;
      setStats({
        totalPackets: data.length,
        attacksDetected: attacks,
        health: data.length > 0 ? Math.max(0, 100 - (attacks / data.length) * 100).toFixed(1) : 100
      });
    } catch (error) {
      console.error('Error fetching detections:', error);
    }
  };

  useEffect(() => {
    if (currentPage === 'dashboard') {
      fetchDetections();
      const interval = setInterval(fetchDetections, 2000);
      return () => clearInterval(interval);
    }
  }, [currentPage]);

  if (currentPage === 'threats') {
    return (
      <div>
        <nav className="nav-bar">
          <button onClick={() => setCurrentPage('dashboard')} className="nav-btn">
            📊 Dashboard
          </button>
          <button onClick={() => setCurrentPage('threats')} className="nav-btn active">
            🚨 Threats
          </button>
        </nav>
        <Threats />
      </div>
    );
  }

  return (
    <div>
      <nav className="nav-bar">
        <button onClick={() => setCurrentPage('dashboard')} className="nav-btn active">
          📊 Dashboard
        </button>
        <button onClick={() => setCurrentPage('threats')} className="nav-btn">
          🚨 Threats
        </button>
      </nav>
      <div className="dashboard">
      <header className="dashboard-header">
        <div className="title-group">
          <h1>AI-Driven Intrusion Detection System</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem' }}>Real-time Network Monitoring & AI Remediation</p>
        </div>
        <div className="status-badge">
          <div className="pulse"></div>
          <span>IDS Sensor Active</span>
        </div>
      </header>

      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-label">System Health</div>
          <div className="stat-value" style={{ color: stats.health > 90 ? 'var(--accent-green)' : 'var(--accent-red)' }}>
            {stats.health}%
          </div>
          <Activity size={24} style={{ marginTop: '0.5rem', opacity: 0.5 }} />
        </div>
        <div className="stat-card">
          <div className="stat-label">Total Flows Analyzed</div>
          <div className="stat-value">{stats.totalPackets}</div>
          <Server size={24} style={{ marginTop: '0.5rem', opacity: 0.5, color: 'var(--accent-blue)' }} />
        </div>
        <div className="stat-card">
          <div className="stat-label">Attacks Blocked</div>
          <div className="stat-value" style={{ color: stats.attacksDetected > 0 ? 'var(--accent-red)' : 'inherit' }}>
            {stats.attacksDetected}
          </div>
          <Shield size={24} style={{ marginTop: '0.5rem', opacity: 0.5, color: 'var(--accent-red)' }} />
        </div>
      </div>

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Network Flow (Src → Dst)</th>
              <th>Protocol</th>
              <th>IDS Result</th>
              <th>AI Suggestion</th>
            </tr>
          </thead>
          <tbody>
            {detections.length === 0 ? (
              <tr>
                <td colSpan="5" className="empty-state">
                  <Terminal size={48} style={{ marginBottom: '1rem', opacity: 0.2 }} />
                  <p>Monitoring network traffic... No flows detected yet.</p>
                </td>
              </tr>
            ) : (
              detections.map((d, i) => (
                <tr key={i}>
                  <td>{d.timestamp.split(' ')[1]}</td>
                  <td>
                    <div className="ip-flow">
                      <span title={`${d.src_ip}:${d.src_port}`}>{d.src_ip}</span>
                      <Share2 size={12} style={{ opacity: 0.3 }} />
                      <span title={`${d.dst_ip}:${d.dst_port}`}>
                        {d.dst_ip} <strong style={{ color: 'var(--accent-blue)' }}>:{d.dst_port}</strong>
                      </span>
                    </div>
                  </td>
                  <td>{d.protocol}</td>
                  <td>
                    <span className={`attack-pill ${d.is_attack ? 'is-attack' : 'is-normal'}`}>
                      {d.is_attack ? (
                        <><AlertTriangle size={12} style={{ marginRight: '4px' }} /> {d.attack_type}</>
                      ) : (
                        <><CheckCircle2 size={12} style={{ marginRight: '4px' }} /> Benign</>
                      )}
                    </span>
                    <div style={{ fontSize: '10px', marginTop: '4px', opacity: 0.5 }}>
                      Conf: {(d.confidence * 100).toFixed(1)}%
                    </div>
                  </td>
                  <td>
                    <div className="suggestion-text">{d.suggestion}</div>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
    </div>
  );
}

export default App;
