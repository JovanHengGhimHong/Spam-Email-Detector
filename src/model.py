import torch
import numpy as np
import torch.nn as nn
from torch.utils.data import Subset, DataLoader
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score

# predicts on recall
def train_kf(input_model, params, train_loader, loss_fn, optimizer, kf, batch_size=None, epochs=10, early_stop=False, patience=5):
  if batch_size is None:
    batch_size = train_loader.batch_size

  total_recalls = []
  total_precisions = []
  total_f1s = []
  total_accuracies = []
  

  for fold, (train_idx, val_idx) in enumerate(kf.split(train_loader.dataset, 
                                                     [y for _, y in train_loader.dataset])):
    print(f"\nFold {fold+1}/{kf.get_n_splits()}")
    
    train_subset = Subset(train_loader.dataset, train_idx)
    val_subset = Subset(train_loader.dataset, val_idx)

    train_subset_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=True)
    val_subset_loader = DataLoader(val_subset, batch_size=batch_size, shuffle=False)

    # actual training
    model = input_model(**params)
    optm = optimizer(model.parameters(), lr=params['lr'] if 'lr' in params else 1e-03)
    model.fit(epochs, train_subset_loader, loss_fn, optm, early_stop=early_stop, patience=patience)

    # predict on validation
    predictions = model.predict(val_subset_loader)
    y_true = [y for _, y in val_subset_loader.dataset]
    fold_recall = recall_score(y_true, predictions, average='macro')
    fold_precision = precision_score(y_true, predictions, average='macro')
    fold_f1 = f1_score(y_true, predictions, average='macro')
    fold_accuracy = accuracy_score(y_true, predictions)

    # storing
    total_recalls.append(fold_recall)
    total_precisions.append(fold_precision)
    total_f1s.append(fold_f1)
    total_accuracies.append(fold_accuracy)

    # report
    print('=' * 40, end='\n')
    print(f"Fold {fold+1}:")
    print(f"Validation Recall: {fold_recall:.3f}")
    print(f"Validation Precision: {fold_precision:.3f}")
    print(f"Validation F1 Score: {fold_f1:.3f}")
    print(f"Validation Accuracy: {fold_accuracy:.3f}")
    print('=' * 40, end='\n')


  return {
    'recall': np.mean(total_recalls),
    'precision': np.mean(total_precisions),
    'f1': np.mean(total_f1s),
    'accuracy': np.mean(total_accuracies)
  }


    

class Model(nn.Module):
  '''
  This Model serves as a base class for all models.
  
  This model predicts on recall
  '''
  def __init__(self):
    super().__init__()
    self.accuracy_history = []
    self.loss_history = []
    # user defines layers 
   
  def forward(self, x):
    # user defines forward pass
    return x

  def fit(self, epochs, train_loader, loss_fn, optimizer, early_stop=False, patience=5):
    super().train()

    if patience < 1:
      raise ValueError("Patience must be at least 1.")

    if early_stop is False and patience > 0:
      print("Warning: Patience is set but early_stop is False. Patience will be ignored.")

    min_loss = np.inf
    wait = 0
    for i in range(epochs):
      epoch_loss = 0.0
      total = 0 
      correct = 0 
      for x_batch, y_batch in train_loader:
        # reset gradients
        optimizer.zero_grad()

        logits = self(x_batch)

        # back propagation
        loss = loss_fn(logits, y_batch)
        loss.backward()
        
        # update weights
        optimizer.step()
        
        # store weights
        epoch_loss += loss.item()
        
        # compute accuracy
        predictions = logits.argmax(dim=1)
      
        total += y_batch.size(0)
        correct += (predictions == y_batch).sum().item()
        

      epoch_accuracy = correct / total * 100

      # storing
      self.accuracy_history.append(epoch_accuracy)
      self.loss_history.append(epoch_loss)

      print(f"Epoch {i+1}/{epochs}, Loss: {epoch_loss/len(train_loader):.4f}, Accuracy: {epoch_accuracy:.2f}%")

      # early stopping check
      # early stop to always track loss
      if early_stop == False:
        continue
      
      if epoch_loss < min_loss:
        min_loss = epoch_loss
        wait = 0
        continue

      wait += 1
      if wait >= patience:
        print(f"Early stopping at epoch {i+1} due to no improvement in validation loss for {patience} consecutive epochs.")
        break

  def predict(self, test_loader):
    super().eval()
    predictions = []

    with torch.no_grad():
      for x_batch, _ in test_loader:
        logits = self(x_batch)
        preds = logits.argmax(dim=1)
        predictions.extend(preds.tolist())

    return predictions

    
if __name__ == '__main__':
  pass