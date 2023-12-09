import mlflow
import optuna
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def objective(trial):
    k = trial.suggest_int("k", 5,10)   

    model = KMeans(n_clusters=k, random_state=0, n_init=10).fit(filtered_tfidf)
    score = silhouette_score(filtered_tfidf, model.predict(filtered_tfidf))

    return score

def main():
    with mlflow.start_run():
        best_score = -1
        best_k = None
        metrics = []

        study = optuna.create_study(direction="maximize")
        study.optimize(objective, n_trials=10)

        mlflow.log_param("best_k", study.best_params["k"])
        mlflow.log_param("best_score", study.best_value)

        fig, ax = plt.subplots()
        ax.plot(range(2, 21), [trial.value for trial in study.trials])
        ax.set_xlabel("$K$")
        ax.set_ylabel("Silhouette Score")
        ax.set_xticks(range(2, 21))
        ax.set_title('Variation of Silhouette Score with Different K Values')
        plt.savefig("silhouette_scores_plot.png")
        mlflow.log_artifact("silhouette_scores_plot.png")

        best_k_optuna = study.best_params["k"]
        best_score_optuna = study.best_value

        print(f"Best K (Optuna): {best_k_optuna}")
        print(f"Best Silhouette Score (Optuna): {best_score_optuna}")

if __name__ == "__main__":
    # Load your data (assuming 'filtered_tfidf' is defined)
    # filtered_tfidf = ...

    main()