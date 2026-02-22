import os
import traceback
import google.generativeai as genai

# Use environment variable first for safety, otherwise fallback to hardcoded (not recommended)
api_key = os.environ.get("GEMINI_API_KEY") or ""

if not api_key:
    print("Warning: No API key set in GEMINI_API_KEY environment variable.")
    print("If you want to run with a key here (not recommended), set it in the script or export GEMINI_API_KEY.")

genai.configure(api_key=api_key)

def main():
    try:
        print("Testing Gemini API connection (list models)...")
        models = genai.list_models()
        count = 0
        for m in models:
            count += 1
            # Print representative fields if available
            if isinstance(m, dict):
                name = m.get('name') or m.get('id') or str(m)
            else:
                name = getattr(m, 'name', None) or str(m)
            print(f" - {name}")
        print(f"Total models returned: {count}")
    except Exception as e:
        print("\nFull exception traceback:")
        traceback.print_exc()
        print("\nDetected API Key / API access issue.")
        print("Checklist:")
        print(" - Ensure GEMINI_API_KEY is set and correct")
        print(" - Enable the generative AI (Gemini) API in Google Cloud / MakerSuite")
        print(" - Check API key restrictions (HTTP referrers, IPs, service restrictions)")
        print(" - Check project quotas and billing status")

if __name__ == '__main__':
    main()
