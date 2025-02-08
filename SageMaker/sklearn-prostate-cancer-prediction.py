import argparse
import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    # Argumentos que o SageMaker passa automaticamente
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN"))
    parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR"))
    
    args = parser.parse_args()

    # Carregando os dados do S3
    train_data_path = os.path.join(args.train, "train.csv")
    df = pd.read_csv(train_data_path)

    # Supondo que a coluna 'Early_Detection' seja o alvo (y) e o resto são features (X)
    y = df["Early_Detection"]
    X = df.drop(columns=["Early_Detection"])

    # Divisão em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinando o modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Avaliação do modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

    # Salvando o modelo no diretório que o SageMaker espera
    model_path = os.path.join(args.model_dir, "model.joblib")
    joblib.dump(model, model_path)
