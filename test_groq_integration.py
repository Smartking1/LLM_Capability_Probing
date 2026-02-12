"""
Quick test script to verify Groq API integration.

This script tests:
1. Groq API key is set
2. Groq client can be initialized
3. Basic API call works
4. Configuration is valid
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

def test_api_key():
    """Test that Groq API key is set."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY environment variable not set")
        print("   Set it with: export GROQ_API_KEY=your_key_here")
        print("   Get your key from: https://console.groq.com/keys")
        return False
    print("✓ GROQ_API_KEY is set")
    return True

def test_groq_import():
    """Test that Groq SDK can be imported."""
    try:
        from groq import Groq
        print("✓ Groq SDK imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import Groq SDK: {e}")
        print("   Install with: pip install groq")
        return False

def test_groq_connection():
    """Test basic Groq API connection."""
    try:
        from groq import Groq
        api_key = os.getenv("GROQ_API_KEY")
        client = Groq(api_key=api_key)
        
        # Make a simple test call
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say 'test successful' if you can read this."}],
            max_tokens=20,
        )
        
        result = response.choices[0].message.content
        print(f"✓ Groq API connection successful")
        print(f"  Test response: {result[:50]}...")
        return True
    except Exception as e:
        print(f"❌ Groq API connection failed: {e}")
        return False

def test_config():
    """Test that configuration is valid."""
    try:
        import yaml
        config_path = Path(__file__).parent / "config" / "config.yaml"
        
        with config_path.open() as f:
            config = yaml.safe_load(f)
        
        # Check models are configured
        models = config.get("models", {})
        if not models:
            print("❌ No models configured in config.yaml")
            return False
        
        # Check all models use Groq
        groq_models = [m for m in models.values() if m.get("api_type") == "groq"]
        if len(groq_models) != len(models):
            print(f"❌ Not all models use Groq API type")
            return False
        
        print(f"✓ Configuration valid ({len(models)} Groq models configured)")
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_classifier():
    """Test that classifier can be initialized."""
    try:
        from common import MultiJudgeClassifier
        
        api_key = os.getenv("GROQ_API_KEY")
        classifier = MultiJudgeClassifier(
            num_judges=2,  # Use fewer judges for quick test
            api_key=api_key
        )
        print("✓ MultiJudgeClassifier initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Classifier initialization failed: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("Groq API Integration Test")
    print("=" * 60)
    print()
    
    tests = [
        ("API Key", test_api_key),
        ("Groq SDK Import", test_groq_import),
        ("Groq API Connection", test_groq_connection),
        ("Configuration", test_config),
        ("Classifier", test_classifier),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\nTesting {name}...")
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            results.append(False)
    
    print()
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! System is ready to use.")
        print()
        print("Next steps:")
        print("  1. Run test mode: python run_capability_probing.py --test")
        print("  2. Run full evaluation: python run_capability_probing.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
    print("=" * 60)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
