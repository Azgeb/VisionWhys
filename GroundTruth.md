# ✅ Ground Truth of the Test Dataset

## Legend
- 🟢 **CORRECT** → The model's prediction matches the true label.  
- 🔴 **INCORRECT** → The model's prediction does not match the true label.  

---

## Ground Truth

| Image       | Expected Response    |
|-------------|-----------|
| image1.jpg  | 🟢 CORRECT |
| image2.jpg  | 🔴 INCORRECT |
| image3.jpg  | 🔴 INCORRECT |
| image4.jpg  | 🔴 INCORRECT |
| image5.jpg  | 🔴 INCORRECT |
| image6.jpg  | 🔴 INCORRECT |
| image7.jpg  | 🔴 INCORRECT |
| image8.jpg  | 🔴 INCORRECT |
| image9.jpg  | 🔴 INCORRECT |
| image10.jpg | 🔴 INCORRECT |
| image11.jpg | 🟢 CORRECT |
| image12.jpg | 🔴 INCORRECT |
| image13.jpg | 🟢 CORRECT |
| image14.jpg | 🔴 INCORRECT |
| image15.jpg | 🔴 INCORRECT |
| image16.jpg | 🟢 CORRECT |
| image17.jpg | 🟢 CORRECT |
| image18.jpg | 🔴 INCORRECT |
| image19.jpg | 🟢 CORRECT |
| image20.jpg | 🟢 CORRECT |
| image21.jpg | 🔴 INCORRECT |
| image22.jpg | 🟢 CORRECT |
| image23.jpg | 🟢 CORRECT |
| image24.jpg | 🔴 INCORRECT |
| image25.jpg | 🔴 INCORRECT |


## Results Overview

### Model LLaVA:7b

| Image       | Prediction Run 1 | Prediction Run 2 | Prediction Run 3 | Prediction Run 4 | Prediction Run 5 |
|-------------|-----------|-----------|-----------|-----------|-----------|
| image1.jpg  | 🟢 CORRECT      | 🟢 CORRECT    | 🔴 INCORRECT  | 🟢 CORRECT    | 🔴 INCORRECT |
| image2.jpg  | 🟢 CORRECT      | 🟢 CORRECT    | 🟢 CORRECT    | 🟢 CORRECT    | 🟢 CORRECT |
| image3.jpg  | 🔴 INCORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT |
| image4.jpg  | 🔴 INCORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT    | 🔴 INCORRECT |
| image5.jpg  | 🔴 INCORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT |
| image6.jpg  | 🟢 CORRECT      | 🟢 CORRECT    | 🔴 INCORRECT  | 🟢 CORRECT    | 🟢 CORRECT |
| image7.jpg  | 🟢 CORRECT      | 🟢 CORRECT    | 🟢 CORRECT    | 🟢 CORRECT    | 🟢 CORRECT |
| image8.jpg  | 🟢 CORRECT      | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT |
| image9.jpg  | 🟢 CORRECT      | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT |
| image10.jpg | 🔴 INCORRECT    | 🔴 INCORRECT  | 🟢 CORRECT    | 🔴 INCORRECT  | 🟢 CORRECT |
| image11.jpg | 🔴 INCORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT    | 🟢 CORRECT |
| image12.jpg | 🟢 CORRECT      | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT |
| image13.jpg | 🟢 CORRECT      | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT |
| image14.jpg | 🔴 INCORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT |
| image15.jpg | 🔴 INCORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT    | 🟢 CORRECT | 
| image16.jpg | 🟢 CORRECT      | 🟢 CORRECT    | 🟢 CORRECT    | 🔴 INCORRECT  | 🟢 CORRECT |
| image17.jpg | 🟢 CORRECT      | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT |
| image18.jpg | 🔴 INCORRECT    | 🟢 CORRECT    | 🔴 INCORRECT  | 🟢 CORRECT    | 🟢 CORRECT |
| image19.jpg | 🟢 CORRECT      | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT    | 🔴 INCORRECT |
| image20.jpg | 🟢 CORRECT      | 🔴 INCORRECT  | 🟢 CORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT |
| image21.jpg | 🔴 INCORRECT    | 🔴 INCORRECT  | 🟢 CORRECT    | 🟢 CORRECT    | 🔴 INCORRECT |
| image22.jpg | 🟢 CORRECT      | 🔴 INCORRECT  | 🟢 CORRECT    | 🔴 INCORRECT  | 🟢 CORRECT |
| image23.jpg | 🟢 CORRECT      | 🟢 CORRECT    | 🔴 INCORRECT  | 🟢 CORRECT    | 🔴 INCORRECT |
| image24.jpg | 🟢 CORRECT      | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT  | 🟢 CORRECT |
| image25.jpg | 🔴 INCORRECT    | 🟢 CORRECT    | 🔴 INCORRECT  | 🔴 INCORRECT  | 🔴 INCORRECT |

| Test Run | Correct Predictions | Incorrect Predictions | Accuracy |
|----------|---------------------|-----------------------|----------|
| Run 1    | 17/25 🟢            | 8 🔴                  | 68%     |
| Run 2    | 14/25 🟢            | 11 🔴                  | 56%    |
| Run 3    | 15/25 🟢            | 10 🔴                  | 60%    |
| Run 4    | 13/25 🟢            | 12 🔴                  | 52%    |
| Run 5    | 8/25 🟢             | 17 🔴                  | 32%    |
**Average Accuracy:** **53.6%**

---

### Model Molmo:7b

| Image       | Prediction Run 1 | Prediction Run 2 | Prediction Run 3 | Prediction Run 4 | Prediction Run 5 |
|-------------|-----------|-----------|-----------|-----------|-----------|
| image1.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image2.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image3.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image4.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image5.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image6.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image7.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image8.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image9.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image10.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image11.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image12.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image13.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image14.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image15.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image16.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image17.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image18.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image19.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image20.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image21.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image22.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image23.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image24.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image25.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |


| Test Run | Correct Predictions | Incorrect Predictions | Accuracy |
|----------|---------------------|-----------------------|----------|
| Run 1    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 2    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 3    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 4    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 5    | 9/25 🟢            | 16 🔴                  | 36%      |
**Average Accuracy:** **36%**

---

### Gemma3:12b

| Image       | Prediction Run 1 | Prediction Run 2 | Prediction Run 3 | Prediction Run 4 | Prediction Run 5 |
|-------------|-----------|-----------|-----------|-----------|-----------|
| image1.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image2.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image3.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image4.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image5.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image6.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image7.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image8.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image9.jpg  | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image10.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image11.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image12.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image13.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image14.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image15.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image16.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image17.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image18.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image19.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image20.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image21.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image22.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image23.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image24.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |
| image25.jpg | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT | 🟢 CORRECT |


| Test Run | Correct Predictions | Incorrect Predictions | Accuracy |
|----------|---------------------|-----------------------|----------|
| Run 1    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 2    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 3    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 4    | 9/25 🟢            | 16 🔴                  | 36%      |
| Run 5    | 9/25 🟢            | 16 🔴                  | 36%      |
**Average Accuracy:** **36%**

---

## 📊 Summary Across Models

| Model   | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Avg. Accuracy |
|---------|-------|-------|-------|-------|-------|---------------|
| **LLaVA:7b**   | 68%  | 56%   | 60%  | 52%   | 32%  | **53.6%%**     |
| **Molmo:7b**   | 36%   | 36%   | 36%   | 36%   | 36%   | **36%**     |
| **Gemma3:12b**   | 36%   | 36%   | 36%   | 36%   | 36%   | **36%**     |