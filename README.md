# CekDulu - Is it a hoax or true information?

The information detection process, including distinguishing between hoaxes and true information, is built using the IndoBERT model. The achieved accuracy is approximately 97%. If the prediction is labeled as a hoax, a second prediction is performed for a more detailed hoax classification. The level 2 classification model for hoaxes utilizes NBSVM. The detailed misclassification/hoax classification is not applied to all categories due to the consideration of the number of data records.

The prediction results consist of the class/label and its probability.

The demo video can be watched here: https://drive.google.com/file/d/1i68jlsxg1T4yW_RrMNPO1T9a6winMgSO/view?usp=drive_link

p.s.: 
- I developed this after a long period of not working with text data.
- It was supposed to be available on the web app (Streamlit), but it might be too resource-intensive, so it no longer works.
