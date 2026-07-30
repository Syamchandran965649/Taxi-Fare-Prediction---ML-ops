from src.model_training.trainer import ModelTrainer

# function that defines training pipeline

def main():
    trainer=ModelTrainer()
    trainer.load_data()
    trainer.split_data()
    results=trainer.train_all_models()
    print("\nFinal Results")

    for model_name,metrics in results.items():

        print(model_name)
        # print(metrics)
        for key,value in metrics.items():
            print(f"{key}:{value:4f}")
        print()

if __name__=="__main__":
    main()
