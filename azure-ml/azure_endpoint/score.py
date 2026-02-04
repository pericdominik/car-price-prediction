import json
import os
import joblib
import pandas as pd
import traceback

def _find_file(root_dir, filename):
    for root, _, files in os.walk(root_dir):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(f"{filename} not found under {root_dir}")

def init():
    global model
    global preprocessor

    try:
        model_dir = os.getenv("AZUREML_MODEL_DIR")
        print("AZUREML_MODEL_DIR =", model_dir)

        model_path = _find_file(model_dir, "final_model.pkl")
        preprocessor_path = _find_file(model_dir, "final_preprocessor.pkl")

        print("Model path:", model_path)
        print("Preprocessor path:", preprocessor_path)

        model = joblib.load(model_path)
        preprocessor = joblib.load(preprocessor_path)

        print("INIT SUCCESS")

    except Exception as e:
        print("INIT FAILED")
        print(str(e))
        print(traceback.format_exc())
        raise e  # OVO JE BITNO da Azure vidi da je init puknuo

def run(raw_data):
    try:
        data = json.loads(raw_data)

        if isinstance(data, dict):
            rows = [data]
        elif isinstance(data, list):
            rows = data
        else:
            return {"error": "Invalid input format"}

        df = pd.DataFrame(rows)
        X = preprocessor.transform(df)
        preds = model.predict(X)

        if len(preds) == 1:
            return {"predicted_price": float(preds[0])}

        return {"predicted_price": [float(p) for p in preds]}

    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }



