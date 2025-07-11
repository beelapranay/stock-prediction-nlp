# News-Driven Sentiment Trading Pipeline

An end-to-end Python project that ingests financial news headlines, scores them with FinBERT, detects market regimes via a Gaussian HMM, trains a logistic-regression predictor (~70% directional accuracy), and optimizes an automated trading strategy with PPO in a custom Gym environment.

## 📂 Repository Contents

- **final_master.ipynb**  
  Main Jupyter notebook with full implementation and analysis  
- **NVDA.csv**, **MU.csv**, **MRK.csv**, **MS.csv**  
  Historical daily open/close price data for each ticker

## ⚙️ Environment Setup

### 1. Install Dependencies

<pre markdown> bash pip install pandas regex kagglehub tqdm transformers torch numpy
 hmmlearn scikit-learn matplotlib seaborn gym stable-baselines3 </pre>

## 2. Prepare Workspace

Place these CSVs alongside `final_master.ipynb`:

- `NVDA.csv`
- `MU.csv`
- `MRK.csv`
- `MS.csv`

> **Note:** The KaggleHub integration in the notebook will auto-download the news dataset.

---

## ▶️ Running the Notebook

1. Open `final_master.ipynb` in JupyterLab, VS Code, or another IDE.  
2. Run all cells in order.  
3. The notebook will:
   - Download & filter news headlines  
   - Merge headlines with price data  
   - Score sentiment via FinBERT  
   - Detect “calm” vs. “volatile” regimes with HMM  
   - Train a logistic-regression classifier  
   - Wrap test data in a custom Gym env and train multiple PPO agents  
   - Select & evaluate the best policy  


## 📝 Paper Trading with Alpaca

To place real paper trades using the PPO agent, install Alpaca's SDK:

```bash
pip install alpaca-trade-api
```

Set your Alpaca API key and secret in `alpaca_paper_trade.py`. The script defines an `AlpacaPaperTrader` helper used by the environment. When the agent goes long or short, an order will be submitted to the Alpaca paper endpoint.

See the comments in `alpaca_paper_trade.py` for details.

