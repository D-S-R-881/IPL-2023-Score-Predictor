# IPL-2023-Score-Predictor
This is IPL 2023 First Innings score predictor.
This project is a machine learning model that predicts the final score of the first innings in an IPL cricket match. The model takes 8 parameters to make its predictions, including the teams playing, the venue, the current score, the number of wickets left, balls left, runs scored in last 5 overs and current run rate.<br>
Demo :- https://ipl-score-predictor.streamlit.app/

<div align="center">
  <img src="https://github.com/D-S-R-881/IPL-2023-Score-Predictor/assets/78027597/31ce9c41-88a1-45a3-8d20-8294720663fa" alt="Description of the image" width="600" height="400">
  <p><i>Front-End of the WebSite.</i></p>
</div>



The model was trained on a dataset of historical IPL matches. This model based on the data of the IPL matches form 2008 to 2022 and the first 17 matches of IPL 2023. The dataset includes information on the teams playing, the venue, the current score, the number of wickets left, and the final score of the first innings.
The model was developed using a machine learning pipeline that includes data preprocessing, feature engineering, model training, and model evaluation. The model achieved an accuracy of approximately 95% for the XGBoost.

<b>Working Demo</b>

<div align="center">
  <img src="https://github.com/D-S-R-881/IPL-2023-Score-Predictor/assets/78027597/44959544-92e2-487b-a634-668e4d3f453d" alt="Description of the image" width="600" height="400">
  <p><i>Image 1</i></p>
</div>

Image 1 shows the input screen of the IPL 2023 First Innings Cricket Score Predictor. The user has selected the Lucknow Super Giants (LSG) as the batting team, the Punjab Kings as the bowling team, and the Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium as the venue. The current score is 64 runs, there are 8 wickets left, and 9 overs have been bowled. The runs scored in the last 5 overs are 31. And in response to this input, the predicted score is 160 runs.

The final score of this match is

<div align="center">
  <img src="https://github.com/D-S-R-881/IPL-2023-Score-Predictor/assets/78027597/bb288a77-d4ff-445e-b3f4-6ba8408d6194" alt="Description of the image" width="500" height="150">
  <p><i>Image 2</i></p>
</div>

Image 2 shows that the actual final score of the LSG's first innings. The LSG scored 159 runs, which is close to the model's prediction of 160 runs.

<div align="center">
  <img src="https://github.com/D-S-R-881/IPL-2023-Score-Predictor/assets/78027597/1e2315ef-3bac-4147-84ae-ddaaccc4d019" alt="Description of the image" width="500" height="100">
  <p><i>Image 3</i></p>
</div>

<div align="center">
  <img src="https://github.com/D-S-R-881/IPL-2023-Score-Predictor/assets/78027597/f8925b0d-649d-4708-8fa6-cd040f312696" alt="Description of the image" width="500" height="100">
  <p><i>Image 4</i></p>
</div>

Image 3 and Image 4 shows the score of LSG at the end of 4 overs and at the end of 9 overs respectively. So from this we can tell that the runs scored by LSG in last 5 overs are 31, which is required by our model and similarily we can input required things in the model to get the final score predicted by the model.

Overall, these images show that the IPL 2023 First Innings Cricket Score Predictor is able to make accurate predictions of the final score of the first innings, even when only a few overs have been bowled.
