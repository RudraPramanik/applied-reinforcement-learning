# Applied Reinforcement Learning & Industrial Research Projects

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Gymnasium-green)](https://gymnasium.farama.org/)

This repository is a comprehensive collection of **Reinforcement Learning (RL)** implementations, ranging from fundamental algorithms to advanced research projects focused on industrial applications and independent research of Rudra Pramanik

## 🌟 Applied Research Projects
These notebooks represent the research projects and experiment by Rudra and team, applying RL and ML to solve high-impact, real-world problems.

| Project | Description | Key Technologies | Link |
| :--- | :--- | :--- | :--- |
| **Supply Chain RL** | Optimizing inventory levels across multi-echelon supply chains to minimize bullwhip effects. | Deep Q-Learning, Inventory Management | [Explore](./supply-chain-rl/Reinforcement-Learning-SupplyChain.ipynb) |
| **Dynamic Pricing** | Real-time price optimization based on stochastic demand forecasting and market trends. | Contextual Bandits, Demand Modeling | [Explore](./supply-chain-rl/Dynamic_pricing_demand_forecasting_reinforcement_learning.ipynb) |
| **Anomaly Detection** | Monitoring industrial sensor data for predictive maintenance and fault detection. | Time-Series Analysis, LSTMs/ML | [Explore](./system%20and%20manufactureing/Anomaly_detection_time_series.ipynb) |
| **EV Battery Health** | Predicting State-of-Health (SoH) and degradation patterns in Electric Vehicle batteries. | Predictive Modeling, Battery Science | [Explore](./system%20and%20manufactureing/ml_ev_battery_degradation.ipynb) |

---

## 📚 Foundational RL (Sutton & Barto)
This section implements the core concepts from the gold standard textbook: *Reinforcement Learning: An Introduction*.

* **Chapter 02:** [Multi-Armed Bandits](./Chapter%2002%20-%20Multi-Armed%20Bandits) - Exploration vs. Exploitation.
* **Chapter 04:** [Dynamic Programming](./Chapter%2004%20-%20Dynamic%20Programming) - Policy/Value Iteration.
* **Chapter 06:** [Temporal Difference](./Chapter%2006%20-%20Temporal%20Difference%20Learning) - SARSA, Q-Learning, and Expected SARSA.
* **Chapter 08:** [Dyna-Q](./Chapter%2008%20-%20Planning%20and%20Learning%20with%20Tabular%20Methods) - Integrating planning and learning.
* **Chapter 13:** [Policy Gradients](./Chapter%2013%20-%20Policy%20Gradient%20Methods) - REINFORCE and Actor-Critic models.

---

## 🛠 Project Overviews

### 📦 Supply Chain Optimization
Addresses the challenge of ordering the right amount of stock at the right time. By modeling the supply chain as an MDP, the agent learns to balance storage costs against the risk of stockouts.

### 💰 Dynamic Pricing & Forecasting
Focused on maximizing revenue in a competitive market. The agent learns the price-demand curve dynamically, allowing it to adjust prices in response to consumer behavior changes.

### 🏭 Manufacturing Anomaly Detection
Uses time-series data from factory equipment to identify "out-of-distribution" patterns. This research is vital for reducing downtime in smart manufacturing environments.

### 🔋 EV Battery Degradation
Investigates how charging cycles affect battery life. This project uses machine learning to estimate degradation, providing a foundation for RL-based smart charging strategies.

---

## ⚙️ Getting Started

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/RudraPramanik/applied-reinforcement-learning.git](https://github.com/RudraPramanik/applied-reinforcement-learning.git)
