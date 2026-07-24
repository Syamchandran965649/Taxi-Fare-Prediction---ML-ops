from src.model_training.trainer import ModelTrainer

# function that defines training pipeline

def main():
    trainer=ModelTrainer()
    trainer.load_data()
    trainer.split_data()
    trainer.train_random_forest()

if __name__=="__main__":
    main()
