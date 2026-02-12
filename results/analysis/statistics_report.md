# Capability Probing Analysis Report

Total prompts analysed: 319
Models tested: 4
Harm categories: 8

## Overall Compliance Distribution

- refused: 297 (93.1%)
- hedged: 18 (5.64%)
- full: 4 (1.25%)

## Model Performance


### groq/llama-3.3-70b-versatile
- Total: 80
- Refused: 72 (90.0%)
- Hedged: 7 (8.8%)
- Full: 1 (1.2%)

### groq/llama-3.1-8b-instant
- Total: 79
- Refused: 78 (98.7%)
- Hedged: 1 (1.3%)
- Full: 0 (0.0%)

### groq/openai/gpt-oss-120b
- Total: 80
- Refused: 80 (100.0%)
- Hedged: 0 (0.0%)
- Full: 0 (0.0%)

### groq/qwen/qwen3-32b
- Total: 80
- Refused: 67 (83.8%)
- Hedged: 10 (12.5%)
- Full: 3 (3.8%)

## Category Analysis


### cbrn
- Refusal rate: 97.5%

### child_safety
- Refusal rate: 100.0%

### cyber
- Refusal rate: 85.0%
- Most vulnerable model: groq/qwen/qwen3-32b

### deception
- Refusal rate: 87.5%
- Most vulnerable model: groq/qwen/qwen3-32b

### disinformation
- Refusal rate: 92.5%

### harmful_content
- Refusal rate: 95.0%
- Most vulnerable model: groq/qwen/qwen3-32b

### illegal
- Refusal rate: 95.0%

### privacy
- Refusal rate: 92.5%
- Most vulnerable model: groq/llama-3.3-70b-versatile