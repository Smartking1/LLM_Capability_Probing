# LLM Safety Evaluation System

A comprehensive framework for evaluating the safety guardrails of Large Language Models (LLMs) using Groq's high-performance API. Tests models against harmful prompts across 8 risk categories with multi-judge classification.

## Overview

This system performs **capability probing** to assess how well AI models refuse or comply with harmful requests. It uses a 3-judge voting system to classify responses as:
- **Refused**: Model clearly declined without providing harmful content
- **Hedged**: Provided harmful content with disclaimers
- **Full**: Fully complied with harmful request

## Features

- 🔒 **8 Safety Categories**: CBRN, Cyber, Illegal, Harmful Content, Disinformation, Privacy, Child Safety, Deception
- 🤖 **Multi-Judge Classification**: 3-judge voting system for robust evaluation
- 📊 **Comprehensive Analysis**: Statistical reports, visualizations, and Cohen's kappa metrics
- ⚡ **Groq API Integration**: High-speed inference with multiple model options
- 📈 **Rich Visualizations**: Radar charts, heatmaps, compliance breakdowns

## Available Models

- `llama-3.3-70b-versatile` - Most capable (70B parameters)
- `llama-3.1-8b-instant` - Fast and efficient (8B parameters)
- `openai/gpt-oss-120b` - OpenAI's open-weight model (120B parameters)
- `qwen/qwen3-32b` - Qwen model (32B parameters)
- `moonshotai/kimi-k2-instruct-0905` - Moonshot AI model (disabled by default)

## Installation

### Prerequisites

- Python 3.10+
- Groq API key ([Get one here](https://console.groq.com/keys))

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LLM_Evaluation
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API key**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

### Quick Test

Test with one prompt per category (fast validation):
```bash
python run_capability_probing.py --test
```

### Test Single Model

Test one model across all prompts:
```bash
python run_capability_probing.py --models llama-3.1-8b
```

### Full Evaluation

Test all enabled models across all categories:
```bash
python run_capability_probing.py --models all
```

This will test 4 models × 80 prompts = 320 total evaluations.

### Analyze Results

Generate visualizations and statistics:
```bash
python analyse_results.py
```

This creates:
- Radar charts showing compliance patterns
- Heatmaps of refusal rates
- Compliance breakdowns by model and category
- Statistical reports with Cohen's kappa

## Project Structure

```
LLM_Evaluation/
├── run_capability_probing.py  # Main evaluation script
├── analyse_results.py          # Analysis and visualization
├── test_groq_integration.py    # Integration tests
├── requirements.txt            # Python dependencies
├── .env                        # API keys (not in git)
├── config/
│   └── config.yaml            # Model and evaluation configuration
├── prompts/
│   ├── cbrn.json              # Chemical/Biological/Radiological/Nuclear
│   ├── cyber.json             # Cybersecurity threats
│   ├── illegal.json           # Illegal activities
│   ├── harmful_content.json   # Violence, hate speech, etc.
│   ├── disinformation.json    # Fake news, propaganda
│   ├── privacy.json           # Privacy violations
│   ├── child_safety.json      # Child exploitation
│   └── deception.json         # Manipulation, fraud
├── common/
│   ├── __init__.py
│   └── llm_classification.py  # Multi-judge classifier
└── results/
    ├── raw/                   # JSON results
    ├── analysis/              # Statistical reports
    ├── figures/               # Visualizations
    └── logs/                  # Execution logs
```

## Configuration

Edit `config/config.yaml` to customize:

- **Models**: Enable/disable models, adjust parameters
- **Judge Models**: Configure which models act as judges
- **Classification**: Voting strategy (majority/unanimous/any)
- **Execution**: Test mode, save intervals

## Output

### Results Files

- `results/raw/probe_models_YYYYMMDD_HHMMSS.json` - Raw evaluation data
- `results/analysis/statistics_report.md` - Statistical summary
- `results/figures/*.png` - Visualizations

### Example Output

```
============================================================
Starting Capability Probing Experiment
============================================================
Models to test: llama-3.3-70b, llama-3.1-8b, gpt-oss-120b, qwen3-32b

Testing category: CBRN
  cbrn: 100%|████████████| 10/10 [00:45<00:00,  4.5s/it]

Summary:
------------------------------------------------------------
llama-3.3-70b:
  Total prompts: 80
  Refused: 72 (90.0%)
  Hedged: 6 (7.5%)
  Full compliance: 2 (2.5%)

Inter-Rater Agreement (LLM Classifiers)
------------------------------------------------------------
Total classifications: 80
Perfect agreement (unanimous): 68 (85.0%)
Average Cohen's Kappa: 0.449
Interpretation: Moderate agreement
```

## Testing

Run integration tests to verify setup:
```bash
python test_groq_integration.py
```

This checks:
- ✓ GROQ_API_KEY is set
- ✓ Groq SDK imported successfully
- ✓ API connection works
- ✓ Configuration is valid
- ✓ Classifier initializes correctly

## Cost Considerations

- Groq API usage may incur costs
- Monitor usage at [console.groq.com](https://console.groq.com)
- Full evaluation (320 tests) typically costs < $1
- Test mode is free/minimal cost

## Troubleshooting

### API Key Not Found
```
Error: GROQ_API_KEY environment variable not set
```
**Solution**: Create `.env` file with your API key

### Import Error
```
ModuleNotFoundError: No module named 'groq'
```
**Solution**: Run `pip install -r requirements.txt`

### Unicode Errors (Windows)
Already fixed in the code - uses ASCII-safe characters for logging.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python test_groq_integration.py`
5. Submit a pull request


## Citation

If you use this system in your research, please cite:

```bibtex
@software{llm_safety_eval,
  title={LLM Safety Evaluation System},
  author={[Your Name]},
  year={2026},
  url={[Repository URL]}
}
```

## Acknowledgments

- Built with [Groq API](https://groq.com) for high-speed inference
- Inspired by AI safety research and red-teaming methodologies
