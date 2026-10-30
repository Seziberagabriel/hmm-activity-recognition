# Human Activity Recognition with a Hidden Markov Model

**Author:** Gabriel Tuyisingize Sezibera
**Course:** ML Techniques 2

A Gaussian HMM implemented from scratch in NumPy (Viterbi + Baum-Welch)
that recognises four activities (standing, walking, jumping, still)
from smartphone accelerometer and gyroscope data

## Results
Accuracy on 2 unseen test sessions: 93.8% (64 windows).

## Videos (data collection)
- Standing: https://youtube.com/shorts/bWs7e355IRA?si=bp6l2l6_ILUUdO3N 
- Walking: https://youtube.com/shorts/LVlvyvSqQ68?si=hGQQ5hofgmKCwEuR
- Jumping: https://youtube.com/shorts/ABJUtjdIHaQ?si=j9N_RQaY79EPhAlP
- Still: https://youtube.com/shorts/ID47XmfWIRY?si=KypBWbRG1UT6vA_w 
  
## Repository contents
- `data/train/<activity>/`: 15 labelled CSV recordings per activity (iPhone 11,
  Sensor Logger, ~99.4 Hz)
- `data/test/`: two unseen continuous sessions with label files
- `hmm_activity_recognition.ipynb`: feature extraction, HMM, evaluation
- `scripts/convert_sensorlogger.py`: converts Sensor Logger exports to the CSV format used here
- `figures/`: plots used in the report

## Data format
Each CSV has the columns `timestamp, ax, ay, az, gx, gy, gz`.
Label files for test sessions have the columns `start, end, label` (seconds).

## How to run
1. Open `hmm_activity_recognition.ipynb` in Google Colab.
2. Upload the `data/` folder next to the notebook (or mount Google Drive).
3. Run all cells from the "1. Configuration and imports" cell down.
